import sqlite3
from contextlib import contextmanager

DB_PATH = "coach.db"

@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS days (
            date TEXT PRIMARY KEY,
            sleep_hours REAL,
            hrv_morning INTEGER,
            hrv_baseline REAL,
            hrv_deviation REAL,
            sleep_debt INTEGER,
            intensity_score INTEGER,
            overload INTEGER,
            overload_reasons TEXT
        )
        """)
