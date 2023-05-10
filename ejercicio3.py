import sqlite3

db_file = 'database.db'

with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   select * from images
                   """)
    for row in cursor.fetchall():
        name, size, date = row
        print(f'{name} {size} {date}')