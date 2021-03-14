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
    person = Account(param[0], param[1], (param[2]), (param[3]), (param[4]))
    while True:
        print(dictionary_of_visualisation['MENU_CLIENT'])
        menu_choice = input("Select number of operation: ")

        if menu_choice == '1':
            person.char_line('-', 65)
            money = input('PUT coins: ')
            person.put_coins_in_account(money)
            MySqlUtilities.update_person(param[0], param[1], (param[2]), int(person.client_balance), int(param[4]))

        elif menu_choice == '2':
            person.char_line('-', 65)
            money = input('GET coins: ')
            person.get_coins_in_account(money)
            MySqlUtilities.update_person(param[0], param[1], (param[2]), int(person.client_balance), int(param[4]))

        elif menu_choice == '3':
            person.char_line('-', 65)
            print(person)
            person.char_line('-', 65)

        elif menu_choice == '4':
            key = person.close_acc()

            if key == 'YES':
                MySqlUtilities.del_person_acc(param[0])
            else:
                continue

            main_menu()

        # Engineering function, hide realization, working only for debugging!
        elif menu_choice == '7':
            MySqlUtilities.show_all()
        # return to the MAIN menu
        elif menu_choice == '0':
            person.char_line('-', 65)
            exit()


def main_menu():
    """The main menu\n
    ----\n
    contained operation of our bank as:
                                1  Create a new account\n
                                2  Open a valid account\n
                                0  Exit

    """
    while True:
        Account.char_line('-', 65)
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
                iban = input(
                    f"""Enter the IBAN of the person 
you want to open: """)

                Account.char_line('-', 65)
                if MySqlUtilities.is_unique_iban(iban) is False:
                    break
                else:
                    print("""
                  This IBAN is non valid,
            enter any values to continue or 'E'
                        to exit:""", end='')
                    choice = input()
                    if choice == 'E' or choice == 'e':
                        main_menu()
            param = (MySqlUtilities.params_from_iban(iban))
            person = Account(param[0][0], param[0][1], param[0][2], param[0][3], param[0][4])
            attempt_counter = 3
            while attempt_counter >= 0:
                key = person.pass_valid(str(param[0][2]))
                if key is True:
                    print('PASSWORD IS CONFIRMED.')
                    person.char_line('-', 65)
                    print(person)
                    person.char_line('-', 65)
                    param = person.val_return()
                    client_menu(param)
                else:
                    print('PASSWORD COULD NOT CONFIRMED, TRY AGAIN.')
                    print(f'Left {attempt_counter} attempts.')
                    person.char_line('-', 65)
                    attempt_counter -= 1
        # Engineering function, hide realization, working only for debugging!
        elif menu_choice == '3':
            MySqlUtilities.show_all()
        # Exit
        elif menu_choice == '0':
            exit()


main_menu()

