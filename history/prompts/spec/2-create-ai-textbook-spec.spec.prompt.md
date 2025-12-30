---
id: "2"
title: "Create AI Textbook Spec"
stage: "spec"
date: "2025-12-30"
surface: "agent"
model: "Qwen"
feature: "ai-textbook-rag"
branch: "001-ai-textbook-rag"
user: "user"
command: "/sp.specify"
labels: ["specification", "ai", "textbook", "rag"]
links:
  spec: "specs/001-ai-textbook-rag/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
 - "specs/001-ai-textbook-rag/spec.md"
 - "specs/001-ai-textbook-rag/checklists/requirements.md"
tests:
 - "none"
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

The text the user typed after `/sp.specify` in the triggering message **is** the feature description. Assume you always have it available in this conversation even if `Phase 2: Specifications1. Data & Content SpecificationsBased on the syllabus provided in the hackathon document, the book must contain the following specific modules1:Book Structure (Docusaurus Sidebar):Introduction: Intro to Physical AI, Hardware Requirements (Workstation vs. Edge Kit)2222.Module 1: The Robotic Nervous System (ROS 2, Nodes, Topics, URDF)3.Module 2: The Digital Twin (Gazebo physics, Unity rendering, Sensors)4.Module 3: The AI-Robot Brain (NVIDIA Isaac Sim, Isaac ROS, Nav2)5.Module 4: Vision-Language-Action (OpenAI Whisper, LLM Cognitive Planning, Capstone Project)6.Database Schema (Neon Postgres):Table users:id: UUID (Primary Key)email: String (Unique)name: Stringbackground_software: Enum/String (e.g., "Python", "C++", "Beginner")7.background_hardware: Enum/String (e.g., "Jetson Kit", "Cloud Only", "Simulation Only")8.Vector Store (Qdrant):Collection: textbook_contentPayload: {"content": "chunk_text", "page_url": "/module-1/ros2", "chapter": "Module 1"}.2. Functional Specifications (The "Must-Haves")A. RAG Chatbot (Base Requirement)Trigger: A chat widget floating on the bottom right of the Docusaurus site.Input: User types a question (e.g., "How do I install ROS 2 on Ubuntu?").Process:Frontend sends query to FastAPI /api/chat.Backend embeds query (OpenAI Embeddings).Backend searches Qdrant for top 3 relevant text chunks9.Backend sends context + query to OpenAI Chat Completion.Output: Returns a concise answer citing the specific module.Constraint: Must support "answering questions based only on text selected by the user"10. Spec Update: The UI must allow highlighting text and clicking "Ask AI".B. Authentication & Profiling (Bonus +50)Provider: Better-Auth implemented in the FastAPI backend11.Flow:User clicks "Login/Signup".On Signup, a modal/form appears asking:"What is your programming experience?""Do you own a Jetson Kit or are you using Cloud?"12.Data is stored in Neon Postgres linked to the user session.C. Dynamic Personalization (Bonus +50)Trigger: A button "Personalize for Me" at the top of a chapter13.Logic:If User = "Cloud Only": The content about "Setting up Jetson" is hidden or rewritten to emphasize "Setting up AWS Instance"14.If User = "Jetson Owner": The content emphasizes "Flashing the SD Card"15.Mechanism: Frontend sends current page content + user ID to /api/personalize. LLM rewrites the intro/tutorials dynamically.D. Localization (Bonus +50)Trigger: A button "Translate to Urdu" at the top of a chapter16.Mechanism: Frontend sends text to /api/translate. LLM returns Urdu text.Latency: Must display a loading skeleton while translation occurs.3. Agentic Workflow Specification (Bonus +50)Tool: We must use Claude Code (CLI tool)17.Subagents: We will define a researcher subagent (to summarize the PDF syllabus) and a writer subagent (to convert summaries into Markdown).Evidence: We will commit the .clauderc or conversation logs as proof of agentic generation.4. Architecture DiagramTo help you visualize the data flow for the "Personalization" feature, here is a sequence diagram.5. API Endpoints Plan (FastAPI)MethodEndpointDescriptionPOST/api/auth/*Better-Auth routes (handled by library).POST/api/chatRAG endpoint. Receives {query, selected_text}.POST/api/personalizeReceives {page_content, user_id}. Returns rewritten text.POST/api/translateReceives {text, target_lang="ur"}. Returns translation.` appears literally below. Do not ask the user to repeat it unless they provided an empty command.

