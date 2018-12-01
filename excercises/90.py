import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

rows = cur.execute("SELECT * FROM countries where area >= 2000000")

with open("area.csv", 'w') as file:
    for el in rows:
        file.writelines(str(el) + "\n")
