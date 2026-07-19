"""
Financial and business strategic tools for the Advisor Agent.
All tools are written as Python functions that perform actual logic.
"""

import json
import mimetypes
import os
import re
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, Any, List
from uuid import uuid4

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(PROJECT_ROOT / "backend" / ".env")


def _parse_numeric_value(val: Any) -> float:
    """Helper to robustly parse a numeric value from float, int, or string containing currency, commas, or suffixes."""
    if isinstance(val, (int, float)):
        return float(val)
    if not val:
        return 0.0


    def _format_display_number(val: Any) -> str:
        """Format a numeric value for display without forcing unnecessary rounding.

        - Preserve integer appearance for whole numbers (e.g. 800000 -> "800,000").
        - For floats, show up to 6 decimal places but strip trailing zeros.
        - Non-numeric values are returned as-is or as "N/A" when falsy.
        """
        if val is None:
            return "N/A"
        if isinstance(val, (int,)):
            return f"{val:,}"
        if isinstance(val, float):
            # If effectively an integer, show without decimals
            if val.is_integer():
                return f"{int(val):,}"
            # Otherwise show up to 6 decimals, but trim trailing zeros
            s = f"{val:,.6f}".rstrip('0').rstrip('.')
            return s
        # Try to coerce strings that look numeric
        try:
            f = float(str(val).replace(',', '').strip())
            if f.is_integer():
                return f"{int(f):,}"
            s = f"{f:,.6f}".rstrip('0').rstrip('.')
            return s
        except Exception:
            return str(val) if val else "N/A"
    
    # Convert to string and clean
    s = str(val).strip()
    
    # Remove currency symbols, commas, spaces
    s = re.sub(r'[$,\s]', '', s)
    
    # Remove trailing M, B, K, m, b, k or words if they are suffixes
    # e.g., "81462M" -> "81462", "81462 million" -> "81462"
    s = re.sub(r'(?i)(million|billion|thousand|m|b|k)$', '', s)
    
    # Check for percentage
    is_percent = False
    if s.endswith('%'):
        is_percent = True
        s = s[:-1]
        
    try:
        num = float(s)
        if is_percent:
            num /= 100.0
        return num
    except ValueError:
        # Fallback: extract first numeric-looking substring
        match = re.search(r'[-+]?\d*\.?\d+', s)
        if match:
            try:
                num = float(match.group())
                if is_percent:
                    num /= 100.0
                return num
            except ValueError:
                pass
        return 0.0



def _normalize_supabase_url(raw_url: str) -> str:
    url = (raw_url or "").rstrip("/")
    if url.endswith("/rest/v1"):
        url = url[: -len("/rest/v1")]
    if url.endswith("/storage/v1"):
        url = url[: -len("/storage/v1")]
    return url


def _get_storage_config() -> Dict[str, str]:
    supabase_url = _normalize_supabase_url(os.getenv("SUPABASE_URL") or os.getenv("SUPABASE_PROJECT_URL") or "")
    service_role_key = (
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        or os.getenv("SUPABASE_SERVICE_ROLE")
        or os.getenv("SUPABASE_ANON_KEY")
        or ""
    )
    bucket = (
        os.getenv("SUPABASE_FIGURE_BUCKET")
        or os.getenv("SUPABASE_RAW_DATA_BUCKET")
        or "raw_data"
    )

    missing = []
    if not supabase_url:
        missing.append("SUPABASE_URL")
    if not service_role_key:
        missing.append("SUPABASE_SERVICE_ROLE_KEY")
    if not bucket:
        missing.append("SUPABASE_FIGURE_BUCKET or SUPABASE_RAW_DATA_BUCKET")

    if missing:
        raise ValueError(f"Supabase storage is not configured. Missing: {', '.join(missing)}")

    return {
        "supabase_url": supabase_url,
        "service_role_key": service_role_key,
        "bucket": bucket,
    }


def _slugify(value: str, fallback: str = "figure") -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value or "").strip("-_.").lower()
    return slug or fallback