Given that feature description, do this:

1. **Generate a concise short name** (2-4 words) for the branch:
   - Analyze the feature description and extract the most meaningful keywords
   - Create a 2-4 word short name that captures the essence of the feature
   - Use action-noun format when possible (e.g., "add-user-auth", "fix-payment-bug")
   - Preserve technical terms and acronyms (OAuth2, API, JWT, etc.)
   - Keep it concise but descriptive enough to understand the feature at a glance
   - Examples:
     - "I want to add user authentication" → "user-auth"
     - "Implement OAuth2 integration for the API" → "oauth2-api-integration"
     - "Create a dashboard for analytics" → "analytics-dashboard"
     - "Fix payment processing timeout bug" → "fix-payment-timeout"

2. **Check for existing branches before creating new one**:

   a. First, fetch all remote branches to ensure we have the latest information:

      ```bash
      git fetch --all --prune
      ```

   b. Find the highest feature number across all sources for the short-name:
      - Remote branches: `git ls-remote --heads origin | grep -E 'refs/heads/[0-9]+-<short-name>$'`
      - Local branches: `git branch | grep -E '^[* ]*[0-9]+-<short-name>$'`
      - Specs directories: Check for directories matching `specs/[0-9]+-<short-name>`

   c. Determine the next available number:
      - Extract all numbers from all three sources
      - Find the highest number N
      - Use N+1 for the new branch number

   d. Run the script `.specify/scripts/powershell/create-new-feature.ps1 -Json "Phase 2: Specifications1. Data & Content SpecificationsBased on the syllabus provided in the hackathon document, the book must contain the following specific modules1:Book Structure (Docusaurus Sidebar):Introduction: Intro to Physical AI, Hardware Requirements (Workstation vs. Edge Kit)2222.Module 1: The Robotic Nervous System (ROS 2, Nodes, Topics, URDF)3.Module 2: The Digital Twin (Gazebo physics, Unity rendering, Sensors)4.Module 3: The AI-Robot Brain (NVIDIA Isaac Sim, Isaac ROS, Nav2)5.Module 4: Vision-Language-Action (OpenAI Whisper, LLM Cognitive Planning, Capstone Project)6.Database Schema (Neon Postgres):Table users:id: UUID (Primary Key)email: String (Unique)name: Stringbackground_software: Enum/String (e.g., "Python", "C++", "Beginner")7.background_hardware: Enum/String (e.g., "Jetson Kit", "Cloud Only", "Simulation Only")8.Vector Store (Qdrant):Collection: textbook_contentPayload: {"content": "chunk_text", "page_url": "/module-1/ros2", "chapter": "Module 1"}.2. Functional Specifications (The "Must-Haves")A. RAG Chatbot (Base Requirement)Trigger: A chat widget floating on the bottom right of the Docusaurus site.Input: User types a question (e.g., "How do I install ROS 2 on Ubuntu?").Process:Frontend sends query to FastAPI /api/chat.Backend embeds query (OpenAI Embeddings).Backend searches Qdrant for top 3 relevant text chunks9.Backend sends context + query to OpenAI Chat Completion.Output: Returns a concise answer citing the specific module.Constraint: Must support "answering questions based only on text selected by the user"10. Spec Update: The UI must allow highlighting text and clicking "Ask AI".B. Authentication & Profiling (Bonus +50)Provider: Better-Auth implemented in the FastAPI backend11.Flow:User clicks "Login/Signup".On Signup, a modal/form appears asking:"What is your programming experience?""Do you own a Jetson Kit or are you using Cloud?"12.Data is stored in Neon Postgres linked to the user session.C. Dynamic Personalization (Bonus +50)Trigger: A button "Personalize for Me" at the top of a chapter13.Logic:If User = "Cloud Only": The content about "Setting up Jetson" is hidden or rewritten to emphasize "Setting up AWS Instance"14.If User = "Jetson Owner": The content emphasizes "Flashing the SD Card"15.Mechanism: Frontend sends current page content + user ID to /api/personalize. LLM rewrites the intro/tutorials dynamically.D. Localization (Bonus +50)Trigger: A button "Translate to Urdu" at the top of a chapter16.Mechanism: Frontend sends text to /api/translate. LLM returns Urdu text.Latency: Must display a loading skeleton while translation occurs.3. Agentic Workflow Specification (Bonus +50)Tool: We must use Claude Code (CLI tool)17.Subagents: We will define a researcher subagent (to summarize the PDF syllabus) and a writer subagent (to convert summaries into Markdown).Evidence: We will commit the .clauderc or conversation logs as proof of agentic generation.4. Architecture DiagramTo help you visualize the data flow for the "Personalization" feature, here is a sequence diagram.5. API Endpoints Plan (FastAPI)MethodEndpointDescriptionPOST/api/auth/*Better-Auth routes (handled by library).POST/api/chatRAG endpoint. Receives {query, selected_text}.POST/api/personalizeReceives {page_content, user_id}. Returns rewritten text.POST/api/translateReceives {text, target_lang="ur"}. Returns translation."` with the calculated number and short-name:
      - Pass `--number N+1` and `--short-name "your-short-name"` along with the feature description
      - Bash example: `.specify/scripts/powershell/create-new-feature.ps1 -Json "Phase 2: Specifications1. Data & Content SpecificationsBased on the syllabus provided in the hackathon document, the book must contain the following specific modules1:Book Structure (Docusaurus Sidebar):Introduction: Intro to Physical AI, Hardware Requirements (Workstation vs. Edge Kit)2222.Module 1: The Robotic Nervous System (ROS 2, Nodes, Topics, URDF)3.Module 2: The Digital Twin (Gazebo physics, Unity rendering, Sensors)4.Module 3: The AI-Robot Brain (NVIDIA Isaac Sim, Isaac ROS, Nav2)5.Module 4: Vision-Language-Action (OpenAI Whisper, LLM Cognitive Planning, Capstone Project)6.Database Schema (Neon Postgres):Table users:id: UUID (Primary Key)email: String (Unique)name: Stringbackground_software: Enum/String (e.g., "Python", "C++", "Beginner")7.background_hardware: Enum/String (e.g., "Jetson Kit", "Cloud Only", "Simulation Only")8.Vector Store (Qdrant):Collection: textbook_contentPayload: {"content": "chunk_text", "page_url": "/module-1/ros2", "chapter": "Module 1"}.2. Functional Specifications (The "Must-Haves")A. RAG Chatbot (Base Requirement)Trigger: A chat widget floating on the bottom right of the Docusaurus site.Input: User types a question (e.g., "How do I install ROS 2 on Ubuntu?").Process:Frontend sends query to FastAPI /api/chat.Backend embeds query (OpenAI Embeddings).Backend searches Qdrant for top 3 relevant text chunks9.Backend sends context + query to OpenAI Chat Completion.Output: Returns a concise answer citing the specific module.Constraint: Must support "answering questions based only on text selected by the user"10. Spec Update: The UI must allow highlighting text and clicking "Ask AI".B. Authentication & Profiling (Bonus +50)Provider: Better-Auth implemented in the FastAPI backend11.Flow:User clicks "Login/Signup".On Signup, a modal/form appears asking:"What is your programming experience?""Do you own a Jetson Kit or are you using Cloud?"12.Data is stored in Neon Postgres linked to the user session.C. Dynamic Personalization (Bonus +50)Trigger: A button "Personalize for Me" at the top of a chapter13.Logic:If User = "Cloud Only": The content about "Setting up Jetson" is hidden or rewritten to emphasize "Setting up AWS Instance"14.If User = "Jetson Owner": The content emphasizes "Flashing the SD Card"15.Mechanism: Frontend sends current page content + user ID to /api/personalize. LLM rewrites the intro/tutorials dynamically.D. Localization (Bonus +50)Trigger: A button "Translate to Urdu" at the top of a chapter16.Mechanism: Frontend sends text to /api/translate. LLM returns Urdu text.Latency: Must display a loading skeleton while translation occurs.3. Agentic Workflow Specification (Bonus +50)Tool: We must use Claude Code (CLI tool)17.Subagents: We will define a researcher subagent (to summarize the PDF syllabus) and a writer subagent (to convert summaries into Markdown).Evidence: We will commit the .clauderc or conversation logs as proof of agentic generation.4. Architecture DiagramTo help you visualize the data flow for the "Personalization" feature, here is a sequence diagram.5. API Endpoints Plan (FastAPI)MethodEndpointDescriptionPOST/api/auth/*Better-Auth routes (handled by library).POST/api/chatRAG endpoint. Receives {query, selected_text}.POST/api/personalizeReceives {page_content, user_id}. Returns rewritten text.POST/api/translateReceives {text, target_lang="ur"}. Returns translation." --json --number 5 --short-name "user-auth" "Add user authentication"`
      - PowerShell example: `.specify/scripts/powershell/create-new-feature.ps1 -Json "Phase 2: Specifications1. Data & Content SpecificationsBased on the syllabus provided in the hackathon document, the book must contain the following specific modules1:Book Structure (Docusaurus Sidebar):Introduction: Intro to Physical AI, Hardware Requirements (Workstation vs. Edge Kit)2222.Module 1: The Robotic Nervous System (ROS 2, Nodes, Topics, URDF)3.Module 2: The Digital Twin (Gazebo physics, Unity rendering, Sensors)4.Module 3: The AI-Robot Brain (NVIDIA Isaac Sim, Isaac ROS, Nav2)5.Module 4: Vision-Language-Action (OpenAI Whisper, LLM Cognitive Planning, Capstone Project)6.Database Schema (Neon Postgres):Table users:id: UUID (Primary Key)email: String (Unique)name: Stringbackground_software: Enum/String (e.g., "Python", "C++", "Beginner")7.background_hardware: Enum/String (e.g., "Jetson Kit", "Cloud Only", "Simulation Only")8.Vector Store (Qdrant):Collection: textbook_contentPayload: {"content": "chunk_text", "page_url": "/module-1/ros2", "chapter": "Module 1"}.2. Functional Specifications (The "Must-Haves")A. RAG Chatbot (Base Requirement)Trigger: A chat widget floating on the bottom right of the Docusaurus site.Input: User types a question (e.g., "How do I install ROS 2 on Ubuntu?").Process:Frontend sends query to FastAPI /api/chat.Backend embeds query (OpenAI Embeddings).Backend searches Qdrant for top 3 relevant text chunks9.Backend sends context + query to OpenAI Chat Completion.Output: Returns a concise answer citing the specific module.Constraint: Must support "answering questions based only on text selected by the user"10. Spec Update: The UI must allow highlighting text and clicking "Ask AI".B. Authentication & Profiling (Bonus +50)Provider: Better-Auth implemented in the FastAPI backend11.Flow:User clicks "Login/Signup".On Signup, a modal/form appears asking:"What is your programming experience?""Do you own a Jetson Kit or are you using Cloud?"12.Data is stored in Neon Postgres linked to the user session.C. Dynamic Personalization (Bonus +50)Trigger: A button "Personalize for Me" at the top of a chapter13.Logic:If User = "Cloud Only": The content about "Setting up Jetson" is hidden or rewritten to emphasize "Setting up AWS Instance"14.If User = "Jetson Owner": The content emphasizes "Flashing the SD Card"15.Mechanism: Frontend sends current page content + user ID to /api/personalize. LLM rewrites the intro/tutorials dynamically.D. Localization (Bonus +50)Trigger: A button "Translate to Urdu" at the top of a chapter16.Mechanism: Frontend sends text to /api/translate. LLM returns Urdu text.Latency: Must display a loading skeleton while translation occurs.3. Agentic Workflow Specification (Bonus +50)Tool: We must use Claude Code (CLI tool)17.Subagents: We will define a researcher subagent (to summarize the PDF syllabus) and a writer subagent (to convert summaries into Markdown).Evidence: We will commit the .clauderc or conversation logs as proof of agentic generation.4. Architecture DiagramTo help you visualize the data flow for the "Personalization" feature, here is a sequence diagram.5. API Endpoints Plan (FastAPI)MethodEndpointDescriptionPOST/api/auth/*Better-Auth routes (handled by library).POST/api/chatRAG endpoint. Receives {query, selected_text}.POST/api/personalizeReceives {page_content, user_id}. Returns rewritten text.POST/api/translateReceives {text, target_lang="ur"}. Returns translation." -Json -Number 5 -ShortName "user-auth" "Add user authentication"`

   **IMPORTANT**:
   - Check all three sources (remote branches, local branches, specs directories) to find the highest number
   - Only match branches/directories with the exact short-name pattern
   - If no existing branches/directories found with this short-name, start with number 1
   - You must only ever run this script once per feature
   - The JSON is provided in the terminal as output - always refer to it to get the actual content you're looking for
   - The JSON output will contain BRANCH_NAME and SPEC_FILE paths
   - For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot")

