# Implementation Plan: AI-Powered Textbook with RAG

**Branch**: `001-ai-textbook-rag` | **Date**: 2025-12-30 | **Spec**: [link](spec.md)
**Input**: Feature specification from `/specs/001-ai-textbook-rag/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the implementation of an AI-powered textbook with RAG capabilities, authentication, personalization, and localization features for Physical AI & Humanoid Robotics. The system uses a hybrid static-dynamic architecture with Docusaurus for the static content layer and React components for dynamic features. The backend is built with FastAPI to handle AI/LLM requests, authentication, personalization, and localization services. The implementation fully satisfies all constitutional principles and includes research, data models, API contracts, and quickstart guide.

## Technical Context

**Language/Version**: Python 3.11 (for backend), JavaScript/TypeScript (for frontend), Qwen CLI (for agentic development)
**Primary Dependencies**: Docusaurus (React-based SSG), FastAPI (Python), Better-Auth (authentication), Qdrant (vector DB), Neon Postgres (relational DB), OpenRouter SDK (AI/LLM services), FastEmbed (local embeddings)
**Storage**: Neon Postgres for user profiles and authentication data, Qdrant Cloud for vector storage of textbook content for RAG functionality using FastEmbed (Local/Qdrant) for embeddings
**Testing**: pytest (for backend API tests), Jest (for frontend component tests), integration tests for RAG pipeline
**Target Platform**: Web application (client-server architecture), deployable on GitHub Pages or Vercel
**Project Type**: Web application (frontend + backend)
**Performance Goals**: RAG chatbot responses within 5 seconds using OpenRouter, Urdu translation within 10 seconds, 95% uptime during peak usage
**Constraints**: Must use Qwen CLI and Spec-Kit Plus for creation process, Better-Auth for authentication to qualify for bonus points, Qdrant Cloud Free Tier for vector storage, OpenRouter with xiaomi/mimo-v2-flash:free model to ensure zero cost
**Scale/Scope**: Support for 1000+ concurrent users, 4 curriculum modules, multi-language support (English/Urdu initially)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on the project constitution, this plan must align with the following principles:
- I. AI-Native Content Creation: The system will be designed from the ground up to work with AI systems for querying, personalization, and dynamic adaptation.
- II. Intelligent Querying (RAG Implementation): The system will implement a robust RAG Chatbot using OpenRouter API (Xiaomi MiMo-V2-Flash), FastAPI, Neon, and Qdrant.
- III. Agentic Workflow Integration: The project will demonstrate use of Qwen CLI Subagents for content generation and management.
- IV. Identity & Profiling System: A functional Sign-up/Sign-in system using Better-Auth will capture user's software/hardware background.
- V. Dynamic Personalization Engine: The system will include a feature that rewrites/adjusts chapter content based on user profile using OpenRouter API (Xiaomi MiMo-V2-Flash).
- VI. Localization & Accessibility: The project will include a real-time "Translate to Urdu" button for chapter content using OpenRouter API (Xiaomi MiMo-V2-Flash).

**Post-Design Re-evaluation**: All constitutional principles are satisfied by the implemented architecture:
- The hybrid static-dynamic architecture with Docusaurus and React components supports AI-native content creation
- The RAG pipeline using OpenRouter API (Xiaomi MiMo-V2-Flash), FastAPI, Neon, and Qdrant is fully implemented
- Qwen CLI is integrated for agentic development workflow
- Better-Auth is implemented for identity and profiling
- The personalization engine is designed to adapt content based on user profiles using OpenRouter API
- The localization feature includes Urdu translation capability using OpenRouter API

## Project Structure

### Documentation (this feature)

```text
specs/001-ai-textbook-rag/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
physical-ai-textbook/
├── README.md               # Submission Requirement (Video link, etc.)
├── .qwenrc                 # Proof of Agentic Workflow
├── /docs                   # The Content (Docusaurus)
│   ├── /intro              # Introduction & Hardware setup
│   ├── /module-1           # ROS 2 Content
│   ├── /module-2           # Gazebo/Unity Content
│   ├── /module-3           # NVIDIA Isaac Content
│   └── /module-4           # VLA & Capstone Content
├── /frontend               # Docusaurus Project
│   ├── /src
│   │   ├── /components     # React Components (ChatWidget, AuthButton)
│   │   └── /pages
│   ├── docusaurus.config.js
│   └── package.json
├── /backend                # FastAPI Project
│   ├── /app
│   │   ├── main.py         # Entry point
│   │   ├── /api            # Route handlers (chat, auth, personalize)
│   │   ├── /core           # Config (Env vars, DB connection)
│   │   ├── /services       # AI Logic (RAG pipeline, OpenRouter wrapper)
│   │   └── /models         # Pydantic schemas
│   ├── requirements.txt
│   └── .env                # API Keys (OpenRouter, Qdrant, Neon)
└── /scripts                # Utility scripts
    └── ingest.py           # Script to read /docs and upload to Qdrant using FastEmbed for local embedding
```

**Structure Decision**: Web application structure selected with separate frontend (Docusaurus) and backend (FastAPI) projects to handle static content delivery and dynamic AI-powered features respectively, with OpenRouter integration for zero-cost AI operations using local embeddings via FastEmbed.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
