import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('test_db.sqlite')
db.row_factory = dict_factory
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
cursor.execute("INSERT INTO users (name, email) VALUES ('Tatyana', 'tatyana@yandex.ru')")

# cursor.executescript("""
# INSERT INTO users (name, email) VALUES ('John', 'dou@mail.com');
# INSERT INTO users (name, email) VALUES ('Nick', 'send@mail.com');
# """)

# users = [
#     ('user1', 'user1@gmail.com'),
#     ('user2', 'user2@gmail.com'),
#     ('user3', 'user3@gmail.com'),
# ]
# cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
# db.commit()

email = 'dou@mail.com'

# cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, 'Marina'))
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': email,
#                                                                             'name': 'Alex'})

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
print(results)

for user in results:
    print(user['name'], user['email'])


print(db.total_changes)

db.commit()

db.close()
