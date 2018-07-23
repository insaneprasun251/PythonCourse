import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

# CREATE TABLE

c.execute('''CREATE TABLE IF NOT EXISTS main.stocks(date text, trans text, symbol text, quantity real, price real,
              name text)''')
# Altering table by adding column
# c.execute('''ALTER TABLE main.stocks ADD COLUMN name text''')
conn.commit()
# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2018-07-23', 'BUY', 'RHAT', 100, 35.14, 'Peter')")

# Save (commit) changes
conn.commit()
#
t = ("BUY",)
c.execute('SELECT * FROM stocks WHERE trans=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00, 'Mark'),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00, 'Thomas'),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00, 'Marie'),
#              ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?,?)', purchases)

conn.commit()

# c.execute('''DELETE FROM main.stocks''')
conn.commit()

for row in c.execute('SELECT * FROM stocks ORDER BY price DESC '):
    print(row)

# Close connection
conn.close()
