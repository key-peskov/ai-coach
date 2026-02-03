def hard_stop(state):
    if state["overload"]:
        return "recovery"
    if state["hrv_deviation"] is not None and state["hrv_deviation"] <= -0.25:
        return "recovery"
    return None
