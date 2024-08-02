import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE 
)
''')

# cursor.execute("INSERT INTO users (name, email) VALUES ('Alex', 'test@mail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Peter', 'peter@mail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Ivan', 'ivan@mail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Marina', 'tatyana@mail.com')")

# cursor.executescript("""
# INSERT INTO users (name, email) VALUES ('John', 'dou@mail.com');
# INSERT INTO users (name, email) VALUES ('Nick', 'send@mail.com');
# """)

users = [
    ('user1', 'user1@gmail.com'),
    ('user2', 'user2@gmail.com'),
    ('user3', 'user3@gmail.com'),
]
cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
db.commit()

db.close()