3. Load `.specify/templates/spec-template.md` to understand required sections.

4. Follow this execution flow:

    1. Parse user description from Input
       If empty: ERROR "No feature description provided"
    2. Extract key concepts from description
       Identify: actors, actions, data, constraints
    3. For unclear aspects:
       - Make informed guesses based on context and industry standards
       - Only mark with [NEEDS CLARIFICATION: specific question] if:
         - The choice significantly impacts feature scope or user experience
         - Multiple reasonable interpretations exist with different implications
         - No reasonable default exists
       - **LIMIT: Maximum 3 [NEEDS CLARIFICATION] markers total**
       - Prioritize clarifications by impact: scope > security/privacy > user experience > technical details
    4. Fill User Scenarios & Testing section
       If no clear user flow: ERROR "Cannot determine user scenarios"
    5. Generate Functional Requirements
       Each requirement must be testable
       Use reasonable defaults for unspecified details (document assumptions in Assumptions section)
    6. Define Success Criteria
       Create measurable, technology-agnostic outcomes
       Include both quantitative metrics (time, performance, volume) and qualitative measures (user satisfaction, task completion)
       Each criterion must be verifiable without implementation details
    7. Identify Key Entities (if data involved)
    8. Return: SUCCESS (spec ready for planning)

5. Write the specification to SPEC_FILE using the template structure, replacing placeholders with concrete details derived from the feature description (arguments) while preserving section order and headings.

