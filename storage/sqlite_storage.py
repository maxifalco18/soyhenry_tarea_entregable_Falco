import sqlite3

class SQLiteStorage:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self._crear_tabla()

    def _crear_tabla(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            tipo TEXT,
            sala TEXT,
            temperatura REAL,
            humedad REAL,
            co2 REAL
        )
        """)
        self.conn.commit()

    def guardar_log(self, log):
        self.conn.execute(
            "INSERT INTO logs (timestamp, tipo, sala, temperatura, humedad, co2) VALUES (?, ?, ?, ?, ?, ?)",
            (
                log["timestamp"],
                log["tipo"],
                log["sala"],
                log["temperatura"],
                log["humedad"],
                log["co2"]
            )
        )
        self.conn.commit()
