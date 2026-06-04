# Financial Agent - Skills and Context

## Agent Overview

The Financial Agent is a reasoning-based system designed to provide grounded, evidence-based financial analysis and reporting. It operates through two core skills: **Web Searching** for information retrieval and **Report Generation** for synthesized analysis. The agent strictly adheres to a no-hallucination principle, ensuring all outputs are grounded in retrieved documents and verified sources.

---

## Skill 1: Web Searching

### Purpose

Identify and generate potential web search prompts to augment local knowledge bases with external data sources when context is insufficient.

### Input

- User query or task requiring external information
- Similarity score threshold (indicates confidence level of local retrieval)
- Current context documents (retrieved from local RAG system)

### Output

**Array of Web Search Prompts** (Structured Format)

```json
{
  "prompts": [
    {
      "query": "string - specific, actionable web search query",
      "rationale": "string - why this search complements the current context",
      "priority": "high|medium|low",
      "expected_sources": ["source types or domains"]
    }
  ],
  "total_prompts": "number",
  "search_strategy": "string - overall approach for web augmentation"
}
```

### Guidelines

1. **Specificity**: Generate precise, queryable prompts rather than vague questions
2. **Complementarity**: Ensure searches fill gaps in existing local context
3. **Prioritization**: Rank prompts by relevance and urgency
4. **Source Awareness**: Suggest appropriate source types (e.g., news, financial reports, regulatory filings)
5. **Relevance Filtering**: Only generate web searches when local confidence is below acceptable threshold

### Example

**Query**: "What are the latest regulatory changes affecting fintech companies?"

**Output Array**:

```json
{
  "prompts": [
    {
      "query": "fintech regulatory changes 2026",
      "rationale": "Captures recent regulatory landscape shifts",
      "priority": "high",
      "expected_sources": ["financial_news", "regulatory_databases"]
    },
    {
      "query": "SEC fintech compliance requirements 2026",
      "rationale": "Provides specific U.S. regulatory guidance",
      "priority": "high",
      "expected_sources": ["official_regulatory", "compliance_guides"]
    },
    {
      "query": "global fintech regulation updates 2026",
      "rationale": "Captures international regulatory landscape",
      "priority": "medium",
      "expected_sources": ["financial_news", "international_reports"]
    }
  ],
  "total_prompts": 3,
  "search_strategy": "Multi-angle approach combining U.S., SEC, and global regulatory changes"
}
```

---

## Skill 2: Reasoning & Report Generation

### Purpose

Synthesize grounded, evidence-based analysis and reports exclusively from retrieved documents, with zero tolerance for hallucination.

### Input

- User query or analysis request
- Retrieved context documents (from RAG system)
- Similarity/confidence scores
- Web search augmentation data (optional)

### Output

**Structured Report with Evidence Trail**

```
[Report Title]

Executive Summary
- Concise overview grounded in retrieved sources

Key Findings
1. Finding 1
   - Source: [Document Title/Source]
   - Confidence: [Score]
   - Evidence: [Quote or paraphrase from source]

2. Finding 2
   - Source: [Document Title/Source]
   - Confidence: [Score]
   - Evidence: [Quote or paraphrase from source]

Limitations & Gaps
- Data limitations
- Gaps in local context
- Areas requiring external research

Recommendations
[Only when supported by retrieved documents]
```

### Core Principles - NO HALLUCINATION

1. **Source Attribution**: Every claim must cite its source document
2. **Evidence Trail**: Quote or explicitly paraphrase from sources
3. **Confidence Marking**: Indicate confidence level for each finding
4. **Gap Identification**: Explicitly state what information is missing or unavailable
5. **Assertion Blocking**: If no grounded context exists, clearly state the limitation
   - Do Say: "This information is not available in the current knowledge base"
   - Don't Say: "Based on trends, this will likely happen..."

### Fallback Behavior

When context documents are insufficient:

```
Insufficient Context Response:

Query: [User Query]
Confidence Score: [Low Score]

Status: Unable to generate grounded analysis

Reason: The current knowledge base does not contain sufficient evidence to support reliable findings on this topic.

Available Evidence:
- [List any partial/related findings from weak sources]

Recommended Action:
- Consider web search prompts for external data
- Provide additional source materials
- Refine the query for better context matching
```

### Example Report

**Query**: "Summarize the Q3 financial performance of our investment portfolio"

**Output**:

```
Financial Portfolio Performance - Q3 Analysis

Executive Summary
Based on retrieved quarterly reports, the portfolio demonstrated mixed performance
with gains in technology sectors offset by regulatory pressures in fintech holdings.

Key Findings

1. Technology Sector Growth
   - Source: Q3 Investment Report (Oct 2024)
   - Confidence: 0.87
   - Evidence: "Technology holdings increased 12% quarter-over-quarter,
     driven primarily by AI infrastructure stocks"

2. Fintech Regulatory Headwinds
   - Source: Q3 Compliance Summary (Oct 2024)
   - Confidence: 0.92
   - Evidence: "Regulatory compliance costs increased 15% due to new
     SEC guidelines on digital assets"

3. Overall Portfolio Return
   - Source: Q3 Financial Statements (Oct 2024)
   - Confidence: 0.95
   - Evidence: "Portfolio achieved 8.3% total return, exceeding
     benchmark by 1.2 percentage points"

Limitations & Gaps
- Quarterly reports do not contain detailed forward-looking guidance
- Specific asset allocation by manager is not available
- Market condition projections would require external research sources

Recommendations
All recommendations are supported by Q3 reports:
- Maintain overweight position in technology (as suggested in portfolio review)
- Monitor fintech holdings for additional regulatory impacts
```

---

## Integration with LLM Module

The agent's reasoning outputs are generated through the `synthesize()` method in `llm.py`, which:

1. Validates context document availability
2. Constructs grounded findings from retrieved documents
3. Maintains confidence scores from RAG retrieval
4. Tracks web search augmentation usage
5. Generates structured output with source attribution

---

## Decision Flow

```
User Query
    ↓
[Web Searching Skill]
    → Generate search prompts array
    → If confidence sufficient: STOP
    → If confidence low: Return prompts for external search
    ↓
[External Data Retrieved?]
    → YES: Augment local context
    → NO: Use local context only
    ↓
[Reasoning & Report Generation Skill]
    → Extract grounded findings
    → Attribute to sources
    → Mark confidence scores
    → Identify gaps
    → Generate report
    ↓
Final Report (No Hallucination)
```

---

## Quality Assurance Checklist

For every generated report, verify:

- [ ] All factual claims have source attribution
- [ ] Confidence scores are realistic (0.0-1.0)
- [ ] Gaps and limitations are clearly stated
- [ ] No predictions or inferences beyond retrieved data
- [ ] Web search prompts are concrete and actionable
- [ ] Report structure includes evidence trails
- [ ] Fallback messaging is used when context is insufficient
