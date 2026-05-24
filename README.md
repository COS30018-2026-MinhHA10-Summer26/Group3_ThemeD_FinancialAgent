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
```

## Run locally

Quick, reliable steps to run the project on your machine for development.

Prerequisites
- Git
- Node.js 18+ and npm (or pnpm)
- Python 3.11 or 3.12
- Optional: Docker / Docker Compose (for containerized run)

1) Backend — Python (recommended for development)

- Create and activate a virtual environment:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

- Install Python dependencies:

```bash
pip install -r requirements.txt
```

- Configure environment variables:

```bash
# If a template exists, copy it and edit values (API keys, DB URL, etc.)
cp .env.example .env 2>/dev/null || true
# Edit backend/.env and frontend/.env.local as needed
```

- Run the API server (from the `backend` folder):

```bash
cd api
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The backend will be reachable at http://localhost:8000 and OpenAPI docs at http://localhost:8000/docs.

2) Frontend — Next.js

```bash
cd frontend
npm install
# copy or create frontend/.env.local from template if needed
npm run dev
```

The frontend runs at http://localhost:3000 by default.

3) Run both with Docker Compose (optional)

If you prefer containers and a single command, use the included compose file:

```bash
docker compose up --build
```

4) Notes & troubleshooting
- Ports: frontend 3000, backend 8000. If occupied, change dev server ports or compose configuration.
- Env files: make sure API keys (OpenAI, etc.) and any DB connection strings are set. Do NOT commit secrets.
- Python version: use 3.11/3.12 to match dependencies; if you see native build errors, ensure your local toolchain (gcc/clang) is installed.
- If the frontend cannot reach the backend during development, check `frontend/src/auth.ts` and `frontend/src/lib/api.ts` for the configured backend base URL or proxy.

5) Running tests

Backend unit tests (if available):

```bash
cd backend
pytest
```

Frontend unit/integration tests (if available):

```bash
cd frontend
npm test
```
