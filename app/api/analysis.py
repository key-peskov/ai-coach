from fastapi import APIRouter
from app.db.repository import get_last_day

router = APIRouter()

@router.get("/last")
def last_day():
    return get_last_day()
