# Physical AI Textbook with RAG Constitution

## Core Principles

### I. Agentic Development with Qwen CLI
All development work must leverage Qwen CLI for automated code generation, task execution, and project management. The development process should be driven by specifications and task breakdowns that Qwen CLI can execute.

### II. Decoupled Architecture
The system must follow a decoupled architecture with a Docusaurus-based frontend for static content delivery and a FastAPI backend for dynamic AI-powered features. This ensures scalability, maintainability, and independent deployment of components.

### III. Test-First (NON-NEGOTIABLE)
TDD is mandatory: Tests must be written before implementation, ensuring they fail initially. The Red-Green-Refactor cycle must be strictly enforced for all features and bug fixes.

### IV. AI-First Design
The system must be designed from the ground up to work with AI systems for querying, personalization, and dynamic adaptation. All AI processing should leverage OpenRouter API with appropriate models.

### V. Spec-Driven Development
All development must follow the Spec-Kit Plus methodology with clear specifications (spec.md), implementation plans (plan.md), and executable tasks (tasks.md). No development should proceed without proper specification.

### VI. TypeScript & Modern Tooling
All new frontend code must be written in TypeScript to ensure type safety and better developer experience. Tailwind CSS should be used for styling to maintain consistent UI components.

## Technology Stack Constraints

### Frontend Requirements
- **Framework**: Docusaurus for static site generation with React components
- **Language**: TypeScript (not JavaScript)
- **Styling**: Tailwind CSS (not Vanilla CSS)
- **Components**: React-based with proper type definitions

### Backend Requirements
- **Framework**: FastAPI for Python-based API development
- **Language**: Python 3.11+
- **Database**: Neon Postgres for relational data, Qdrant for vector storage
- **AI Services**: OpenRouter API integration with specified models

### Development Tooling
- **Primary Tool**: Qwen CLI for all development tasks and automation
- **Spec Management**: Spec-Kit Plus for specification-driven development
- **Version Control**: Git with proper branching and tagging strategies

## Development Workflow

### Specification Phase
- All features must begin with a detailed specification document (spec.md)
- User stories must be clearly defined with acceptance criteria
- Technical requirements and constraints must be documented upfront

### Planning Phase
- Implementation plans (plan.md) must align with specifications
- Architecture decisions must be documented and justified
- Tech stack choices must follow constitution guidelines

### Execution Phase
- Tasks must be broken down in tasks.md with clear dependencies
- Implementation must follow the defined phases (Setup → Foundational → User Stories → Polish)
- All completed tasks must be marked with [X] in the tasks file

## Governance

The constitution supersedes all other development practices. Any amendments must be documented with proper justification, approval, and migration plan. All pull requests and code reviews must verify compliance with constitutional principles.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
