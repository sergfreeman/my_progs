import sqlite3

conn = sqlite3.connect('orders.db')


cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   ID INTEGER PRIMARY KEY AUTOINCREMENT,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

cur.execute("""INSERT INTO users( fname, lname, gender)
   VALUES('Alex', 'Smith', 'male');""")
conn.commit()

user = (None,'Lois', 'Lane', 'Female')

cur.execute("INSERT INTO users VALUES( ?, ?, ?, ?);", user)
conn.commit()

cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)

cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)

