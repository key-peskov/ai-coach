def detect_overload(sleep_debt, intensity_score, hrv_deviation):
    reasons = []
    if hrv_deviation is not None and hrv_deviation <= -0.15:
        reasons.append("HRV ниже baseline > 15%")
    if sleep_debt and intensity_score > 0:
        reasons.append("Недосып + нагрузка")
    return reasons
