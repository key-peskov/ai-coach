from app.core import analyzer, baseline, overload
from app.db.repository import get_recent_hrv, save_day
from app.core.safety import hard_stop
from app.core.recommendations import RECOMMENDATIONS
from app.core.intensity_mapper import choose_level

def process_day(day):
    metrics = analyzer.analyze(day)
    history = get_recent_hrv()
    base = baseline.compute_baseline(history)
    dev = baseline.deviation(day.hrv_morning, base)

    reasons = overload.detect_overload(
        metrics["sleep_debt"], metrics["intensity_score"], dev
    )

    state = {
        "date": day.date,
        "hrv_morning": day.hrv_morning,
        "hrv_baseline": base,
        "hrv_deviation": dev,
        "sleep_debt": metrics["sleep_debt"],
        "intensity_score": metrics["intensity_score"],
        "overload": len(reasons) > 0,
        "overload_reasons": reasons
    }

    forced = hard_stop(state)
    training_type = forced or "climbing"
    level = choose_level(state)

    rec = RECOMMENDATIONS.get(training_type, RECOMMENDATIONS["recovery"])
    if isinstance(rec, dict) and level in rec:
        rec = rec[level]

    save_day(state)
    return {"state": state, "recommendation": rec}
