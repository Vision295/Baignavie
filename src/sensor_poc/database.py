import os
import sqlite3
from datetime import datetime

import pandas as pd

DB_NAME = "../../sensors.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS measurements (
                timestamp TEXT,
                spo2 REAL,
                heart_rate REAL,
                pressure REAL,
                accel_x REAL,
                accel_y REAL,
                accel_z REAL
            )
        """)

def delete_db():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print("Database deleted.")
    else:
        print("Database does not exist.")

def save_measurement(data):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            INSERT INTO measurements VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().isoformat(),
            data["spo2"],
            data["heart_rate"],
            data["pressure"],
            data["accel_x"],
            data["accel_y"],
            data["accel_z"]
        ))

def get_measurements():
    with sqlite3.connect(DB_NAME) as conn:
        return pd.read_sql_query(
            "SELECT * FROM measurements ORDER BY timestamp",
            conn,
            parse_dates=["timestamp"]
        )
