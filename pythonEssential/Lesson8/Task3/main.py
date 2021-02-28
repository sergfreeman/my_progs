"""
Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы
он сохранял базу ссылок на диске и не «забывал» при перезапуске. При желании можете ознакомиться
с модулем shelve (https://docs.python.org/3/library/shelve.html), который в данном случае будет весьма
удобен и упростит выполнение задания.
"""

import shelve
FILENAME = 'links_base.dat'


def add_component():
    with shelve.open(FILENAME, 'c') as states:
        states[input('short name:')] = input('link:')
        states.close()


def find_component():
    key = (input('Enter the key: '))
    with shelve.open(FILENAME) as states:
        if key in states:
            print(states[key])
        else:
            print("Undefined KEY value")
    states.close()


def show_all():
    with shelve.open(FILENAME, 'c') as states:
        print("Short links is:")
        for short in states.keys():
            print(short, end=' ')
        states.close()


while True:
    print("""
            MENU
        1.  Add new link
        2.  Open link
        3.  Show links list

        0.  Exit
    """)
    choice = input('>>')

    if choice == '1':
        add_component()
    elif choice == '2':
        find_component()
    elif choice == '3':
        show_all()
    elif choice == '0':
        exit()