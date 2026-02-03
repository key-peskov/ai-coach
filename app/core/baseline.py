def compute_baseline(values, window=7):
    if len(values) < window:
        return None
    recent = values[-window:]
    return sum(recent) / len(recent)

def deviation(today, baseline):
    if baseline is None:
        return None
    return (today - baseline) / baseline
