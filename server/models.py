import sqlite3

def init_db():
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
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

def save_item(user_id, name, rarity, collected_at):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("INSERT INTO inventory (user_id, item_name, rarity, collected_at) VALUES (?, ?, ?, ?)",
                (user_id, name, rarity, collected_at))
    conn.commit()
    conn.close()

def get_inventory(user_id):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT item_name, rarity, collected_at FROM inventory WHERE user_id=?", (user_id,))
    results = cur.fetchall()
    conn.close()
    return results
