import sqlite3
from datetime import datetime

class DBProxy:
    def __init__(self, db_name="game_scores.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                time TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def insert_score(self, name, score, elapsed_time):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO scores (name, score, time, date) VALUES (?, ?, ?, ?)",
            (name, score, elapsed_time, date)
        )
        self.conn.commit()

    def get_top_scores(self, limit=10):
        self.cursor.execute(
            "SELECT name, score, time, date FROM scores ORDER BY score DESC LIMIT ?",
            (limit,)
        )
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

