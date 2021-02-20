import account
# import receiving_money
from account import start_create_ac
# from receiving_money import mr


from account import start_create_ac


def main_menu():
    # person = Account('', None, None, None)
    while True:
        print('''
              Wellcome to the "BANKA" bank
            ********************************
            *                              *
            *    1.  Open a new account    *   
            *    2.  Receive coins         *
            *    3.  Put coins             *
            *    4.  Show balance          *
            *    5.  Close your account    *
            *                              *
            *    0.  Exit                  *
            *                              *
            ********************************
            ''')

        menu_choice = input("Select number of operation: ")
        if menu_choice == '1':

            start_create_ac()
            # account.person.show_person_info()
            # person = Account('', None, None, None)
            # exit()
            # person.show_person_info()
        elif menu_choice == '2':
            mr()
        elif menu_choice == '3':
            pass
        elif menu_choice == '4':
            pass
        elif menu_choice == '5':
            pass
        elif menu_choice == '0':
            exit()


main_menu()
