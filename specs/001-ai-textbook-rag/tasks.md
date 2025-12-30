# Tasks: AI-Powered Textbook with RAG

**Input**: Design documents from `/specs/001-ai-textbook-rag/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in physical-ai-textbook/
- [x] T002 [P] Initialize backend project with FastAPI dependencies in backend/requirements.txt
- [x] T003 [P] Initialize frontend project with Docusaurus dependencies in frontend/package.json
- [x] T004 Create .env.example file in backend/ with API key placeholders
- [x] T005 Create README.md with project overview and setup instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T006 Setup database schema and migrations framework for Neon Postgres
- [ ] T007 [P] Implement Better-Auth authentication framework in backend/
- [ ] T008 [P] Setup API routing and middleware structure in backend/app/main.py
- [ ] T009 Create User model in backend/app/models/user.py based on data-model.md
- [ ] T010 Configure error handling and logging infrastructure in backend/app/core/
- [ ] T011 Setup environment configuration management in backend/app/core/config.py
- [ ] T012 Create basic Docusaurus configuration in frontend/docusaurus.config.js
- [ ] T013 Setup Qdrant client connection in backend/app/core/qdrant_client.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - RAG Chatbot Interaction (Priority: P1) 🎯 MVP

**Goal**: Implement the core RAG chatbot functionality that allows users to ask questions about textbook content and receive answers citing specific modules.

**Independent Test**: The chatbot widget appears on the Docusaurus site, accepts user questions, and returns answers citing specific modules from the textbook.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T014 [P] [US1] Contract test for POST /api/chat in backend/tests/contract/test_chat.py
- [ ] T015 [P] [US1] Integration test for RAG pipeline in backend/tests/integration/test_rag_pipeline.py

### Implementation for User Story 1

- [ ] T016 [P] [US1] Create TextbookContent model in backend/app/models/textbook_content.py
- [ ] T017 [P] [US1] Create ChatQueryRequest and ChatQueryResponse schemas in backend/app/models/schemas.py
- [ ] T018 [US1] Implement RAG service in backend/app/services/rag_service.py (handles embedding, retrieval, generation)
- [ ] T019 [US1] Implement POST /api/chat endpoint in backend/app/api/chat.py
- [ ] T020 [US1] Create ingestion script scripts/ingest.py to read MDX files and store embeddings in Qdrant
- [ ] T021 [US1] Add validation and error handling for chat queries
- [ ] T022 [US1] Create ChatWidget React component in frontend/src/components/ChatWidget.js
- [ ] T023 [US1] Integrate ChatWidget with Docusaurus pages
- [ ] T024 [US1] Implement text selection and "Ask AI" functionality in frontend

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - User Authentication & Profiling (Priority: P2)

**Goal**: Implement user registration and login with capture of software/hardware background information.

**Independent Test**: A user can sign up with email, provide programming experience and hardware background, and have this information stored in their profile.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US2] Contract test for POST /api/auth/register in backend/tests/contract/test_auth.py
- [ ] T026 [P] [US2] Integration test for user registration flow in backend/tests/integration/test_auth_flow.py

### Implementation for User Story 2

- [ ] T027 [P] [US2] Create UserSession model in backend/app/models/user_session.py
- [ ] T028 [US2] Implement POST /api/auth/register endpoint in backend/app/api/auth.py
- [ ] T029 [US2] Implement POST /api/auth/login endpoint in backend/app/api/auth.py
- [ ] T030 [US2] Add database schema for users table with background_software and background_hardware fields
- [ ] T031 [US2] Create authentication middleware in backend/app/middleware/auth_middleware.py
- [ ] T032 [US2] Add signup form component in frontend/src/components/AuthModal.js
- [ ] T033 [US2] Add login button to Docusaurus navbar

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Content Personalization (Priority: P3)

**Goal**: Implement content personalization that adapts textbook content based on user's hardware profile.

**Independent Test**: When a user clicks "Personalize for Me" on a chapter, the content rewrites to emphasize technologies and setup relevant to their profile.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T034 [P] [US3] Contract test for POST /api/personalize in backend/tests/contract/test_personalize.py
- [ ] T035 [P] [US3] Integration test for personalization flow in backend/tests/integration/test_personalization.py

### Implementation for User Story 3

- [ ] T036 [P] [US3] Create PersonalizationRequest and PersonalizationResponse schemas in backend/app/models/schemas.py
- [ ] T037 [US3] Implement POST /api/personalize endpoint in backend/app/api/personalize.py
- [ ] T038 [US3] Implement personalization service in backend/app/services/personalization_service.py
- [ ] T039 [US3] Add "Personalize for Me" button component in frontend/src/components/PersonalizeButton.js
- [ ] T040 [US3] Connect personalization button to backend API
- [ ] T041 [US3] Implement caching for personalized content if needed

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Content Localization (Priority: P4)

**Goal**: Implement Urdu translation functionality for textbook content.

**Independent Test**: When a user clicks "Translate to Urdu" on a chapter, the content is translated to Urdu while maintaining technical accuracy.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T042 [P] [US4] Contract test for POST /api/translate in backend/tests/contract/test_translate.py
- [ ] T043 [P] [US4] Integration test for translation flow in backend/tests/integration/test_translation.py

### Implementation for User Story 4

- [ ] T044 [P] [US4] Create TranslationRequest and TranslationResponse schemas in backend/app/models/schemas.py
- [ ] T045 [US4] Create TranslationCache model in backend/app/models/translation_cache.py
- [ ] T046 [US4] Implement POST /api/translate endpoint in backend/app/api/translate.py
- [ ] T047 [US4] Implement translation service in backend/app/services/translation_service.py
- [ ] T048 [US4] Add "Translate to Urdu" button component in frontend/src/components/TranslateButton.js
- [ ] T049 [US4] Connect translation button to backend API with loading indicators

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T050 [P] Documentation updates in docs/
- [ ] T051 Code cleanup and refactoring
- [ ] T052 Performance optimization across all stories
- [ ] T053 [P] Additional unit tests (if requested) in backend/tests/unit/
- [ ] T054 Security hardening
- [ ] T055 Run quickstart.md validation
- [ ] T056 Create .clauderc file to demonstrate agentic workflow
- [ ] T057 Deploy frontend to Vercel
- [ ] T058 Deploy backend to cloud platform
- [ ] T059 Update README.md with deployment links and tech stack

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Depends on US2 (needs user profiles) and US1 (content exists)
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for POST /api/chat in backend/tests/contract/test_chat.py"
Task: "Integration test for RAG pipeline in backend/tests/integration/test_rag_pipeline.py"

# Launch all models for User Story 1 together:
Task: "Create TextbookContent model in backend/app/models/textbook_content.py"
Task: "Create ChatQueryRequest and ChatQueryResponse schemas in backend/app/models/schemas.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence