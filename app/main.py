from fastapi import FastAPI
from app.api import checkin, analysis

app = FastAPI(title="AI Coach")

app.include_router(checkin.router, prefix="/checkin")
app.include_router(analysis.router, prefix="/analysis")
