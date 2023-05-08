import sqlite3
import os

def check_db(filename):
    return os.path.exists(filename)

db_file = 'database.db'
schema_file = 'schema.sql'

if check_db(db_file):
    print('Database already exists. Exiting...')
    exit(0)

with open(schema_file, 'r') as rf:
    schema = rf.read

with sqlite3.connect(db_file) as conn:
    print('Created connection')
    conn.executescript(schema.sql)
    print('Created the Table! Now inserting')
    conn.executescript("""
                       insert into images (name, size, date)
                       values
                       ('sample.png', 100, '2019-10-10'),
                       ('ask_python.png', 450, '2019-05-02'),
                       ('class_room.jpeg', 1200, '2018-04-07'),
                       """)
    print('Inserted values into the table!')
print('Closed the connection!')