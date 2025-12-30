# Data Model: AI-Powered Textbook with RAG

## Overview
This document defines the data models for the AI-powered textbook with RAG capabilities, authentication, personalization, and localization features for Physical AI & Humanoid Robotics.

## Entity Models

### User
Represents a learner with profile information.

**Fields:**
- `id`: UUID (Primary Key) - Unique identifier for the user
- `email`: String (Unique) - User's email address for authentication
- `name`: String - User's display name
- `background_software`: Enum/String (e.g., "Python", "C++", "Beginner") - User's software background
- `background_hardware`: Enum/String (e.g., "Jetson Kit", "Cloud Only", "Simulation Only") - User's hardware background
- `created_at`: DateTime - Timestamp when user account was created
- `updated_at`: DateTime - Timestamp when user profile was last updated

**Validation Rules:**
- Email must be valid and unique
- Background fields must be from predefined options
- Name cannot be empty

**Relationships:**
- One-to-many with UserSession (user can have multiple sessions)

### Textbook Content
Represents the curriculum content organized in modules, chapters, and text chunks stored in vector format for RAG retrieval.

**Fields:**
- `id`: UUID (Primary Key) - Unique identifier for the content chunk
- `content`: String - The actual text content chunk
- `page_url`: String - URL path to the page containing this content (e.g., "/module-1/ros2")
- `chapter`: String - The chapter/module this content belongs to (e.g., "Module 1")
- `embedding`: Vector - The vector embedding of the content for RAG retrieval
- `created_at`: DateTime - Timestamp when content was ingested
- `updated_at`: DateTime - Timestamp when content was last updated

**Validation Rules:**
- Content must not be empty
- Page URL must follow the format "/module-X/..."
- Chapter must be one of the defined modules (Intro, Module 1-4)

**Relationships:**
- None (standalone entity stored in vector database)

### User Session
Represents an active user session for authentication and tracking.

**Fields:**
- `id`: UUID (Primary Key) - Unique identifier for the session
- `user_id`: UUID (Foreign Key) - Reference to the associated user
- `session_token`: String - Secure session token
- `expires_at`: DateTime - Expiration timestamp for the session
- `created_at`: DateTime - Timestamp when session was created

**Validation Rules:**
- Session token must be cryptographically secure
- Expiration must be in the future
- User ID must reference an existing user

**Relationships:**
- Many-to-one with User (multiple sessions per user)

### Translation Cache
Optional entity to cache translations for performance.

**Fields:**
- `id`: UUID (Primary Key) - Unique identifier for the cached translation
- `original_content_id`: UUID - Reference to the original content chunk
- `target_language`: String - Target language code (e.g., "ur" for Urdu)
- `translated_content`: String - The translated content
- `created_at`: DateTime - Timestamp when translation was cached
- `expires_at`: DateTime - Expiration timestamp for the cached translation

**Validation Rules:**
- Original content ID must reference an existing content chunk
- Target language must be a valid language code
- Translated content must not be empty

**Relationships:**
- Many-to-one with Textbook Content (multiple cached translations per content chunk)

## State Transitions

### User Profile State
- **New User**: User has just signed up, profile information may be incomplete
- **Profile Complete**: User has provided both software and hardware background information
- **Profile Updated**: User has modified their profile information

### Content Personalization State
- **Original Content**: Content in its default state
- **Personalized**: Content has been adapted based on user profile
- **Cache Valid**: Personalized content is cached and can be served directly

## API Contract Models (Pydantic Schemas)

### User Registration Request
```python
class UserRegistrationRequest(BaseModel):
    email: EmailStr
    name: str
    background_software: str
    background_hardware: str
    password: str
```

### User Registration Response
```python
class UserRegistrationResponse(BaseModel):
    success: bool
    user_id: UUID
    message: str
```

### Chat Query Request
```python
class ChatQueryRequest(BaseModel):
    query: str
    selected_text: Optional[str] = None
    user_id: Optional[UUID] = None
```

### Chat Query Response
```python
class ChatQueryResponse(BaseModel):
    answer: str
    sources: List[str]  # List of module/chapter references
    confidence: float
```

### Personalization Request
```python
class PersonalizationRequest(BaseModel):
    page_content: str
    user_id: UUID
```

### Personalization Response
```python
class PersonalizationResponse(BaseModel):
    personalized_content: str
```

### Translation Request
```python
class TranslationRequest(BaseModel):
    text: str
    target_language: str = "ur"  # Default to Urdu
```

### Translation Response
```python
class TranslationResponse(BaseModel):
    translated_text: str
```