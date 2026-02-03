from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class Training(BaseModel):
    type: str
    duration_min: int
    intensity: str

class DayInput(BaseModel):
    date: date
    sleep_hours: float
    hrv_morning: int
    trainings: List[Training]

class DayState(BaseModel):
    date: date
    hrv_morning: int
    hrv_baseline: Optional[float]
    hrv_deviation: Optional[float]
    sleep_debt: bool
    intensity_score: int
    overload: bool
    overload_reasons: List[str]
