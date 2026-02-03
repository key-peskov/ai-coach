from fastapi import APIRouter

from app.agent.explainer import explain
from app.db.repository import get_last_day

router = APIRouter()

@router.get("/explain")
def explain_last():
    last = get_last_day()
    if not last:
        return {"detail": "No data"}

    explanation = explain(
        state=last,
        recommendation=last.get("recommendation", {})
    )
    return {"explanation": explanation}