def _upload_file_to_supabase(file_path: str, object_path: str, content_type: str) -> str:
    config = _get_storage_config()
    encoded_object_path = urllib.parse.quote(object_path, safe="/-_.~")
    request_url = (
        f"{config['supabase_url']}/storage/v1/object/"
        f"{config['bucket']}/{encoded_object_path}"
    )

    with open(file_path, "rb") as file_handle:
        request = urllib.request.Request(
            request_url,
            data=file_handle.read(),
            method="POST",
        )

    request.add_header("Authorization", f"Bearer {config['service_role_key']}")
    request.add_header("apikey", config["service_role_key"])
    request.add_header("x-upsert", "true")
    request.add_header("Content-Type", content_type or "application/octet-stream")

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            response.read()
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="ignore") or error.reason
        raise RuntimeError(f"Failed to upload figure to Supabase: {detail}") from error
    except urllib.error.URLError as error:
        raise RuntimeError("Failed to connect to Supabase storage while uploading figure.") from error

    return (
        f"{config['supabase_url']}/storage/v1/object/public/"
        f"{config['bucket']}/{encoded_object_path}"
    )


def _validate_figure_rows(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not data:
        raise ValueError("Figure data must contain at least one row.")
    if not all(isinstance(row, dict) for row in data):
        raise ValueError("Figure data must be a list of objects.")
    return data


def _markdown_table(data: List[Dict[str, Any]]) -> str:
    rows = _validate_figure_rows(data)
    columns = list(rows[0].keys())
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(column, "")) for column in columns) + " |")
    return "\n".join(lines)


def _render_chart_png(
    figure_type: str,
    title: str,
    data: List[Dict[str, Any]],
    x_key: str,
    y_keys: List[str],
    x_label: str,
    y_label: str,
) -> str:
    os.environ.setdefault("MPLCONFIGDIR", tempfile.gettempdir())

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    rows = _validate_figure_rows(data)
    if not x_key:
        x_key = list(rows[0].keys())[0]
    if not y_keys:
        y_keys = [key for key in rows[0].keys() if key != x_key]
    if not y_keys:
        raise ValueError("At least one numeric y_key is required for chart figures.")

    x_values = [str(row.get(x_key, "")) for row in rows]
    fig, ax = plt.subplots(figsize=(9, 5.2), dpi=160)

    if figure_type == "line_chart":
        for y_key in y_keys:
            y_values = [_parse_numeric_value(row.get(y_key, 0)) for row in rows]
            ax.plot(x_values, y_values, marker="o", linewidth=2, label=y_key)
    else:
        width = 0.8 / max(len(y_keys), 1)
        x_positions = list(range(len(x_values)))
        for index, y_key in enumerate(y_keys):
            y_values = [_parse_numeric_value(row.get(y_key, 0)) for row in rows]
            offsets = [position + (index - (len(y_keys) - 1) / 2) * width for position in x_positions]
            ax.bar(offsets, y_values, width=width, label=y_key)
        ax.set_xticks(x_positions)
        ax.set_xticklabels(x_values)

    ax.set_title(title or "Advisor Figure", fontsize=13, pad=14)
    ax.set_xlabel(x_label or x_key)
    ax.set_ylabel(y_label or ", ".join(y_keys))
    ax.grid(axis="y", alpha=0.25)
    if len(y_keys) > 1:
        ax.legend(frameon=False)
    fig.tight_layout()

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_path = temp_file.name
    temp_file.close()
    fig.savefig(temp_path, bbox_inches="tight")
    plt.close(fig)
    return temp_path

