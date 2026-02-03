from fastapi import FastAPI

from app.api import analysis, checkin, explain
from app.db.db import init_db

app = FastAPI(title="AI Coach")

# --- init ---
init_db()

# --- routers ---
app.include_router(checkin.router, prefix="/checkin", tags=["checkin"])
app.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
app.include_router(explain.router, prefix="/recommendations", tags=["recommendations"])


@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}