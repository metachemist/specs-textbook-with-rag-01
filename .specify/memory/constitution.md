<!--
Version change: 0.0.0 → 1.0.0
List of modified principles:
- [PRINCIPLE_1_NAME] → I. AI-Native Content Creation
- [PRINCIPLE_2_NAME] → II. Intelligent Querying (RAG Implementation)
- [PRINCIPLE_3_NAME] → III. Agentic Workflow Integration
- [PRINCIPLE_4_NAME] → IV. Identity & Profiling System
- [PRINCIPLE_5_NAME] → V. Dynamic Personalization Engine
- [PRINCIPLE_6_NAME] → VI. Localization & Accessibility
- [SECTION_2_NAME] → Technical Boundaries & Constraints
- [SECTION_3_NAME] → Success Criteria & Development Workflow

Added sections:
- Complete project-specific principles based on user input
- Technical boundaries and constraints section
- Success criteria and development workflow section

Removed sections:
- Template placeholder sections

Templates requiring updates:
- .specify/templates/plan-template.md ✅ reviewed - no changes needed
- .specify/templates/spec-template.md ✅ reviewed - no changes needed
- .specify/templates/tasks-template.md ✅ reviewed - no changes needed
- .specify/templates/adr-template.md ✅ reviewed - no changes needed
- .specify/templates/agent-file-template.md ✅ reviewed - no changes needed
- .specify/templates/checklist-template.md ✅ reviewed - no changes needed

No placeholders deferred - all template tokens have been replaced with project-specific content.
-->

# Physical AI & Humanoid Robotics Constitution

## Core Principles

### I. AI-Native Content Creation
All content must be engineered as an "AI-Native" technical textbook that transcends static reading. The project will leverage Agentic AI to create a personalized, interactive, and multi-lingual learning experience, adhering strictly to the Panaversity Hackathon guidelines. Content must be designed from the ground up to work with AI systems for querying, personalization, and dynamic adaptation.

### II. Intelligent Querying (RAG Implementation)
The system must implement a robust RAG (Retrieval-Augmented Generation) Chatbot using OpenAI Agents/ChatKit, FastAPI, Neon, and Qdrant. This bot must answer questions based specifically on the book's content and user-selected text. All querying functionality must be embedded directly in the Docusaurus-based website to provide seamless user experience.

### III. Agentic Workflow Integration
The project must demonstrate proof of using Claude Code Subagents and Agent Skills to generate or manage the book content. This includes leveraging AI agents for content creation, editing, and management processes. The agentic workflow must be clearly documented and demonstrated in the final deliverable.

### IV. Identity & Profiling System
A functional Sign-up/Sign-in system using Better-Auth must be implemented that captures the user's software/hardware background. This system must be secure, reliable, and capture relevant profile information that will be used for content personalization. User privacy and data protection must be prioritized.

### V. Dynamic Personalization Engine
The system must include a feature that rewrites/adjusts chapter content based on the user's profile. For example, highlighting "Edge Computing" for users with Jetson Kits vs. "Cloud" for AWS users. This personalization must be real-time and contextually appropriate to the user's technical background and preferences.

### VI. Localization & Accessibility
The project must include a real-time "Translate to Urdu" button for chapter content, demonstrating localization capabilities. The system should be architected to support additional languages in the future. All content must be accessible and culturally appropriate for diverse audiences.

## Technical Boundaries & Constraints

The project must use Claude Code and Spec-Kit Plus for the creation process. The frontend must be built with Docusaurus (React-based SSG). The backend/AI stack must include FastAPI (Python) for the API layer, Neon Serverless Postgres for relational data, Qdrant Cloud (Free Tier) for vector storage, and OpenAI Agents SDK/ChatKit for the RAG pipeline. Better-Auth is strictly required for authentication to qualify for bonus points.

## Success Criteria & Development Workflow

To secure a potential win and the maximum score (300 Points), the final deliverable must meet specific criteria including Content Authority (Docusaurus-based website with 4 Modules), Intelligent Querying (embedded RAG Chatbot), Agentic Workflow (Claude Code Subagents), Identity & Profiling (Better-Auth), Dynamic Personalization, Localization, and proper Deployment on GitHub Pages or Vercel with a public GitHub repository. All features must be fully functional and well-integrated.

## Governance

This constitution supersedes all other development practices for the Physical AI & Humanoid Robotics project. All amendments to these principles must be documented with clear justification and approval from project stakeholders. All pull requests and code reviews must verify compliance with these principles. The project must maintain alignment with Panaversity Hackathon guidelines throughout development. All development must follow the Spec-Driven Development (SDD) methodology as outlined in the project templates.

**Version**: 1.0.0 | **Ratified**: 2025-01-01 | **Last Amended**: 2025-12-30
