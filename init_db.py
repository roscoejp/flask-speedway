import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO tags (epc, title, comment, original_register) VALUES (?, ?, ?, ?)", ('DEADBEEF12345678DEADBEEF', 'Test Tag', 'This is a sample tag.', 'init-script'))
cur.execute("INSERT INTO tags (epc, comment, original_register) VALUES (?, ?, ?)", ('FEEDBEEF12345678FEEDBEEF', 'This is a sample tag.', 'init-script'))

connection.commit()
connection.close()
