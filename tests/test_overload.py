from app.core.overload import detect_overload


def test_overload_hrv_only():
    reasons = detect_overload(False, 0, -0.18)
    assert "HRV ниже baseline > 15%" in reasons

def test_overload_sleep_and_training():
    reasons = detect_overload(True, 2, -0.05)
    assert "Недосып + нагрузка" in reasons

def test_no_overload():
    reasons = detect_overload(False, 1, -0.02)
    assert reasons == []
