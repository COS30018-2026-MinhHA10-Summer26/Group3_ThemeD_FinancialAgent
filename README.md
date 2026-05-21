# Intelligent Financial Research Agent

COS30018 — Intelligent Systems Project

## Project Overview

The Intelligent Financial Research Agent is an AI-powered multi-tool financial assistant designed to perform:

- financial information retrieval,
- market/news searching,
- retrieval-augmented generation (RAG),
- autonomous tool usage,
- financial reasoning,
- and structured report generation.

Unlike a standard chatbot, the system acts as an intelligent agent capable of selecting and using external tools dynamically to solve user financial analysis tasks.

---

# Core Features

## 1. AI Agent Orchestration

The system uses an agent workflow to:

- understand user intent,
- select appropriate tools,
- execute multi-step reasoning,
- synthesize responses.

Example:

```text
User Query
→ Search financial news
→ Retrieve stock data
→ Retrieve contextual documents
→ Analyze information
→ Generate report