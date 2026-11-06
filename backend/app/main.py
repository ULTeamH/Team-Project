from fastapi import FastAPI

app = FastAPI(
    title="CampusEvents API",
    description="Backend API for the CampusEvents university event platform.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
