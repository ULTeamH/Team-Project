# CampusEvents — Initial Architecture

## 1. Architecture overview

CampusEvents will use a frontend application, a Python API, and a relational database.

```text
Students / Organizers
        |
        v
Next.js + TypeScript
        |
        v
FastAPI (Python)
        |
        v
PostgreSQL
```

The frontend communicates with the FastAPI backend over HTTP. The backend handles application logic and database access. Python will also be used for future event analytics.

## 2. Technology responsibilities

| Component | Technology | Responsibility |
|---|---|---|
| Frontend | Next.js + TypeScript | User interface and client-side interactions |
| Backend API | Python + FastAPI | API endpoints and application logic |
| Database | PostgreSQL | Users, events, registrations and attendance |
| ORM | SQLAlchemy (planned) | Database access and models |
| Containers | Docker / Docker Compose | Consistent local development environment |
| Version control | Git / GitHub | Source code and team collaboration |
| CI/CD | GitHub Actions (planned) | Automated checks and deployment |
| Cloud | AWS (planned) | Hosting the application |
| UI design | Figma | Wireframes and interface design |

## 3. Initial deployment approach

The initial cloud deployment is planned for AWS. A possible first deployment is one Ubuntu EC2 instance running the application containers with Docker Compose and an Nginx reverse proxy.

For the initial development stage, the team will run the backend and PostgreSQL locally using Docker Compose. The frontend will be initialized separately with Next.js.

## 4. Architecture decisions to confirm

The team should confirm these decisions before implementing production features:

- API URL and route conventions.
- Database schema and migration approach.
- Authentication approach.
- File and image storage requirements.
- Whether PostgreSQL will remain containerized in the first cloud deployment or move to a managed database.
- CI/CD workflow and deployment permissions.

## 5. Security notes

- Never commit real credentials or `.env` files.
- Use environment variables for secrets and configuration.
- Do not expose PostgreSQL publicly.
- Use HTTPS for public deployments.
- Use restricted permissions for cloud resources.
