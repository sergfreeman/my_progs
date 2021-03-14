
from banca_bank.account import Account
from banca_bank.mysql_utilities import MySqlUtilities
from banca_bank.txt_dict import dictionary_of_visualisation


def client_menu(param):
    """The clients menu\n
    ----\n
    contained operation:
                         1   put coins\n
                         2   get coins\n
                         3   view profile
                         4   close account\n
                         0   exit to the main menu\n

    """
    person = Account(param[0], param[1], int(param[2]), int(param[3]), int(param[4]))
    while True:
        print(dictionary_of_visualisation['MENU_CLIENT'])
        menu_choice = input("Select number of operation: ")

        if menu_choice == '1':
            money = input('PUT coins: ')
            person.put_coins_in_account(money)
            MySqlUtilities.update_person(param[0], param[1], (param[2]), int(person.client_balance), int(param[4]))

            print(person)
            person.char_line('-', 65)

        elif menu_choice == '2':
            money = input('GET coins: ')
            person.get_coins_in_account(money)
            MySqlUtilities.update_person(param[0], param[1], (param[2]), int(person.client_balance), int(param[4]))
            print(person)
            person.char_line('-', 65)

        elif menu_choice == '3':
            person.char_line('-', 65)
            print(person)
            person.char_line('-', 65)

        elif menu_choice == '4':
            MySqlUtilities.del_person_acc(param[0])
            person.close_acc()
            break

        # Create new account
        # Engineering function, hide realization, working only for debugging!
        elif menu_choice == '7':
            MySqlUtilities.show_all()
        # return to the MAIN menu
        elif menu_choice == '0':
            person.char_line('-', 65)
            break


def main_menu():
    """The main menu\n
    ----\n
    contained operation of our bank as:
                                1  Create a new account\n
                                2  Open a valid account\n
                                0  Exit

    """
    while True:
        print(dictionary_of_visualisation['MENU_MAIN'])
        menu_choice = input("Select number of operation: ")

        # Create new account
        if menu_choice == '1':
            while True:
                iban = Account.create_iban()
                if MySqlUtilities.is_unique_iban(iban) is True:
                    break

            param = iban, Account.create_name(), Account.create_password(), 0, 0

            Account.char_line('-', 65)
            MySqlUtilities.update_person(param[0], param[1], param[2], param[3], param[4])
            client_menu(param)

        # Load valid account
        elif menu_choice == '2':
            while True:
                Account.char_line('-', 65)
                iban = input('Enter the IBAN of the person you want to open: ')
                if len(iban) == 29:
                    break
            param = (MySqlUtilities.show_from_iban(iban))

            # print('param0:',param[0][0])

            person = Account(param[0][0], param[0][1], param[0][2], param[0][3], param[0][4])
            person.char_line('-', 65)
            print(person)
            person.char_line('-', 65)
            MySqlUtilities.update_person(param[0], param[1], param[2], param[3], param[4])
            client_menu(param)

        # Create new account
        # Engineering function, hide realization, working only for debugging!
        elif menu_choice == '3':
            MySqlUtilities.show_all()

        # Exit
        elif menu_choice == '0':
            exit()


main_menu()
client_menu()