def comparison_tool(
    data_a: Dict[str, Any],
    data_b: Dict[str, Any],
    entity_a_name: str,
    entity_b_name: str
) -> str:
    """
    Compares key metrics of two entities and returns a formatted markdown table
    including absolute and percentage changes.

    ANTI-HALLUCINATION CONTRACT: All numeric values in data_a and data_b MUST
    be taken verbatim from source documents or prior tool outputs.
    Do NOT pass estimated, rounded, or training-knowledge values to this function.
    If an exact value is not available in the documents, omit that metric and
    note its absence in the report instead.

    Args:
        data_a: Dict of metric names and numeric values for entity A.
        data_b: Dict of metric names and numeric values for entity B.
        entity_a_name: Name of Entity A (e.g. "Tesla")
        entity_b_name: Name of Entity B (e.g. "BYD" or "Industry Average")
    """
    lines = [
        f"### Comparison Table: {entity_a_name} vs {entity_b_name}",
        "",
        f"| Metric | {entity_a_name} | {entity_b_name} | Change (Abs) | Change (%) |",
        "| :--- | :---: | :---: | :---: | :---: |"
    ]
    
    # Get all unique metrics from both datasets
    all_metrics = sorted(list(set(data_a.keys()) | set(data_b.keys())))
    
    for metric in all_metrics:
        val_a = data_a.get(metric)
        val_b = data_b.get(metric)

        # Format values using the display helper to avoid forced two-decimal rounding
        str_a = _format_display_number(val_a) if isinstance(val_a, (int, float)) or (val_a and str(val_a).strip()) else "N/A"
        str_b = _format_display_number(val_b) if isinstance(val_b, (int, float)) or (val_b and str(val_b).strip()) else "N/A"

        abs_diff_str = "N/A"
        pct_diff_str = "N/A"

        if isinstance(val_a, (int, float)) and isinstance(val_b, (int, float)):
            abs_diff = val_a - val_b
            sign = "+" if abs_diff >= 0 else "-"
            abs_formatted = _format_display_number(abs(abs_diff))
            abs_diff_str = f"{sign}{abs_formatted}"

            if val_b != 0:
                pct_diff = (abs_diff / val_b) * 100
                pct_diff_str = f"{pct_diff:+.2f}%"
            else:
                pct_diff_str = "+inf%"

        lines.append(f"| {metric} | {str_a} | {str_b} | {abs_diff_str} | {pct_diff_str} |")

    # Suspect-rounding detector: flag values that look like rounded estimates
    # (e.g. exactly $1B, $500M, $10B) which LLMs commonly hallucinate.
    _ROUND_THRESHOLDS = [1_000_000_000, 500_000_000, 100_000_000, 50_000_000, 10_000_000]
    suspect_metrics: list[str] = []
    all_values = list(data_a.values()) + list(data_b.values())
    for metric in all_metrics:
        va = data_a.get(metric)
        vb = data_b.get(metric)
        for v in (va, vb):
            if isinstance(v, (int, float)) and v != 0:
                abs_v = abs(float(v))
                if any(abs_v % threshold == 0 for threshold in _ROUND_THRESHOLDS):
                    if metric not in suspect_metrics:
                        suspect_metrics.append(metric)

    if suspect_metrics:
        lines.append("")
        lines.append(
            "> \u26a0\ufe0f **Data Quality Warning:** The following metric(s) contain values that appear to be "
            "rounded estimates rather than exact figures from source documents: "
            f"**{', '.join(suspect_metrics)}**. "
            "Verify these figures against the original filing before citing them."
        )

    return "\n".join(lines)


