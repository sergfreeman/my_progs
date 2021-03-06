import io

from banca_bank.account import Account
from banca_bank.ac_in_out import dictionary_of_visualisation


# import receiving_money
# from account import start_create_ac
# from receiving_money import mr


# from account import start_create_ac
def client_menu():
    """The clients menu\n
    ----\n
    contained operation:
                            get coins\n
                            put coins\n
                            close account\n
                            exit to the main menu\n

    """
    while True:
        print(dictionary_of_visualisation['M_CLIENT'])
        menu_choice = input("Select number of operation: ")

        if menu_choice == '1':
            # Create new account
            person = Account(Account.create_iban(), '', None, None, None)
            # person.(f'{Account.create_iban('0')}', {Account.create_name()},
            #                  {Account.create_password()}, {0}, {0})
            #
            # Account.create_name()
            # person.create_iban()
            # person.create_password()
            person.client_balance = 133
            print(person)
            person.char_line('-', 65)

        elif menu_choice == '2':
            f = open('bank_db.banka', 'r')
            x = f.readlines(1)
            print(x)

        elif menu_choice == '0':
            break


def main_menu():
    """The main menu\n
    ----\n
    contained operation of our bank as:
                                  Create a new account\n
                                  Open a valid account\n
                                  Exit

    """
    while True:
        print(dictionary_of_visualisation['MENU_MAIN'])
        menu_choice = input("Select number of operation: ")

        if menu_choice == '1':
            # Create new account

            person = Account(Account.create_iban(), Account.create_name(), Account.create_password(), 0, 0)
            print(person)
            person.char_line('-', 65)

        elif menu_choice == '2':
            # person = account.Account('', None, None, None, None)
            # person.client_acc_list = import_export.ImportExport.list_db_open()
            # print(person.client_acc_list)
            print()

        elif menu_choice == '0':
            exit()


main_menu()

# while True:
#         print('''
#             **********************************
#             *   Welcome to the "BANKA" bank  *
#             **********************************
#             *                                *
#             *    0.  Create a new account    *
#             *    1.  Open a valid account    *
#             *    2.  Receive coins           *
#             *    3.  Put coins               *
#             *    4.  Show balance            *
#             *    5.  Close your account      *
#             *                                *
#             *    9.  Exit                    *
#             *                                *
#             **********************************
#             ''')
#
#         menu_choice = input("Select number of operation: ")
#
#         if menu_choice == '0':
#             # Create new account
#
#             person = account.Account('', None, None, None, None)
#
#             person.create_name()
#             person.create_iban()
#             person.create_password()
#             person.client_balance = 133
#             print(person)
#             person.char_line('-', 65)
#
#         elif menu_choice == '1':
#             f = open('bank_db.banka', 'r')
#             x = f.readlines(1)
#             print(x)
#
#         elif menu_choice == '2':
#             person.receive_coins(input('Enter coins:'))
#
#         elif menu_choice == '3':
#             person.put_coins_in_account(input('Enter coins:'))
#         elif menu_choice == '4':
#             person.show_person_info()
#         elif menu_choice == '5':
#             pass
#         elif menu_choice == '9':
#             exit()
