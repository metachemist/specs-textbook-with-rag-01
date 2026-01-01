# Research Summary: AI-Powered Textbook with RAG

## Overview
This document summarizes the research conducted for implementing the AI-powered textbook with RAG capabilities, authentication, personalization, and localization features for Physical AI & Humanoid Robotics.

## Key Decisions & Rationale

### 1. Hybrid Static-Dynamic Architecture
- **Decision**: Use Docusaurus for static content delivery with React components for dynamic features
- **Rationale**: Docusaurus provides excellent SEO, fast loading, and is optimized for documentation. React components can be mounted inside Docusaurus to provide dynamic functionality like chat widgets and authentication modals.
- **Alternatives considered**: 
  - Full SPA (Next.js): Would sacrifice SEO and initial load performance
  - Static-only: Would not support dynamic personalization and chat features

### 2. Backend Technology Stack
- **Decision**: Use FastAPI for the backend API
- **Rationale**: FastAPI provides async support which is crucial for handling slow AI/LLM requests without blocking. It also offers automatic API documentation and strong typing with Pydantic.
- **Alternatives considered**:
  - Flask: Less performant for async operations
  - Node.js/Express: Would require different language expertise

### 3. Vector Database Selection
- **Decision**: Use Qdrant Cloud for vector storage
- **Rationale**: Required for the RAG chatbot functionality to store embeddings of the textbook content. Qdrant Cloud is specifically mentioned in the requirements.
- **Alternatives considered**: 
  - Pinecone: Alternative vector DB but Qdrant is specified in requirements
  - Weaviate: Alternative vector DB but Qdrant is specified in requirements

### 4. Authentication System
- **Decision**: Use Better-Auth for user authentication and profiling
- **Rationale**: Required for bonus points in the hackathon. Better-Auth handles complex user session logic and captures the required software/hardware background information.
- **Alternatives considered**:
  - Custom auth system: Would not qualify for bonus points
  - Other auth providers: Would not meet hackathon requirements

### 5. Database for User Profiles
- **Decision**: Use Neon Postgres for storing user profiles
- **Rationale**: Required for the hackathon. Neon provides serverless Postgres which is cost-effective and scales automatically.
- **Alternatives considered**:
  - Other databases: Would not meet hackathon requirements

### 6. Agentic Development Strategy
- **Decision**: Use Claude Code for generating boilerplate, content, and code
- **Rationale**: Required for 50 bonus points in the hackathon. Claude Code will be used for the architect, content, and coding agents.
- **Alternatives considered**:
  - Manual development: Would not qualify for bonus points

## Technical Implementation Details

### RAG Pipeline Architecture
1. **Ingestion**: Run an ingest script that reads Markdown files from `/docs`, chunks them, embeds them using OpenAI embeddings, and stores in Qdrant
2. **Query Processing**: When a user asks a question, the frontend sends it to the backend
3. **Retrieval**: The backend embeds the query and searches Qdrant for the top 3 relevant text chunks
4. **Generation**: The backend sends the context + query to OpenAI Chat Completion API
5. **Response**: The backend returns a concise answer citing specific modules from the textbook

### Personalization Pipeline
1. **User Profiling**: During signup, capture user's software and hardware background
2. **Content Adaptation**: When user clicks "Personalize for Me", frontend sends page content + user ID to backend
3. **Content Rewriting**: Backend retrieves user context and uses LLM to rewrite content appropriately (e.g., emphasizing "AWS Instance" for cloud users vs. "SD Card flashing" for Jetson users)

### Localization Pipeline
1. **Translation Request**: When user clicks "Translate to Urdu", frontend sends text to backend
2. **LLM Processing**: Backend uses LLM to translate content to Urdu
3. **Response**: Backend returns translated text with loading indicators for UX

## Security & Privacy Considerations
- User profile data will be stored securely in Neon Postgres
- API keys will be stored in environment variables, not in source code
- Authentication will be handled by Better-Auth with secure session management
- Content personalization will not expose other users' data

## Performance Considerations
- RAG chatbot responses targeted within 5 seconds
- Urdu translation targeted within 10 seconds
- Caching strategies for frequently accessed content
- Optimized embedding and retrieval processes

## Deployment Strategy
- Frontend: Deployed on GitHub Pages or Vercel
- Backend: Deployed on a cloud platform supporting Python/FastAPI
- Database: Neon Postgres (serverless)
- Vector DB: Qdrant Cloud