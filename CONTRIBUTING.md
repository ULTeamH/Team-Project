# Contributing to CampusEvents

Welcome to the CampusEvents team. Please follow this workflow for every change.

## 1. Pick an issue

- Work on an issue assigned to you.
- Ask the team leader if the task or acceptance criteria are unclear.
- Move the issue to **In Progress** on the GitHub Projects board.

## 2. Create a branch

Start from the latest `main` branch:

```bash
git checkout main
git pull origin main
git checkout -b feature/short-description
```

Branch naming examples:

- `feature/frontend-initialization`
- `feature/navbar-component`
- `feature/backend-health-check`
- `feature/database-setup`
- `feature/docker-configuration`
- `docs/project-readme`

## 3. Commit and push

Use clear commit messages:

```bash
git add .
git commit -m "Add backend health check endpoint"
git push -u origin feature/your-branch-name
```

## 4. Open a Pull Request

- Open a Pull Request into `main`.
- Explain what changed and how it was tested.
- Link the related issue (for example, `Closes #12`).
- Request a review from the team leader or relevant teammate.
- Merge only after approval.

## Team rules

- Do not commit directly to `main`.
- Do not commit passwords, tokens, API keys, or real `.env` files.
- Keep Pull Requests focused and reasonably small.
- Update documentation when setup instructions change.
- Test your changes before requesting review.
