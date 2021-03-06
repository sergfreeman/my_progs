import random


class Account:
    def __init__(
            self,
            my_account_number,
            my_name,
            my_account_password,
            my_account_coins,
            my_time):

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
                __time_deal (type: Integer)
        """
        self.__name = my_name
        self.__IBAN = my_account_number
        self.__account_password = my_account_password

        self.__account_coins = my_account_coins
        self.__account_coins = 100
        self.__time_deal = my_time



    WELCOME = 'Welcome to the "BANKA" Bank!'
    client_acc_list = list()


    @classmethod
    def create_name(cls):

        """
            __name (type: String)
                Create name for new account from two parts (first name and last name).\n
                Both parts must have more than two and less than 50 alphabet sign.\n
                This name used by client logs.

        """
        print("\n\tCREATE NEW ACCOUNT")
        name = ''
        tmp_name = ''

        for part_of_name in ('first_name', 'last_name'):
            if part_of_name == 'first_name':
                part_name = 'First name'
            else:
                part_name = 'Last name'

            while True:
                try:
                    print(f'{part_name} name is:', end='')
                    tmp_name = input()

                    if tmp_name != " " and len(tmp_name) in range(2, 50):

                        if tmp_name.isalpha():
                            name += tmp_name
                            if part_name == 'Last name':
                                return name
                            else:
                                name = tmp_name.__add__(' ')
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
        return chr(random.randint(65, 91))

    @staticmethod
    def generate_number():
        """(type: String) Generate random number from 0 to 9"""
        return random.randint(0, 10)

    @classmethod
    def create_iban(cls):
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

        cls.__IBAN = f'{country_cod}{control_alpha}{bank_code}{five_zero}{account_number}'
        return cls.__IBAN

    @classmethod
    def create_password(cls):
        """
            __account_password (type: String)\n
            Create and confirm a new account password.\n
            Contains ten letters, special characters or numbers without a space.
        """
        while True:

            print('SET YOUR PASSWORD\t', end='')
            cls.__account_password = cls.enter_password()
            print('CONFIRM YOUR PASSWORD\t', end='')
            confirm_password = cls.enter_password()

            if cls.__account_password == confirm_password:

                print('PASSWORD IS CONFIRMED\t')
                cls.char_line('-', 65)
                print(f'''
 Well done. You are our new Client! {cls.WELCOME}
                ''')
                cls.char_line('-', 65)
                return confirm_password
            else:
                print('PASSWORD COULD NOT CONFIRMED, TRY AGAIN.')
            return confirm_password, cls

    def __repr__(self):
        """Create representation of main object values"""
        return f"""
        Private Client 
        information:
        
                        Client: {self.__name}
                          IBAN: {self.__IBAN}
                      password: {self.__account_password}
                         coins: {self.__account_coins}
                  time of deal: {self.__time_deal}
        """


    @staticmethod
    def enter_password():
        """Input password method"""

        while True:
            try:
                tmp_password = input('(ten letters, special characters or numbers without a space):')
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

    def receive_coins(self, val):
        """
            (type: String)
                Receive coins from account balance\n
                Call method-setter: client_balance
        """
        self.char_line('-', 65)
        try:
            val = int(val)
            if val <= self.client_balance:
                self.client_balance -= val
                print(f'Confirmed: you receive {val}')
            else:
                print("Canceled: you got no money.")

            print(f"Balance: {self.client_balance} coins")
            self.char_line('-', 65)
        except (TypeError, ValueError):
            print("Error, value should be integer")

    def put_coins_in_account(self, val):
        """
            (type: String)
                Put coins on account balance\n
                Call method-setter: client_balance
        """
        self.char_line('-', 65)
        try:
            val = int(val)
            if val > 0:
                self.client_balance += val
                print(f'Confirmed: you put {val} coins on your balance')
            else:
                print("Canceled: impossible operation.")
            print(f"Balance: {self.client_balance} coins")
            self.char_line('-', 65)
        except (TypeError, ValueError):
            print("Error, value should be integer")

    @staticmethod
    def pass_valid(valid_password):
        print("Please, enter your password", end='')
        enter_password = input()
        if valid_password == enter_password:
            return True
        else:
            return False

    @staticmethod
    def input_ac():
        tmp_iban = 'UA' + input('Enter your personal account (27 symbol): UA')
        if len(tmp_iban) == 29:
            return tmp_iban
        else:
            if len(tmp_iban) > 29:
                text = 'much'
            else:
                text = 'less'
            print(f'Invalid value of IBAN length, too{text} symbols')



