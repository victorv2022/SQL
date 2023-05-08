import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

db_file = 'database.db'
with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
print('Automatically closed the connection!')