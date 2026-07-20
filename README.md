# EduPilot-AI
> An AI-Powered Academic & Career Copilot for University Students

EduPilot AI is a full-stack AI platform that helps students with document understanding, study assistance, research, placement preparation, AI project mentoring, and productivity management — all in one modern dashboard.

Built with FastAPI, React, TypeScript, LangGraph, RAG, OCR, ChromaDB, and LLMs (OpenAI / Gemini).
---

## Features

### AI Document Assistant
- Upload PDF, DOCX, PPTX, TXT and images
- OCR fallback for scanned documents (Tesseract / EasyOCR)
- Multi-document semantic search over your whole corpus
- Citation-aware AI responses (source + page number)
- Conversation memory across sessions
- RAG-based document understanding via a LangGraph agent

### AI Study Assistant
- Smart notes generator
- Chapter summaries (concise / detailed / bullet-point)
- Flashcards
- MCQ quiz generator
- Exam-focused "important topics" prediction
- Mind map generation

### Research Assistant
- Research paper summarization
- Literature review generator
- Research gap detection
- Multi-paper comparison tables
- APA & BibTeX citation generator

### Placement Assistant
- Resume parser
- ATS resume scoring + actionable feedback
- Resume vs. job description matching
- Skill gap analysis
- Interview question generator
- Company-wise placement prep roadmap

### AI Project Mentor
- AI-generated project ideas
- Software architecture (Mermaid diagrams)
- Folder structure generator
- Database schema generator (SQL)
- REST API design
- Professional GitHub README generator

### Productivity Assistant
- AI study planner / timetable generator
- Daily task management (create, list, delete)
- Goal tracking
- Deadline reminders
- Learning analytics dashboard


## System Architecture

```text
                    React + TypeScript
                           |
                           v
                  FastAPI REST Backend
                           |
          +----------------+-----------------+
          v                v                 v
 Authentication      AI Services      Document Processing
          |                |                 |
          v                v                 v
    JWT Security      LangGraph Agent      OCR Engine
                           |
                           v
                    Chroma Vector DB
                           |
                           v
                   OpenAI / Gemini API
```

Design principles:
- Repository pattern — `BaseRepository[T]` gives every model CRUD for free; concrete repos add domain-specific queries
- Dependency injection — FastAPI `Depends()` for DB sessions, current user, role guards
- Provider abstraction — `BaseAIProvider` decouples the app from OpenAI/Gemini; swap via `AI_PROVIDER` env var
- Async everywhere — SQLAlchemy async engine, async endpoints, in-process `BackgroundTasks` for document processing (Celery optional for production)
- Centralized exceptions — domain exceptions map to consistent JSON error responses

---

## Tech Stack

| Layer | Stack |
|---|---|
| Frontend | React, TypeScript, Tailwind CSS, Vite, Axios, Zustand |
| Backend | FastAPI, SQLAlchemy (async), Pydantic, JWT Auth, Repository Pattern |
| AI / ML | OpenAI GPT, Google Gemini, LangGraph, ChromaDB, Sentence Transformers |
| OCR | Tesseract OCR, EasyOCR (optional) |
| Database | SQLite (local dev, zero-config) / PostgreSQL (production) |
| DevOps | Docker, Docker Compose, GitHub Actions CI/CD |

---

## Project Structure

```text
edupilot-ai
|
|-- backend
|   |-- app
|   |   |-- core          # config, security (JWT), logging, exceptions
|   |   |-- db             # async session, declarative base
|   |   |-- models         # SQLAlchemy models
|   |   |-- schemas        # Pydantic request/response models
|   |   |-- repositories   # Repository pattern
|   |   |-- services       # business logic + AI provider + vector store
|   |   |-- agents         # LangGraph RAG agent
|   |   |-- api/v1/endpoints
|   |   |-- tasks          # Celery tasks (optional)
|   |   `-- main.py
|   |-- requirements.txt
|   `-- .env.example
|
|-- frontend
|   |-- src
|   |   |-- pages
|   |   |-- components
|   |   |-- services
|   |   `-- store
|   `-- package.json
|
|-- scripts
|-- docker-compose.yml
|-- README.md
`-- LICENSE
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Priyanshu90122/edupilot-ai.git
cd edupilot-ai
```

### 2. Backend setup

```bash
cd backend
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create your `.env` (copy from `.env.example` if present, or create fresh):

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key

# OR use OpenAI instead:
# AI_PROVIDER=openai
# OPENAI_API_KEY=your_openai_api_key
```

Note: Gemini model names change often — Google periodically retires dated models (`gemini-1.5-flash`, `gemini-2.0-flash`, `gemini-2.5-flash`, and the `text-embedding-004` embedding model have all been retired). This project uses the `gemini-flash-latest` alias for chat and `gemini-embedding-001` for embeddings so it keeps working without code changes. If Gemini calls ever return 404, check Google's deprecation page (https://ai.google.dev/gemini-api/docs/deprecations) for the current model name.

Run the backend:

```bash
python -m uvicorn app.main:app --reload
```

### 3. Frontend setup (separate terminal)

```bash
cd frontend
npm install
npm run dev
```

### 4. Open the app

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| Swagger docs | http://localhost:8000/api/docs |

---

## Docker (optional — Postgres + Redis + Celery stack)

```bash
cp backend/.env.docker.example backend/.env
# edit backend/.env: set SECRET_KEY + AI_PROVIDER + the matching API key

docker compose up --build
```

- Backend: http://localhost:8000/api/docs
- Frontend: http://localhost:3000
- Flower: http://localhost:5555

---

## Testing

```bash
cd backend
pytest --cov=app --cov-report=term-missing
```

---

## Auth Model

JWT access (60 min) + refresh (7 day) tokens, bcrypt password hashing, role-based access (`student` / `admin`). Every module route requires `Authorization: Bearer <access_token>`.

---
## Future Improvements

- Voice AI Assistant
- AI Tutor
- Multi-Agent Collaboration
- Mobile App
- AI Career Advisor
- Live Coding Interview Simulator
- Personalized Learning Recommendations

---

## License

This project is licensed under the MIT License.

---

## Author

Priyanshu Bisht
GitHub: https://github.com/Priyanshu90122

---

If you found this project useful, consider giving it a star on GitHub. It helps others discover the project and supports future development.
