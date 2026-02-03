def choose_level(state):
    if state["overload"]:
        return "low"
    if state["hrv_deviation"] is not None and state["hrv_deviation"] <= -0.15:
        return "low"
    return "medium"
