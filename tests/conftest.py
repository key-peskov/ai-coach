import pytest
from datetime import date
from app.core.models import DayInput, Training

@pytest.fixture
def sample_day():
    return DayInput(
        date=date.today(),
        sleep_hours=6.0,
        hrv_morning=32,
        trainings=[
            Training(type="climbing", duration_min=60, intensity="medium")
        ],
    )
