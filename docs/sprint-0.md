# CampusEvents — Sprint 0: Project Initialization & Team Onboarding

**Sprint deadline: 08.11.2026**

## 1. Sprint goal

Initialize the project, configure development environments, establish the GitHub workflow, and onboard all team members.

This sprint focuses on setup and onboarding rather than complete application features.

## 2. Team members and tasks

### Sahib Aliyev — Team Leader

**Responsibilities:** Project coordination and repository management.

- [ ] Create and configure the GitHub repository.
- [ ] Create the initial project folder structure.
- [ ] Create and configure the GitHub Projects board.
- [ ] Define branch naming conventions and Pull Request workflow.
- [ ] Create initial GitHub Issues and assign tasks.
- [ ] Prepare the main README with project description and setup instructions.
- [ ] Ensure all team members have repository access.
- [ ] Coordinate onboarding and review initial Pull Requests.

**Deliverables:** Initialized repository, project board, initial documentation, and contribution guidelines.

### Said Gambarchayev — Frontend Developer

**Responsibilities:** Frontend initialization.

- [ ] Install and configure Next.js with TypeScript.
- [ ] Initialize the frontend project structure.
- [ ] Configure basic global CSS and application layout.
- [ ] Create a simple CampusEvents homepage placeholder.
- [ ] Verify that the application runs locally.
- [ ] Familiarize yourself with the Next.js project structure and conventions.

**Deliverables:** Working Next.js application, initial homepage, and basic frontend structure.

### Vagif Huseynli — Frontend Developer

**Responsibilities:** Frontend setup and UI preparation.

- [ ] Familiarize yourself with Next.js and TypeScript.
- [ ] Review the initial frontend structure created by Said.
- [ ] Prepare a basic reusable component structure.
- [ ] Create a simple navigation/header component.
- [ ] Suggest a basic UI design direction for CampusEvents.
- [ ] Verify that the components work with the main application.

**Deliverables:** Initial reusable components, navigation/header component, and proposed UI direction.

### Mykyta Kultenko — Backend / Full-Stack Developer

**Responsibilities:** Backend architecture and application integration.

- [ ] Review the overall application architecture.
- [ ] Familiarize yourself with FastAPI and the project technology stack.
- [ ] Review the initial backend structure.
- [ ] Define basic API endpoint conventions.
- [ ] Prepare the PostgreSQL integration structure using SQLAlchemy.
- [ ] Configure the initial database connection module.
- [ ] Coordinate with Ahmed on backend architecture and integration.
- [ ] Review how the frontend will communicate with the backend API.

**Deliverables:** Initial backend architecture, PostgreSQL integration setup, and basic API conventions.

### Ahmed Henni — Python Developer

**Responsibilities:** Python backend and analytics preparation.

- [ ] Initialize the Python project using FastAPI.
- [ ] Configure the initial backend folder structure.
- [ ] Create the main FastAPI application entry point.
- [ ] Implement a basic health-check endpoint (`GET /health`).
- [ ] Configure environment variable handling.
- [ ] Add initial backend dependencies and `requirements.txt`.
- [ ] Research Python libraries that may be useful for future event analytics.
- [ ] Prepare an initial analytics module structure.
- [ ] Verify that the API runs locally.

**Deliverables:** Working FastAPI application, health-check endpoint, initial analytics module structure, and backend dependencies.

### Adam Ibadov — Deployment & Cloud Engineer

**Responsibilities:** Containerization and infrastructure preparation.

- [ ] Install and configure Docker and Docker Compose.
- [ ] Prepare an initial Dockerfile for the frontend.
- [ ] Prepare an initial Dockerfile for the backend.
- [ ] Create a Docker Compose configuration.
- [ ] Configure PostgreSQL as a Docker service with persistent storage.
- [ ] Verify that the frontend, backend, and database containers can start.
- [ ] Research AWS EC2 deployment requirements for future sprints.
- [ ] Document basic instructions for running the application using Docker Compose.

**Deliverables:** Frontend and backend Dockerfiles, Docker Compose configuration, local containerized environment, and initial cloud deployment research.

## 3. GitHub workflow

All team members must follow this workflow:

1. Pull the latest changes from `main`.
2. Create a separate feature branch.
3. Implement the assigned task.
4. Commit changes using descriptive commit messages.
5. Push the branch to GitHub.
6. Open a Pull Request into `main`.
7. Wait for review and approval before merging.

### Branch naming examples

- `feature/frontend-initialization`
- `feature/navbar-component`
- `feature/backend-initialization`
- `feature/database-setup`
- `feature/docker-configuration`
- `docs/project-readme`

### Rules

- No direct commits to `main`.
- Every task should have an assigned GitHub Issue.
- Every Pull Request should reference its corresponding Issue.
- Keep Pull Requests small and focused.
- Never commit passwords, API keys, tokens, or real `.env` files.
- Update the README when setup instructions change.

## 4. Sprint completion criteria

By **08.11.2026**:

- [ ] GitHub repository is initialized and accessible to all members.
- [ ] GitHub Projects board is configured.
- [ ] All team members understand the Git workflow.
- [ ] Frontend application runs locally.
- [ ] Backend application runs locally.
- [ ] FastAPI health-check endpoint responds successfully.
- [ ] Initial PostgreSQL integration is prepared.
- [ ] Docker Compose configuration is available.
- [ ] Frontend and backend Dockerfiles are prepared.
- [ ] Initial README and setup instructions are documented.
- [ ] Every team member has submitted at least one contribution through GitHub.
- [ ] Initial Pull Requests have been reviewed and merged.

## 5. Expected outcome

At the end of Sprint 0, CampusEvents should have a working development foundation. The team should be able to run the frontend, backend, and database locally, collaborate through GitHub, and understand the responsibilities of each component.

The next sprint can focus on implementing the first application features, including database models, user authentication, and event management.

**Sprint 0 is complete when the team is ready to start developing the actual CampusEvents functionality.**
