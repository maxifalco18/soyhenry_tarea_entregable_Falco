import sqlite3

conn = sqlite3.connect("ecowatch.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM logs ")
for row in cursor.fetchall():
    print(row)

conn.close()
