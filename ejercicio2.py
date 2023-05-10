import sqlite3
import os

def check_db(filename):
    return os.path.exists(filename)

db_file = 'database.db'
schema_file = 'schema.sql'
insert_file = 'insert_images.sql'

if check_db(db_file):
    print('Database already exists.')
else:
    print('Database does not exists.')

with open(schema_file, 'r') as rf:
    schema = rf.read()

print(schema)

with open(insert_file, 'r') as cursor:
    insert = cursor.read()


with sqlite3.connect(db_file) as conn:
    print('Created connection')
    conn.executescript(schema)
    print('Created the Table! Now inserting')
    conn.executescript(insert)
    print('Inserted values into the table!')
print('Closed the connection!')