6. **Specification Quality Validation**: After writing the initial spec, validate it against quality criteria:

   a. **Create Spec Quality Checklist**: Generate a checklist file at `FEATURE_DIR/checklists/requirements.md` using the checklist template structure with these validation items:

      ```markdown
      # Specification Quality Checklist: [FEATURE NAME]
      
      **Purpose**: Validate specification completeness and quality before proceeding to planning
      **Created**: [DATE]
      **Feature**: [Link to spec.md]
      
      ## Content Quality
      
      - [ ] No implementation details (languages, frameworks, APIs)
      - [ ] Focused on user value and business needs
      - [ ] Written for non-technical stakeholders
      - [ ] All mandatory sections completed
      
      ## Requirement Completeness
      
      - [ ] No [NEEDS CLARIFICATION] markers remain
      - [ ] Requirements are testable and unambiguous
      - [ ] Success criteria are measurable
      - [ ] Success criteria are technology-agnostic (no implementation details)
      - [ ] All acceptance scenarios are defined
      - [ ] Edge cases are identified
      - [ ] Scope is clearly bounded
      - [ ] Dependencies and assumptions identified
      
      ## Feature Readiness
      
      - [ ] All functional requirements have clear acceptance criteria
      - [ ] User scenarios cover primary flows
      - [ ] Feature meets measurable outcomes defined in Success Criteria
      - [ ] No implementation details leak into specification
      
      ## Notes
      
      - Items marked incomplete require spec updates before `/sp.clarify` or `/sp.plan`
      ```

   b. **Run Validation Check**: Review the spec against each checklist item:
      - For each item, determine if it passes or fails
      - Document specific issues found (quote relevant spec sections)

   c. **Handle Validation Results**:

      - **If all items pass**: Mark checklist complete and proceed to step 6

      - **If items fail (excluding [NEEDS CLARIFICATION])**:
        1. List the failing items and specific issues
        2. Update the spec to address each issue
        3. Re-run validation until all items pass (max 3 iterations)
        4. If still failing after 3 iterations, document remaining issues in checklist notes and warn user

      - **If [NEEDS CLARIFICATION] markers remain**:
        1. Extract all [NEEDS CLARIFICATION: ...] markers from the spec
        2. **LIMIT CHECK**: If more than 3 markers exist, keep only the 3 most critical (by scope/security/UX impact) and make informed guesses for the rest
        3. For each clarification needed (max 3), present options to user in this format:

           ```markdown
           ## Question [N]: [Topic]
           
           **Context**: [Quote relevant spec section]
           
           **What we need to know**: [Specific question from NEEDS CLARIFICATION marker]
           
           **Suggested Answers**:
           
           | Option | Answer | Implications |
           |--------|--------|--------------|
           | A      | [First suggested answer] | [What this means for the feature] |
           | B      | [Second suggested answer] | [What this means for the feature] |
           | C      | [Third suggested answer] | [What this means for the feature] |
           | Custom | Provide your own answer | [Explain how to provide custom input] |
           
           **Your choice**: _[Wait for user response]_
           ```

        4. **CRITICAL - Table Formatting**: Ensure markdown tables are properly formatted:
           - Use consistent spacing with pipes aligned
           - Each cell should have spaces around content: `| Content |` not `|Content|`
           - Header separator must have at least 3 dashes: `|--------|`
           - Test that the table renders correctly in markdown preview
        5. Number questions sequentially (Q1, Q2, Q3 - max 3 total)
        6. Present all questions together before waiting for responses
        7. Wait for user to respond with their choices for all questions (e.g., "Q1: A, Q2: Custom - [details], Q3: B")
        8. Update the spec by replacing each [NEEDS CLARIFICATION] marker with the user's selected or provided answer
        9. Re-run validation after all clarifications are resolved

   d. **Update Checklist**: After each validation iteration, update the checklist file with current pass/fail status

