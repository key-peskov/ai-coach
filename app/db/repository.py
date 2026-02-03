import json

from app.db.db import get_conn


def save_day(state):
    with get_conn() as conn:
        conn.execute("""
        INSERT OR REPLACE INTO days
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            state.date.isoformat(),
            getattr(state, "sleep_hours", None),
            state.hrv_morning,
            state.hrv_baseline,
            state.hrv_deviation,
            int(state.sleep_debt),
            state.intensity_score,
            int(state.overload),
            json.dumps(state.overload_reasons),
        ))

def get_recent_hrv(limit=14):
    with get_conn() as conn:
        rows = conn.execute("""
        SELECT hrv_morning FROM days
        ORDER BY date ASC
        LIMIT ?
        """, (limit,)).fetchall()
    return [r["hrv_morning"] for r in rows if r["hrv_morning"]]

def get_last_day():
    with get_conn() as conn:
        row = conn.execute("""
        SELECT * FROM days
        ORDER BY date DESC
        LIMIT 1
        """).fetchone()
    return dict(row) if row else None
