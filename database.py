```python
import sqlite3
from datetime import datetime

DB_NAME = "war_game.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, balance INTEGER DEFAULT 0, created_at TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS countries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, owner_id INTEGER, power INTEGER DEFAULT 100, money INTEGER DEFAULT 1000, reserved INTEGER DEFAULT 0)")
    c.execute("CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, created_at TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS payments (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, country_id INTEGER, amount INTEGER, status TEXT DEFAULT 'pending', receipt_file_id TEXT, created_at TEXT)")
    conn.commit()
    conn.close()

def add_user(uid, uname, fname):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (user_id, username, first_name, created_at) VALUES (?, ?, ?, ?)", (uid, uname, fname, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_countries():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, name, reserved FROM countries")
    res = c.fetchall()
    conn.close()
    return res

def add_country(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO countries (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_random_news():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT text FROM news ORDER BY RANDOM() LIMIT 1")
    res = c.fetchone()
    conn.close()
    return res[0] if res else None

def add_news(text):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO news (text, created_at) VALUES (?, ?)", (text, datetime.now().isoformat()))
    conn.commit()
    conn.close()
```
