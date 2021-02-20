

import random


class Account:
    def __init__(self, my_name, my_account_number, my_account_password, my_account_coins):

        self.__name = my_name

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

        self.__IBAN = my_account_number

        def generate_alpha():
            return chr(random.randint(65, 90))

        def generate_number():
            return random.randint(0, 10)

        country_cod = 'UA'
        control_alpha = generate_alpha() + generate_alpha()
        bank_code = '390465'
        five_zero = '00000'
        account_number = ''
        for digit in range(13):
            account_number += str(generate_number())

        self.__IBAN = country_cod + control_alpha + bank_code + five_zero + account_number

        self.__account_coins = my_account_coins
        self.__account_coins = 100

        self.__account_password = my_account_password
        while True:
            print('Set your password')
            self.__account_password = self.enter_password()
            print('Confirm your password')
            confirm_password = self.enter_password()
            if self.__account_password == confirm_password:
                print('Password is confirmed\n')



                self.char_line('-', 65)

                print('''
 Well done. You are our new Client! Welcome to the "BANKA" Bank!
                ''')

                break
            else:
                print('Password could not confirmed, try again')

    def __repr__(self):

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
        return self.__account_coins

    @client_balance.setter
    def client_balance(self, val):
        self.__account_coins = val

    def show_person_info(self):
        Account.char_line('-', 65)
        print(self)
        Account.char_line('-', 65)


    @staticmethod
    def char_line(symbol, quantity):
        print(f'{symbol}' * quantity)


def start_create_ac():

    person = Account('', None, None, None)
    print(person)

def some():
    Account.show_person_info()

