# API Contracts: AI-Powered Textbook with RAG

## Overview
This document defines the API contracts for the AI-powered textbook with RAG capabilities, authentication, personalization, and localization features.

## Authentication Endpoints

### POST /api/auth/register
Register a new user with profile information.

**Request:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "background_software": "Python",
  "background_hardware": "Jetson Kit",
  "password": "securePassword123"
}
```

**Response (200):**
```json
{
  "success": true,
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "message": "User registered successfully"
}
```

**Response (400):**
```json
{
  "error": "Invalid input data",
  "details": ["email", "background_hardware"]
}
```

### POST /api/auth/login
Authenticate a user and return session token.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200):**
```json
{
  "success": true,
  "session_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "name": "John Doe",
    "background_software": "Python",
    "background_hardware": "Jetson Kit"
  }
}
```

## RAG Chatbot Endpoints

### POST /api/chat
Process a user query and return a response based on textbook content using OpenRouter API (Xiaomi MiMo-V2-Flash).

**Request:**
```json
{
  "query": "How do I install ROS 2 on Ubuntu?",
  "selected_text": "Optional text that user has highlighted",
  "user_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Response (200):**
```json
{
  "answer": "To install ROS 2 on Ubuntu, first set up your locale, then add the ROS 2 apt repository, and finally install the desktop package...",
  "sources": ["/module-1/ros2", "/module-1/installation"],
  "confidence": 0.85
}
```

**Response (400):**
```json
{
  "error": "Query is required"
}
```

## Personalization Endpoints

### POST /api/personalize
Rewrite content based on user profile using OpenRouter API (Xiaomi MiMo-V2-Flash).

**Request:**
```json
{
  "page_content": "This section covers setting up your development environment. You can use a workstation or an edge computing device like the Jetson Nano...",
  "user_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Response (200):**
```json
{
  "personalized_content": "This section covers setting up your development environment. Since you have a Jetson Nano, we'll focus on setting it up for AI/robotics development..."
}
```

**Response (400):**
```json
{
  "error": "Both page_content and user_id are required"
}
```

## Localization Endpoints

### POST /api/translate
Translate content to the target language using OpenRouter API (Xiaomi MiMo-V2-Flash).

**Request:**
```json
{
  "text": "This section covers the fundamentals of robotic navigation.",
  "target_language": "ur"
}
```

**Response (200):**
```json
{
  "translated_text": "یہ سیکشن روبوٹک نیویگیشن کے بنیادیات پر مشتمل ہے۔"
}
```

**Response (400):**
```json
{
  "error": "Text and target_language are required"
}
```

## OpenRouter-Specific Endpoints

### POST /api/openrouter/test
Test the OpenRouter integration with Xiaomi MiMo-V2-Flash model.

**Request:**
```json
{
  "prompt": "Hello, how are you?",
  "model": "xiaomi/mimo-v2-flash:free"
}
```

**Response (200):**
```json
{
  "response": "I'm doing well, thank you for asking!",
  "model_used": "xiaomi/mimo-v2-flash:free",
  "tokens_used": 12
}
```

## Error Response Format
All error responses follow this format:

```json
{
  "error": "Descriptive error message",
  "code": "ERROR_CODE",
  "timestamp": "2025-12-30T10:00:00Z"
}
```

## Common Headers
- `Authorization: Bearer <session_token>` - Required for authenticated endpoints
- `Content-Type: application/json` - Required for request bodies
- `Accept: application/json` - Expected response format