7. Report completion with branch name, spec file path, checklist results, and readiness for the next phase (`/sp.clarify` or `/sp.plan`).

**NOTE:** The script creates and checks out the new branch and initializes the spec file before writing.

## General Guidelines

## Quick Guidelines

- Focus on **WHAT** users need and **WHY**.
- Avoid HOW to implement (no tech stack, APIs, code structure).
- Written for business stakeholders, not developers.
- DO NOT create any checklists that are embedded in the spec. That will be a separate command.

### Section Requirements

- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation

When creating this spec from a user prompt:

1. **Make informed guesses**: Use context, industry standards, and common patterns to fill gaps
2. **Document assumptions**: Record reasonable defaults in the Assumptions section
3. **Limit clarifications**: Maximum 3 [NEEDS CLARIFICATION] markers - use only for critical decisions that:
   - Significantly impact feature scope or user experience
   - Have multiple reasonable interpretations with different implications
   - Lack any reasonable default
4. **Prioritize clarifications**: scope > security/privacy > user experience > technical details
5. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
6. **Common areas needing clarification** (only if no reasonable default exists):
   - Feature scope and boundaries (include/exclude specific use cases)
   - User types and permissions (if multiple conflicting interpretations possible)
   - Security/compliance requirements (when legally/financially significant)

