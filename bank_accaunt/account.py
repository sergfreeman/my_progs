

import random


class Account:
    def __init__(self, my_name, my_account_number, my_account_password, my_account_coins):

        """
            Initial four class Account params
                __name (type: String)
                    Name of clients
                __IBAN (type: String)
                    Unique account number
                __account_password (type: String)
                    Unique password
                __account_coins  (type: Integer)
                    Balance
        """
        self.__name = my_name
        self.__IBAN = my_account_number
        self.__account_password = my_account_password

        self.__account_coins = my_account_coins
        self.__account_coins = 100

    WELCOME = 'Welcome to the "BANKA" Bank!'

    def create_name_new_account(self):

        """
            __name (type: String)
                Create name for new account from two parts (first name and last name).
                Both parts must have more than two and less than 50 alphabet sign.
                This name used by client logs.

        """
        print("\n\tCREATE NEW ACCOUNT")

        for part_of_name in ('first_name', 'last_name'):

            if part_of_name == 'first_name':
                tmp_name = 'First name'
            else:
                tmp_name = 'Last name'

            while True:
                try:

                    print(f'{tmp_name} name is:', end='')
                    tmp_name = input()
                    if tmp_name != " " and len(tmp_name) in range(2, 50):
                        if tmp_name.isalpha():
                            if self.__name != '':
                                self.__name += ' '
                            self.__name = self.__name + tmp_name
                            break
                        else:
                            print('Name must have only literals, pleas try again!')
                    else:
                        print('Name must have more than two literal, pleas try again!')
                        continue
                except ValueError:
                    print('Error value')
                    continue

    @staticmethod
    def generate_alpha():
        """(type: String) Generate random upper case literal from A to Z"""
        return chr(random.randint(65, 90))

    @staticmethod
    def generate_number():
        """(type: String) Generate random number from 0 to 9"""
        return random.randint(0, 10)

    def create_new_iban(self):
        """ Create new unique account value IBAN (International Bank Account Number)
            https://uk.wikipedia.org/wiki/International_Bank_Account_Number
        """
        country_cod = 'UA'
        control_alpha = f'{Account.generate_alpha()}{Account.generate_alpha()}'
        bank_code = '390465'
        five_zero = '00000'
        account_number = ''
        for digit in range(13):
            account_number += str(Account.generate_number())

        self.__IBAN = f'{country_cod}{control_alpha}{bank_code}{five_zero}{account_number}'

    def create_new_password(self):
        """
            __account_password (type: String)\n
            Create and confirm a new account password.\n
            Contains ten letters, special characters or numbers without a space.
        """
        while True:

            print('SET YOUR PASSWORD\t', end=' ')
            self.__account_password = self.enter_password()
            print('CONFIRM YOUR PASSWORD\t')
            confirm_password = self.enter_password()

            if self.__account_password == confirm_password:

                print('PASSWORD IS CONFIRMED\n')
                self.char_line('-', 65)
                print(f'''
 Well done. You are our new Client! {self.WELCOME}
                ''')
                self.char_line('-', 65)
                break
            else:
                print('PASSWORD COULD NOT CONFIRMED, TRY AGAIN.')

    def __repr__(self):
        """Create representation of main object values"""
        return f"""
        Private Client 
        information:
        
                        Client: {self.__name}
                          IBAN: {self.__IBAN}
                      password: {self.__account_password}
                         coins: {self.__account_coins}
        """


    @staticmethod
    def enter_password():
        """Input password method"""

        while True:
            try:
                tmp_password = input('Enter account password (10 literals, special signs or digits without space):')
                if len(tmp_password) == 1:
                    if not tmp_password.find(' '):
                        print("Error, password couldn't contain white space.")
                        continue
                    else:
                        break
                else:
                    print('Error, password length should be ten symbol.')
            except ValueError:
                print("Type error")
        return tmp_password

    @property
    def client_balance(self):
        """(type: String) Getter of client balance"""
        return self.__account_coins

    @client_balance.setter
    def client_balance(self, val):
        """(type: Setter) Setter of client balance"""
        self.__account_coins = val

    def show_person_info(self):
        """Show main account parameters"""
        Account.char_line('-', 65)
        print(self)
        Account.char_line('-', 65)


    @staticmethod
    def char_line(symbol, quantity):
        """Drawing symbol line"""
        print(f'{symbol}' * quantity)


def start_create_ac():
    """
    Create new account launcher.\n
    Show main params.
    """
    person = Account('', None, None, None)
    person.create_name_new_account()
    person.create_new_iban()
    person.create_new_password()
    person.client_balance = 1

    print(person)
    Account.char_line('-', 65)


