import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
for row in c.execute('SELECT country FROM countries WHERE area > 2000000'):
    print(row[0])
