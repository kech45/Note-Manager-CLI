import sqlite3


class Storage:

    def __init__(self, db_path):
        self.__db_path = db_path
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                created_at VARCHAR(255) DEFAULT (datetime('now'))
            )
        """)
        conn.commit()
        conn.close()

    def add_note(self, title: str, content: str):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO notes(title, content) VALUES (?, ?)", (title, content)
        )
        conn.commit()
        conn.close()

    def get_all_notes(self):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_note_by_given_id(self, note_id: int):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def delete_note_by_given_id(self, note_id: int):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        conn.close()
