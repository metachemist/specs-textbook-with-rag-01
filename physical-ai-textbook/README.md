# Physical AI & Humanoid Robotics Textbook

An AI-powered textbook with RAG capabilities, authentication, personalization, and localization features for Physical AI & Humanoid Robotics.

## Features

- **RAG Chatbot**: Ask questions about the textbook content and get AI-powered answers
- **User Authentication**: Sign up and log in to personalize your learning experience
- **Content Personalization**: Content adapts based on your hardware setup (e.g., Jetson Kit vs. Cloud)
- **Localization**: Content available in multiple languages (starting with Urdu)

## Tech Stack

- **Frontend**: Docusaurus (React-based SSG)
- **Backend**: FastAPI (Python)
- **Authentication**: Better-Auth
- **Vector Database**: Qdrant Cloud
- **Relational Database**: Neon Postgres
- **AI/LLM Services**: OpenAI SDK

## Project Structure

```
physical-ai-textbook/
├── README.md               # This file
├── .clauderc               # Proof of Agentic Workflow
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
│   │   ├── /services       # AI Logic (RAG pipeline, OpenAI wrapper)
│   │   └── /models         # Pydantic schemas
│   ├── requirements.txt
│   └── .env                # API Keys (OpenAI, Qdrant, Neon)
└── /scripts                # Utility scripts
    └── ingest.py           # Script to read /docs and upload to Qdrant
```

## Setup

### Prerequisites
- Node.js 18+ (for Docusaurus frontend)
- Python 3.11+ (for FastAPI backend)
- Access to OpenAI API (for embeddings and completions)
- Access to Qdrant Cloud (for vector storage)
- Access to Neon Postgres (for user data)

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys and database URLs
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

## Running the Application

### Start the Backend
```bash
# From the backend directory
cd backend
# Activate virtual environment if not already done
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Run the FastAPI server
uvicorn app.main:app --reload --port 8000
```
Backend will be available at `http://localhost:8000`

### Start the Frontend
```bash
# From the frontend directory
cd frontend

# Run the Docusaurus development server
npm start
```
Frontend will be available at `http://localhost:3000`

## Agentic Workflow

This project was developed using Claude Code Subagents for content generation and management, demonstrating the agentic workflow required for the hackathon.

## License

[Specify license here]