import sqlite3

conn = sqlite3.connect ('mydb.db')

c = conn.cursor()
for row in c.execute('SELECT * FROM student'):
    print(row)
conn.close()