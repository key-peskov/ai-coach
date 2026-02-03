from app.core.analyzer import analyze

def test_analyzer_intensity_and_sleep(sample_day):
    metrics = analyze(sample_day)
    assert metrics["intensity_score"] == 2
    assert metrics["sleep_debt"] is True
