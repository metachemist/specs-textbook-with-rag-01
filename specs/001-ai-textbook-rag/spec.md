# Feature Specification: AI-Powered Textbook with RAG

**Feature Branch**: `001-ai-textbook-rag`
**Created**: 2025-12-30
**Status**: Draft
**Input**: User description: "Project Update Directive: Refine Specs for OpenRouter Integration. Please update 'Phase 2: Specifications' to reflect the new AI provider: 1. RAG Chatbot Specifications: - Input/Process: The Backend must now send the context + query to the OpenRouter API (`https://openrouter.ai/api/v1`). - Model: Explicitly require the model ID `xiaomi/mimo-v2-flash:free`. - Embeddings: Specify that text chunks must be embedded using `FastEmbed` (local CPU inference) before searching Qdrant. 2. Personalization & Localization: - Update the mechanism to state that these prompts (rewriting text, translating to Urdu) will be processed by `xiaomi/mimo-v2-flash:free` via OpenRouter. 3. Env Variables: - Remove `OPENAI_API_KEY`. - Add `OPENROUTER_API_KEY`."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - RAG Chatbot with OpenRouter (Priority: P1)

As a learner studying Physical AI & Humanoid Robotics, I want to ask questions about the textbook content through an AI chatbot that now uses OpenRouter with the Xiaomi MiMo-V2-Flash model so that I can get immediate, contextual answers based on the book's content with improved cost efficiency.

**Why this priority**: This is the core value proposition of the AI-powered textbook and forms the base requirement for 100 points in the hackathon. Switching to OpenRouter with the free model ensures zero cost operation.

**Independent Test**: The chatbot widget appears on the Docusaurus site, accepts user questions, and returns answers citing specific modules from the textbook using the OpenRouter API with the Xiaomi MiMo-V2-Flash model.

**Acceptance Scenarios**:

1. **Given** I am viewing a textbook page, **When** I type a question in the chat widget and submit it, **Then** I receive a relevant answer citing specific modules from the textbook via OpenRouter API with Xiaomi MiMo-V2-Flash model.
2. **Given** I have selected specific text on a page, **When** I click "Ask AI" after highlighting text, **Then** the AI answers my question based only on the selected text using OpenRouter with Xiaomi MiMo-V2-Flash model.

---

### User Story 2 - Personalization with OpenRouter (Priority: P2)

As a learner with specific hardware (e.g., Jetson Kit vs. Cloud), I want the textbook content to adapt to my setup using OpenRouter's Xiaomi MiMo-V2-Flash model so that I see relevant instructions and examples for my configuration with zero cost processing.

**Why this priority**: This provides a significantly enhanced learning experience by tailoring content to the user's specific situation while maintaining zero operational costs.

**Independent Test**: When I click "Personalize for Me" on a chapter, the content rewrites to emphasize the technologies and setup relevant to my profile using OpenRouter with Xiaomi MiMo-V2-Flash model.

**Acceptance Scenarios**:

1. **Given** I have a "Cloud Only" profile, **When** I click "Personalize for Me" on a setup chapter, **Then** content emphasizes cloud-based solutions over hardware-specific instructions using OpenRouter with Xiaomi MiMo-V2-Flash model.
2. **Given** I have a "Jetson Kit" profile, **When** I click "Personalize for Me" on a setup chapter, **Then** content emphasizes hardware-specific instructions like flashing SD cards using OpenRouter with Xiaomi MiMo-V2-Flash model.

---

### User Story 3 - Localization with OpenRouter (Priority: P3)

As a learner who prefers Urdu, I want to translate textbook content to Urdu using OpenRouter's Xiaomi MiMo-V2-Flash model so that I can better understand the material in my native language with zero cost processing.

**Why this priority**: This is required for +50 bonus points in the hackathon and expands accessibility while maintaining zero operational costs.

**Independent Test**: When I click "Translate to Urdu" on a chapter, the content is translated to Urdu while maintaining technical accuracy using OpenRouter with Xiaomi MiMo-V2-Flash model.

**Acceptance Scenarios**:

1. **Given** I am viewing an English chapter, **When** I click "Translate to Urdu", **Then** the content is translated to Urdu with a loading indicator using OpenRouter with Xiaomi MiMo-V2-Flash model.
2. **Given** I have translated content displayed, **When** I click "Translate to Urdu" again, **Then** the original English content is restored.

---


---

### Edge Cases

- What happens when the OpenRouter API is temporarily unavailable?
- How does the system handle rate limiting from OpenRouter?
- What happens when the Xiaomi MiMo-V2-Flash model is unavailable?
- How does the system handle very long text selections for the "Ask AI" feature with the new embedding process?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a Docusaurus-based website hosting the Physical AI & Humanoid Robotics curriculum with 4 modules.
- **FR-002**: System MUST send context + query to the OpenRouter API at `https://openrouter.ai/api/v1` for RAG chatbot functionality.
- **FR-003**: System MUST explicitly use the model ID `xiaomi/mimo-v2-flash:free` for all AI processing including chat, personalization, and localization.
- **FR-004**: System MUST embed text chunks using `FastEmbed` (local CPU inference) before searching Qdrant for the RAG pipeline.
- **FR-005**: System MUST process personalization prompts (rewriting text) using `xiaomi/mimo-v2-flash:free` via OpenRouter.
- **FR-006**: System MUST process localization prompts (translating to Urdu) using `xiaomi/mimo-v2-flash:free` via OpenRouter.
- **FR-007**: System MUST remove the `OPENAI_API_KEY` environment variable requirement.
- **FR-008**: System MUST add the `OPENROUTER_API_KEY` environment variable requirement.
- **FR-009**: System MUST maintain all existing functionality while switching to the new AI provider.
- **FR-010**: System MUST ensure zero cost operation by using the free tier models from OpenRouter.

### Key Entities

- **User**: Represents a learner with profile information including software background (e.g., "Python", "C++", "Beginner") and hardware background (e.g., "Jetson Kit", "Cloud Only", "Simulation Only")
- **Textbook Content**: Represents the curriculum content organized in modules, chapters, and text chunks stored in vector format for RAG retrieval using FastEmbed for local CPU-based embeddings

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can ask questions through the RAG chatbot and receive relevant answers citing specific textbook modules within 5 seconds using OpenRouter with Xiaomi MiMo-V2-Flash model.
- **SC-002**: 100% of user signup flows capture both software and hardware background information.
- **SC-003**: Content personalization successfully adapts text to match user's hardware profile (e.g., emphasizing "AWS Instance" for cloud users vs. "SD Card flashing" for Jetson users) using OpenRouter with Xiaomi MiMo-V2-Flash model.
- **SC-004**: Urdu translation maintains technical accuracy and completes within 10 seconds for standard-length chapters using OpenRouter with Xiaomi MiMo-V2-Flash model.
- **SC-005**: System achieves a 300-point score in the Panaversity Hackathon by meeting all specified criteria with zero operational costs.
- **SC-006**: All AI processing (chat, personalization, localization) successfully uses OpenRouter API with Xiaomi MiMo-V2-Flash model.
- **SC-007**: Text embedding process successfully uses FastEmbed for local CPU-based embeddings before Qdrant search.
