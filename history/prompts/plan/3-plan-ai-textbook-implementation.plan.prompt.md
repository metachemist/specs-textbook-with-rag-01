---
id: "3"
title: "Plan AI Textbook Implementation"
stage: "plan"
date: "2025-12-30"
surface: "agent"
model: "Qwen"
feature: "ai-textbook-rag"
branch: "001-ai-textbook-rag"
user: "user"
command: "/sp.plan"
labels: ["planning", "architecture", "ai", "textbook", "rag"]
links:
  spec: "specs/001-ai-textbook-rag/spec.md"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
 - "specs/001-ai-textbook-rag/plan.md"
 - "specs/001-ai-textbook-rag/research.md"
 - "specs/001-ai-textbook-rag/data-model.md"
 - "specs/001-ai-textbook-rag/quickstart.md"
 - "specs/001-ai-textbook-rag/contracts/api-contracts.md"
tests:
 - "none"
---

## Prompt

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType qwen`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

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


/sp.plan Phase 3: High-Level Plan1. System ArchitectureWe are building a Hybrid Static-Dynamic Application.Static Layer: The Docusaurus site provides SEO, fast loading, and the core textbook structure.Dynamic Layer: React components (<ChatWidget />, <AuthModal />) mounted inside Docusaurus talk to our Python backend for "smart" features.2. Tech Stack & Justification (Hackathon Alignment)ComponentTechnologyRole & JustificationFrontendDocusaurus (React)Required1. Optimized for documentation; easy to componentize.BackendFastAPI (Python)Required2. Async support is crucial for handling slow AI/LLM requests without blocking.Vector DBQdrant (Cloud)Required3. Stores embeddings of the book for the RAG chatbot.DatabaseNeon (Postgres)Required4. Serverless Postgres to store user profiles for Better-Auth.AuthBetter-AuthBonus Requirement5. Handles the complex user session logic.Dev ToolClaude CodeRequired6. We will use this CLI to generate the boilerplate and content.3. The "Agentic" Development Strategy (Bonus +50 Pts)The hackathon offers 50 points for using "Claude Code Subagents"7. Here is how we will structure our development workflow to claim this:The Architect Agent: We will task Claude to create the folder structure and configuration files.The Content Agent: We will feed the PDF syllabus to Claude and ask it to "act as a technical writer" to generate the Markdown files for Modules 1-4.The Coding Agent: We will ask Claude to write the FastAPI endpoints based on the pydantic models we define.4. Folder Structure (Monorepo)We will keep everything in one repo for easier submission, but cleanly separated.Plaintextphysical-ai-textbook/
├── README.md               # Submission Requirement (Video link, etc.)
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
    └── ingest.py           # Script to read /docs and upload to Qdrant5. Data Flow: The "Personalization" PipelineTo visualize how the Personalization Bonus 8 works, understanding the flow is critical:Ingestion: We run ingest.py. It reads all Markdown files in /docs -> chunks them -> embeds them -> stores in Qdrant.User Entry: Student signs up. We save {"hardware": "Jetson Nano"} in Neon.Viewing: Student opens "Module 3: AI-Robot Brain".Click: Student clicks "Personalize".Roundtrip:Frontend sends: Page Text + User Session.Backend retrieves Jetson Nano context.LLM Prompt: "Rewrite this text. The user has a Jetson Nano. Focus on memory constraints."Backend returns new text.Update: React updates the DOM with the personalized content.
```

## Response snapshot

The implementation planning for the AI-powered textbook with RAG capabilities has been successfully completed. The following was accomplished:

1. Setup script was run successfully, creating the plan template at specs/001-ai-textbook-rag/plan.md
2. Implementation plan was filled out with technical context, constitution check, and project structure
3. Phase 0 research completed with research.md documenting key decisions, rationale, and alternatives
4. Phase 1 design completed with:
   - Data model created (data-model.md) with entity definitions and API schemas
   - API contracts defined (contracts/api-contracts.md) with endpoint specifications
   - Quickstart guide created (quickstart.md) with setup and run instructions
5. Agent context updated using the update-agent-context.ps1 script
6. Constitution check re-evaluated and confirmed all principles are satisfied
7. All artifacts properly organized in the feature directory

The implementation plan is comprehensive and aligned with the project constitution, ready for the next phase (task breakdown).

## Outcome

- ✅ Impact: Created comprehensive implementation plan with research, data models, API contracts, and quickstart guide
- 🧪 Tests: No tests needed for this documentation update
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and contracts/api-contracts.md
- 🔁 Next prompts: Ready to proceed with task breakdown based on the implementation plan
- 🧠 Reflection: The plan thoroughly addresses all constitutional principles and provides a clear roadmap for implementation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for documentation update
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin task breakdown for the AI textbook implementation