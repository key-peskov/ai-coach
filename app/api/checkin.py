from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies import rate_limit_dep
from app.core.models import DayInput
from app.core.service import process_day

router = APIRouter()

@router.post("/day", dependencies=[Depends(rate_limit_dep)])
def checkin_day(day: DayInput):
    try:
        return process_day(day)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
