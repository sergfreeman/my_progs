import sqlite3

conn = sqlite3.connect('orders2.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   name TEXT,
   age INT);
""")
conn.commit()

# user = [('Olga', 39),
#         ('Vika', 6),
#         ('Stasya', 6),
#         ('Bogdan', 4),
#         ('Luba', 66),
#         ('Serg', 40),
#         ('Andriy', 15),
#         ('Bogdan', 63),
#         ('Juliana', 30),
#         ('Vasya', 29),
#         ('Unknown People', 136)]
# cur.executemany("INSERT INTO users VALUES( ?, ?);", user)
# conn.commit()

# cur.execute("SELECT * FROM users;")
# one_result = cur.fetchone()
# print(one_result[1])


def add_new_pers():
    new_name = input("Enter name of the new person: ")
    new_age = int(input("Enter age of the new person: "))
    cur.execute(f"""INSERT INTO users(name, age) VALUES('{new_name}', {new_age});""")
    conn.commit()


def del_pers():
    choice = input('Enter the name of the person you want to delete:')
    cur.execute(f"DELETE FROM users WHERE name ='{choice}';")
    conn.commit()

    cur.execute(f"select * from users where name ='{choice}';")
    print(cur.fetchall())


def show_all():
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    print(all_results)


def show_name_list():
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    print(all_results)


def show_name():
    choice = input('Enter the name of the person you want view value :')
    cur.execute(f"SELECT * FROM users WHERE name = '{choice}';")
    one_result = cur.fetchone()
    print(one_result[1])

def main_menu():
    while True:
        print("""
                          SELECT OPTION
                          _________________
                          1. Add new person
                          2. Delete person
                          3. Show age from name
                          ...............
                          8. Show name list
                          9. Show all
                          0. Exit
                 
              """)
        choice = input(">>")
        if choice == '1':
            add_new_pers()
        elif choice == '2':
            del_pers()
        elif choice == '3':
            show_name()
        elif choice == '8':
            show_name_list()
        elif choice == '9':
            show_all()
        elif choice == '0':
            exit()

main_menu()