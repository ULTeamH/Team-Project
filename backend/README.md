# Backend

The backend uses Python and FastAPI.

## Local setup with Python

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install packages and start the API:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API: `http://localhost:8000`  
Health check: `http://localhost:8000/health`  
API documentation: `http://localhost:8000/docs`
