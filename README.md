# CampusEvents

**University Event Management Platform**

CampusEvents is a web application where students can discover upcoming university events, view event details, and register to participate. Organizers can create and manage events, set participant limits, and monitor registrations.

## Technology stack

- **Frontend:** Next.js + TypeScript
- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy (planned)
- **Containers:** Docker + Docker Compose
- **Version control and collaboration:** Git + GitHub
- **Cloud deployment:** AWS (planned)
- **UI design:** Figma

## Repository structure

```text
CampusEvents/
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│   └── README.md
├── docs/
│   ├── project-description.md
│   ├── architecture.md
│   └── sprint-0.md
├── docker/
│   └── README.md
├── frontend/
│   └── README.md
├── .gitignore
├── CONTRIBUTING.md
├── docker-compose.yml
└── README.md
```

## Getting started

### Prerequisites

- Git
- Python 3.11 or newer
- Docker Desktop or Docker Engine with Docker Compose
- Node.js LTS (for frontend development)

### Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd CampusEvents
```

### Configure environment variables

Before starting the application, create your local `.env` file from the provided example.

**Bash (Linux/macOS/Git Bash):**

```bash
cp .env.example .env
```

**PowerShell (Windows):**

```powershell
Copy-Item .env.example .env
```

The `.env.example` file contains development-only credentials and serves as a template for local configuration.

The `.env` file contains your local development configuration and must remain uncommitted. Never commit or push this file to GitHub. Only `.env.example` should be included in the repository.

Do not use development credentials in production.

### Run the initial backend and database

After creating your `.env` file, start the backend and database with:

```bash
docker compose up --build
```

The API will be available at `http://localhost:8000`.

- Health check: `http://localhost:8000/health`
- Interactive API documentation: `http://localhost:8000/docs`

PostgreSQL is available locally on port `5432`. Its development credentials are supplied through your local `.env` file.

### Frontend

The frontend folder is currently a placeholder. Initialize the Next.js application there:

```bash
npx create-next-app@latest frontend --typescript --eslint --app --src-dir
```

Follow the prompts, then run the frontend according to the generated Next.js README.

## Project documentation

- [Project description](docs/project-description.md)
- [Architecture](docs/architecture.md)
- [Sprint 0 tasks](docs/sprint-0.md)
- [Contribution guidelines](CONTRIBUTING.md)

## Project status

The repository currently contains the initial documentation and a minimal FastAPI health-check service. Application features will be implemented in subsequent sprints.