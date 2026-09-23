# init_db.py
# SmartCart Database Initialization Script

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "smartcart.db")
SCHEMA_FILE = os.path.join(BASE_DIR, "schema.sql")

def init_db():
    print(f"Initializing SmartCart SQLite database at: {DATABASE}")
    
    if not os.path.exists(SCHEMA_FILE):
        raise FileNotFoundError(f"Schema file not found at: {SCHEMA_FILE}")

    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.executescript(schema_sql)

    conn.commit()
    conn.close()
    print("SmartCart SQLite database initialized successfully!")

if __name__ == "__main__":
    init_db()
