import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "db.sqlite3")


def init_db():
    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()

    # Create users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        name TEXT
    )
    """)

    # Create inventory table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        item_name TEXT,
        rarity TEXT,
        collected_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def get_user_by_name(name):
    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users WHERE name=?", (name,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None


def save_item(user_id, name, rarity, collected_at):
    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO inventory (user_id, item_name, rarity, collected_at)
        VALUES (?, ?, ?, ?)
    """, (user_id, name, rarity, collected_at))
    conn.commit()
    conn.close()

def get_inventory(user_id):
    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()
    cur.execute("""
        SELECT item_name, rarity, collected_at
        FROM inventory
        WHERE user_id=?
    """, (user_id,))
    results = cur.fetchall()
    conn.close()
    return results

def save_score(user_id, score):
    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        score INTEGER,
        created_at TEXT
    )
    """)
    cur.execute("INSERT INTO scores (user_id, score, created_at) VALUES (?, ?, datetime('now'))", (user_id, score))
    conn.commit()
    conn.close()

def get_top_scores(limit=10):
    conn = sqlite3.connect(DB_PATH)

    cur = conn.cursor()
    cur.execute("SELECT user_id, score, created_at FROM scores ORDER BY score DESC LIMIT ?", (limit,))
    results = cur.fetchall()
    conn.close()
    return results
