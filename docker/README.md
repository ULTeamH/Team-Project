# Docker

The root `docker-compose.yml` currently starts the FastAPI backend and PostgreSQL for local development.

The frontend Dockerfile and full-stack container setup can be added after the Next.js application has been initialized.

Start services from the repository root:

```bash
docker compose up --build
```

Stop services:

```bash
docker compose down
```

Stop services and remove the local database volume (this deletes local database data):

```bash
docker compose down -v
```
