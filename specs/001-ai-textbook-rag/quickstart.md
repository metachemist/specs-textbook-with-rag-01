# Quickstart Guide: AI-Powered Textbook with RAG

## Overview
This guide provides a quick setup and run instructions for the AI-powered textbook with RAG capabilities, authentication, personalization, and localization features for Physical AI & Humanoid Robotics.

## Prerequisites
- Node.js 18+ (for Docusaurus frontend)
- Python 3.11+ (for FastAPI backend)
- Access to OpenAI API (for embeddings and completions)
- Access to Qdrant Cloud (for vector storage)
- Access to Neon Postgres (for user data)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd physical-ai-textbook
```

### 2. Backend Setup
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

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

### 4. Environment Configuration
Create a `.env` file in the backend directory with the following variables:
```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
DATABASE_URL=your_neon_postgres_connection_string
SECRET_KEY=your_secret_key_for_auth
```

## Running the Application

### 1. Start the Backend
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

### 2. Start the Frontend
```bash
# From the frontend directory
cd frontend

# Run the Docusaurus development server
npm start
```
Frontend will be available at `http://localhost:3000`

## Ingesting Textbook Content
To populate the vector database with textbook content:

```bash
# From the backend directory
cd backend
# Activate virtual environment
python scripts/ingest.py
```

This script will read all Markdown files from the `/docs` directory, chunk them, create embeddings using OpenAI, and store them in Qdrant.

## Key Features

### 1. RAG Chatbot
- Access the chat widget on any textbook page
- Ask questions about the content
- Get answers with citations to specific modules

### 2. User Authentication & Profiling
- Register with email and provide software/hardware background
- Login to access personalized features

### 3. Content Personalization
- Click "Personalize for Me" on any chapter
- Content will adapt based on your hardware profile (e.g., Jetson Kit vs. Cloud)

### 4. Content Localization
- Click "Translate to Urdu" on any chapter
- Content will be translated to Urdu in real-time

## API Endpoints

### Backend API (running on http://localhost:8000)
- `POST /api/chat` - RAG chatbot endpoint
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/personalize` - Content personalization
- `POST /api/translate` - Content translation

### Frontend (running on http://localhost:3000)
- `/` - Main textbook landing page
- `/intro` - Introduction module
- `/module-1` - ROS 2 module
- `/module-2` - Digital twin module
- `/module-3` - AI-Robot brain module
- `/module-4` - Vision-Language-Action module

## Testing the Application
```bash
# Backend tests
cd backend
# Activate virtual environment
pytest

# Frontend tests
cd frontend
npm test
```

## Deployment
For production deployment:

### Backend
- Deploy to a cloud platform that supports Python/FastAPI (e.g., Heroku, AWS, GCP)
- Ensure environment variables are properly configured
- Set up a production database

### Frontend
- Build the static site: `npm run build`
- Deploy to GitHub Pages or Vercel as specified in the hackathon requirements

## Troubleshooting
- If the RAG chatbot is not returning results, verify that content has been ingested into Qdrant
- If authentication is failing, check that Neon Postgres is accessible and the Better-Auth configuration is correct
- If translations are not working, verify that the OpenAI API key has the necessary permissions