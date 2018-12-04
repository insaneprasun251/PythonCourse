import sqlite3
import pandas

conn = sqlite3.connect('database.db')
cur = conn.cursor()

text = pandas.read_csv('ten-more-countries.txt')

for index, row in text.iterrows():
    # if "ID" in row:
    #     continue
    print(row)
    cur.execute("INSERT INTO countries values (NULL, ?,?, NULL)", (row["Country"], row['Area']))
conn.commit()
conn.close()