def risk_assessment_tool(financial_metrics: Dict[str, float]) -> Dict[str, Any]:
    """
    Performs quantitative risk analysis including Altman Z-Score for manufacturing companies,
    Debt-to-Equity, and Interest Coverage.
    
    Expects financial_metrics containing (values in millions/units):
        - working_capital
        - total_assets
        - retained_earnings
        - ebit (operating income)
        - market_cap (market value of equity)
        - total_liabilities
        - sales (revenues)
        - interest_expense (optional)
        - total_debt (optional)
        - equity (optional, book value)
    """
    metrics_cleaned = {k: _parse_numeric_value(v) for k, v in financial_metrics.items()}
    results: Dict[str, Any] = {}
    
    # 1. Altman Z-Score Calculation (for public manufacturing companies)
    # Z = 1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 0.99*X5
    wc = metrics_cleaned.get("working_capital")
    assets = metrics_cleaned.get("total_assets")
    re_earnings = metrics_cleaned.get("retained_earnings")
    ebit = metrics_cleaned.get("ebit")
    market_cap = metrics_cleaned.get("market_cap")
    liabilities = metrics_cleaned.get("total_liabilities")
    sales = metrics_cleaned.get("sales")
    
    if all(x is not None for x in [wc, assets, re_earnings, ebit, market_cap, liabilities, sales]) and assets > 0 and liabilities > 0:
        x1 = wc / assets
        x2 = re_earnings / assets
        x3 = ebit / assets
        x4 = market_cap / liabilities
        x5 = sales / assets
        
        z_score = (1.2 * x1) + (1.4 * x2) + (3.3 * x3) + (0.6 * x4) + (0.999 * x5)
        
        if z_score >= 2.99:
            zone = "Safe Zone (Low Bankruptcy Risk)"
        elif z_score > 1.81:
            zone = "Gray Zone (Moderate Bankruptcy Risk)"
        else:
            zone = "Distress Zone (High Bankruptcy Risk)"
            
        results["altman_z_score"] = {
            "score": round(z_score, 3),
            "zone": zone,
            "x1_working_capital_to_assets": round(x1, 4),
            "x2_retained_earnings_to_assets": round(x2, 4),
            "x3_ebit_to_assets": round(x3, 4),
            "x4_equity_mv_to_liabilities": round(x4, 4),
            "x5_sales_to_assets": round(x5, 4)
        }
    else:
        results["altman_z_score"] = "Insufficient data to compute Altman Z-Score."
        
    # 2. Debt-to-Equity Ratio
    debt = metrics_cleaned.get("total_debt")
    equity = metrics_cleaned.get("equity")
    if debt is not None and equity is not None and equity > 0:
        de_ratio = debt / equity
        results["debt_to_equity"] = round(de_ratio, 4)
    elif liabilities is not None and market_cap is not None and market_cap > 0:
        # Fallback using total liabilities and market capitalization
        de_ratio_market = liabilities / market_cap
        results["liabilities_to_market_cap"] = round(de_ratio_market, 4)
        
    # 3. Interest Coverage Ratio
    interest = metrics_cleaned.get("interest_expense")
    if ebit is not None and interest is not None and interest > 0:
        coverage = ebit / interest
        results["interest_coverage_ratio"] = round(coverage, 2)
        
    return results


def financial_calculator_tool(
    fixed_costs: float = 0.0,
    price_per_unit: float = 0.0,
    variable_cost_per_unit: float = 0.0,
    initial_investment: float = 0.0,
    net_profit: float = 0.0,
    beginning_value: float = 0.0,
    ending_value: float = 0.0,
    years: float = 0.0
) -> Dict[str, Any]:
    """
    Computes standard financial planning metrics:
    - Break-even Point in units
    - ROI (Return on Investment)
    - CAGR (Compound Annual Growth Rate)
    """
    fixed_costs = _parse_numeric_value(fixed_costs)
    price_per_unit = _parse_numeric_value(price_per_unit)
    variable_cost_per_unit = _parse_numeric_value(variable_cost_per_unit)
    initial_investment = _parse_numeric_value(initial_investment)
    net_profit = _parse_numeric_value(net_profit)
    beginning_value = _parse_numeric_value(beginning_value)
    ending_value = _parse_numeric_value(ending_value)
    years = _parse_numeric_value(years)
    
    results: Dict[str, Any] = {}
    
    # 1. Break-even calculation
    if price_per_unit > variable_cost_per_unit:
        contribution_margin = price_per_unit - variable_cost_per_unit
        break_even_units = fixed_costs / contribution_margin
        results["break_even"] = {
            "units": round(break_even_units, 2),
            "contribution_margin_per_unit": round(contribution_margin, 2),
            "break_even_revenue": round(break_even_units * price_per_unit, 2)
        }
    elif price_per_unit > 0:
        results["break_even"] = "Price per unit is less than or equal to variable cost. Never breaks even."
        
    # 2. ROI calculation
    if initial_investment > 0:
        roi = (net_profit / initial_investment) * 100
        results["roi_percentage"] = round(roi, 2)
        
    # 3. CAGR calculation
    if beginning_value > 0 and ending_value > 0 and years > 0:
        cagr = ((ending_value / beginning_value) ** (1 / years)) - 1
        results["cagr_percentage"] = round(cagr * 100, 2)
        
    return results


