INTENSITY = {"low": 1, "medium": 2, "high": 3}

def analyze(day):
    intensity_score = max((INTENSITY[t.intensity] for t in day.trainings), default=0)
    return {
        "sleep_debt": day.sleep_hours < 7,
        "intensity_score": intensity_score
    }
