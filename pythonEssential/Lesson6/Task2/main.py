"""
Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть
реализована возможность ввода изначальной ссылки и короткого названия и получения изначальной
ссылки по её названию.
"""
my_dict = \
    dict(help='https://stackoverflow.com/', lessons='www.edu.cbsystematics.com',
         film='https://www.youtube.com/', news='https://korrespondent.net/')


def add_component():
    my_dict.setdefault(input('short name:'), input('link:'))


def find_component():
    print(my_dict.get(input('Enter the key: ')))


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
        print(my_dict.keys())
    elif choice == '0':
        exit()
