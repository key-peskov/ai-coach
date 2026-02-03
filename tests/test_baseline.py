from app.core.baseline import compute_baseline, deviation


def test_baseline_not_enough_data():
    assert compute_baseline([30, 31, 32]) is None

def test_baseline_ok():
    values = [40, 42, 41, 39, 38, 40, 41]
    assert compute_baseline(values) == sum(values) / len(values)

def test_deviation_negative():
    baseline = 40
    today = 32
    dev = deviation(today, baseline)
    assert round(dev, 2) == -0.20