**Examples of reasonable defaults** (don't ask about these):

- Data retention: Industry-standard practices for the domain
- Performance targets: Standard web/mobile app expectations unless specified
- Error handling: User-friendly messages with appropriate fallbacks
- Authentication method: Standard session-based or OAuth2 for web apps
- Integration patterns: RESTful APIs unless specified otherwise

### Success Criteria Guidelines

Success criteria must be:

1. **Measurable**: Include specific metrics (time, percentage, count, rate)
2. **Technology-agnostic**: No mention of frameworks, languages, databases, or tools
3. **User-focused**: Describe outcomes from user/business perspective, not system internals
4. **Verifiable**: Can be tested/validated without knowing implementation details

**Good examples**:

- "Users can complete checkout in under 3 minutes"
- "System supports 10,000 concurrent users"
- "95% of searches return results in under 1 second"
- "Task completion rate improves by 40%"

**Bad examples** (implementation-focused):

- "API response time is under 200ms" (too technical, use "Users see results instantly")
- "Database can handle 1000 TPS" (implementation detail, use user-facing metric)
- "React components render efficiently" (framework-specific)
- "Redis cache hit rate above 80%" (technology-specific)

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

```text
Phase 2: Specifications1. Data & Content SpecificationsBased on the syllabus provided in the hackathon document, the book must contain the following specific modules1:Book Structure (Docusaurus Sidebar):Introduction: Intro to Physical AI, Hardware Requirements (Workstation vs. Edge Kit)2222.Module 1: The Robotic Nervous System (ROS 2, Nodes, Topics, URDF)3.Module 2: The Digital Twin (Gazebo physics, Unity rendering, Sensors)4.Module 3: The AI-Robot Brain (NVIDIA Isaac Sim, Isaac ROS, Nav2)5.Module 4: Vision-Language-Action (OpenAI Whisper, LLM Cognitive Planning, Capstone Project)6.Database Schema (Neon Postgres):Table users:id: UUID (Primary Key)email: String (Unique)name: Stringbackground_software: Enum/String (e.g., "Python", "C++", "Beginner")7.background_hardware: Enum/String (e.g., "Jetson Kit", "Cloud Only", "Simulation Only")8.Vector Store (Qdrant):Collection: textbook_contentPayload: {"content": "chunk_text", "page_url": "/module-1/ros2", "chapter": "Module 1"}.2. Functional Specifications (The "Must-Haves")A. RAG Chatbot (Base Requirement)Trigger: A chat widget floating on the bottom right of the Docusaurus site.Input: User types a question (e.g., "How do I install ROS 2 on Ubuntu?").Process:Frontend sends query to FastAPI /api/chat.Backend embeds query (OpenAI Embeddings).Backend searches Qdrant for top 3 relevant text chunks9.Backend sends context + query to OpenAI Chat Completion.Output: Returns a concise answer citing the specific module.Constraint: Must support "answering questions based only on text selected by the user"10. Spec Update: The UI must allow highlighting text and clicking "Ask AI".B. Authentication & Profiling (Bonus +50)Provider: Better-Auth implemented in the FastAPI backend11.Flow:User clicks "Login/Signup".On Signup, a modal/form appears asking:"What is your programming experience?""Do you own a Jetson Kit or are you using Cloud?"12.Data is stored in Neon Postgres linked to the user session.C. Dynamic Personalization (Bonus +50)Trigger: A button "Personalize for Me" at the top of a chapter13.Logic:If User = "Cloud Only": The content about "Setting up Jetson" is hidden or rewritten to emphasize "Setting up AWS Instance"14.If User = "Jetson Owner": The content emphasizes "Flashing the SD Card"15.Mechanism: Frontend sends current page content + user ID to /api/personalize. LLM rewrites the intro/tutorials dynamically.D. Localization (Bonus +50)Trigger: A button "Translate to Urdu" at the top of a chapter16.Mechanism: Frontend sends text to /api/translate. LLM returns Urdu text.Latency: Must display a loading skeleton while translation occurs.3. Agentic Workflow Specification (Bonus +50)Tool: We must use Claude Code (CLI tool)17.Subagents: We will define a researcher subagent (to summarize the PDF syllabus) and a writer subagent (to convert summaries into Markdown).Evidence: We will commit the .clauderc or conversation logs as proof of agentic generation.4. Architecture DiagramTo help you visualize the data flow for the "Personalization" feature, here is a sequence diagram.5. API Endpoints Plan (FastAPI)MethodEndpointDescriptionPOST/api/auth/*Better-Auth routes (handled by library).POST/api/chatRAG endpoint. Receives {query, selected_text}.POST/api/personalizeReceives {page_content, user_id}. Returns rewritten text.POST/api/translateReceives {text, target_lang="ur"}. Returns translation.
```

## Response snapshot

The specification for the AI-powered textbook with RAG capabilities has been successfully created. The following was accomplished:

1. Generated the branch name "ai-textbook-rag" based on the feature description
2. Created the branch "001-ai-textbook-rag" since no existing branches matched
3. Created a comprehensive specification document at specs/001-ai-textbook-rag/spec.md with:
   - Four prioritized user stories (RAG Chatbot, Authentication & Profiling, Content Personalization, Content Localization)
   - Functional requirements aligned with the hackathon criteria
   - Success criteria with measurable outcomes
   - Key entities identified
4. Created a specification quality checklist at specs/001-ai-textbook-rag/checklists/requirements.md
5. All checklist items have been validated and marked as complete

The specification is ready for the next phase (either /sp.clarify or /sp.plan).

## Outcome

- ✅ Impact: Created comprehensive feature specification for AI-powered textbook with RAG, authentication, personalization, and localization features
- 🧪 Tests: No tests needed for this documentation update
- 📁 Files: Created spec.md and requirements.md in the feature directory
- 🔁 Next prompts: Ready to proceed with feature planning based on the specification
- 🧠 Reflection: The specification captures all required hackathon features and is structured for implementation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for documentation update
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin technical planning for the AI textbook feature