import sqlite3
import sys

def list_users():
    conn = sqlite3.connect("db.sqlite3")
    for uid, name in conn.execute("SELECT user_id, name FROM users"):
        print(uid, name)
    conn.close()

def list_inventory(user_id):
    conn = sqlite3.connect("db.sqlite3")
    for name, rarity, when in conn.execute("SELECT item_name, rarity, collected_at FROM inventory WHERE user_id=?", (user_id,)):
        print(when, rarity, name)
    conn.close()

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "users":
        list_users()
    elif cmd == "inventory":
        list_inventory(sys.argv[2])
    else:
        print("Usage: users | inventory <user_id>")
