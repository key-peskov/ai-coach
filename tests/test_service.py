from app.core.service import process_day


def test_process_day_overload(sample_day, mocker):
    mocker.patch(
        "app.db.repository.get_recent_hrv",
        return_value=[40, 42, 41, 39, 38, 40, 41],
    )
    mocker.patch("app.db.repository.save_day")

    result = process_day(sample_day)
    state = result["state"]

    assert state.overload is True
    assert len(state.overload_reasons) > 0
