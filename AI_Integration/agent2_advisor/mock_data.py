"""
Mock datasets simulating RAG chunks and user queries for Tesla 2022 10-K.
Provides real numbers extracted from the official Form 10-K.
"""

USER_QUERY = (
    "Please give some advice of Tesla's financial health and future outlook,"
    "based on the attached financial statements."
)

MOCK_CONTEXT_DOCS = [
    {
        "source": "NASDAQ_TSLA_2022.pdf (Page 4) - Business Overview",
        "text": (
            "Tesla, Inc. designs, develops, manufactures, sells and leases high-performance fully electric vehicles "
            "and energy generation and storage systems, and offers services related to its products. "
            "The company operates in two reportable segments: (i) automotive and (ii) energy generation and storage. "
            "The automotive segment includes consumer vehicles: Model 3, Model Y, Model S, and Model X, "
            "and commercial vehicle Tesla Semi. It also includes automotive regulatory credits sales. "
            "The energy generation and storage segment includes lithium-ion battery energy storage products: "
            "Powerwall (residential scale) and Megapack (commercial/utility scale), and Solar Roof offerings."
        )
    },
    {
        "source": "NASDAQ_TSLA_2022.pdf (Page 5 & 8) - Technology and Manufacturing",
        "text": (
            "Tesla's core vehicle technology competencies include powertrain engineering, proprietary battery cell (4680 cell) "
            "manufacturing, and advanced driver assist systems under Autopilot and Full Self-Driving (FSD) options. "
            "In 2022, Tesla previewed Optimus, a robotic humanoid controlled by the same AI system as FSD.\n"
            "Manufacturing facilities are located globally at Gigafactory Texas (Austin), Fremont (California), "
            "Gigafactory Nevada (Reno), Gigafactory New York (Buffalo), Gigafactory Shanghai (China), "
            "and Gigafactory Berlin-Brandenburg (Germany). Localizing production reduces transportation costs and tariff exposure."
        )
    },
    {
        "source": "NASDAQ_TSLA_2022.pdf (Page 8 & 9) - Supply Chain and Incentives",
        "text": (
            "Tesla's products use raw materials including aluminum, steel, cobalt, lithium, nickel, and copper. "
            "Single-source supplier dependencies for key components pose supply chain disruption risks. "
            "On August 16, 2022, the Inflation Reduction Act of 2022 (IRA) was enacted, providing clean energy incentives, "
            "including federal tax credits of up to $7,500 for eligible Tesla EV buyers in the U.S. through 2032. "
            "Automotive regulatory credits generated in 2022 were sold to other auto manufacturers for compliance."
        )
    },
    {
        "source": "NASDAQ_TSLA_2022.pdf (Part II, Item 8) - Consolidated Balance Sheets & Operations",
        "text": (
            "Tesla, Inc. Consolidated Financial Statements as of December 31, 2022 (values in Millions of USD):\n"
            "- Total Revenues (Sales): $81,462\n"
            "- Income from Operations (EBIT): $13,656\n"
            "- Total Assets: $82,338\n"
            "- Total Liabilities: $36,440\n"
            "- Retained Earnings: $12,885\n"
            "- Total Current Assets: $40,917\n"
            "- Total Current Liabilities: $26,709\n"
            "- Working Capital: $14,208 (Calculated as Current Assets $40,917 - Current Liabilities $26,709)\n"
            "- Market Capitalization (Market Value of Equity as of Dec 31, 2022): $389,000 (roughly 3.16B shares outstanding @ ~$123/share)\n"
            "- Book Value of Equity (Shareholders' Equity): $45,898\n"
            "- Total Debt (Recourse + Non-recourse): $5,748\n"
            "- Interest Expense: $191"
        )
    }
]