def framework_template_library(framework_name: str) -> str:
    """
    Returns markdown outline guidelines for selected business framework.
    """
    templates = {
        "SWOT": """
## SWOT Analysis
1. **Strengths:**
   * What are the core competitive advantages? (Example: Proprietary technology, economies of scale, strong brand).
   * What is the business doing best?
2. **Weaknesses:**
   * Which areas need improvement?
   * Where are there resource shortages or financial/supply chain difficulties?
3. **Opportunities:**
   * What market trends can be leveraged? (Example: IRA Tax Credits, shift to clean energy).
   * Opportunities to expand into new geographic markets or product lines?
4. **Threats:**
   * What barriers exist from new competitors or regulatory policies?
   * Supply chain disruption risks or volatile raw material prices?
""",
        "Porter_5_Forces": """
## Porter's Five Forces Model
1. **Bargaining Power of Suppliers:**
   * How many primary suppliers are there? What is the single-source risk level?
2. **Bargaining Power of Buyers:**
   * Can customers easily switch to alternative products?
3. **Threat of New Entrants:**
   * Are barriers to entry high or low? (Capital, technology, regulations).
4. **Threat of Substitutes:**
   * Are there alternative solutions that are cheaper or more convenient?
5. **Rivalry Among Existing Competitors:**
   * How many competitors are there and what is their scale?
""",
        "PESTEL": """
## PESTEL Analysis
*   **P (Political):** Impact of government policies and supporting tax incentives (such as IRA).
*   **E (Economic):** Interest rates, inflation, input material costs fluctuations.
*   **S (Social):** Trends in consumer shift toward sustainable living and clean energy.
*   **T (Technological):** Development of AI, battery technology, autonomous driving (Self-Driving).
*   **E (Environmental):** Climate change, carbon emissions, recycling regulations.
*   **L (Legal):** Vehicle safety standards, autonomous vehicle data privacy laws.
"""
    }
    
    name_clean = framework_name.upper().replace(" ", "_")
    if "SWOT" in name_clean:
        return templates["SWOT"]
    elif "PORT" in name_clean or "FORCE" in name_clean or "5" in name_clean:
        return templates["Porter_5_Forces"]
    elif "PEST" in name_clean:
        return templates["PESTEL"]
    else:
        return f"Framework '{framework_name}' not found in library. Please use SWOT, Porter_5_Forces, or PESTEL."


def figure_generation_tool(
    figure_type: str,
    title: str,
    data: List[Dict[str, Any]],
    x_key: str = "",
    y_keys: List[str] | None = None,
    x_label: str = "",
    y_label: str = "",
    caption: str = "",
    source_note: str = "",
) -> Dict[str, Any]:
    """
    Creates a report-ready figure.

    Supported figure_type values:
      - bar_chart: creates a PNG and uploads it to Supabase Storage.
      - line_chart: creates a PNG and uploads it to Supabase Storage.
      - table: returns a Markdown table without creating an image.

    PNG figures are stored in the configured Supabase bucket under
    advisor_figure/{figure_id}.png and returned as public URLs.
    """
    normalized_type = (figure_type or "").strip().lower()
    figure_id = f"fig_{uuid4().hex[:12]}"
    y_keys = y_keys or []

    if normalized_type == "table":
        table_markdown = _markdown_table(data)
        return {
            "figure_id": figure_id,
            "figure_type": "table",
            "file_path": None,
            "public_url": None,
            "markdown": table_markdown,
            "data_used": data,
            "caption": caption,
            "source_note": source_note,
            "storage_folder": None,
        }

    if normalized_type not in {"bar_chart", "line_chart"}:
        raise ValueError("figure_type must be one of: bar_chart, line_chart, table.")

    temp_path = _render_chart_png(
        normalized_type,
        title,
        data,
        x_key,
        y_keys,
        x_label,
        y_label,
    )

    try:
        safe_title = _slugify(title)
        object_path = f"advisor_figure/{figure_id}_{safe_title}.png"
        content_type = mimetypes.guess_type(temp_path)[0] or "image/png"
        public_url = _upload_file_to_supabase(temp_path, object_path, content_type)
    finally:
        try:
            os.unlink(temp_path)
        except OSError:
            pass

    alt_text = title or caption or figure_id
    markdown = f"![{alt_text}]({public_url})"
    if caption:
        markdown += f"\n\n*Figure: {caption}*"
    if source_note:
        markdown += f"\n\n*Source: {source_note}*"

    return {
        "figure_id": figure_id,
        "figure_type": normalized_type,
        "file_path": object_path,
        "public_url": public_url,
        "markdown": markdown,
        "data_used": data,
        "caption": caption,
        "source_note": source_note,
        "storage_folder": "advisor_figure",
    }
