import sqlite3
from acc_utilities import Utilities
import txt_dict


class Account(Utilities):
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
                    Password
                __account_coins  (type: Integer)
                    Balance
                __time_deal (type: Integer)
        """
        self.__name = my_name
        self.__IBAN = my_account_number
        self.__account_password = my_account_password
        self.__account_coins = my_account_coins
        self.__time_deal = my_time

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
 Well done. You are our new Client! {txt_dict.dictionary_of_visualisation.get('WELCOME')}
                ''')
                cls.char_line('-', 65)
                return confirm_password
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
                  time of deal: {self.__time_deal}
        """

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
            self.char_line('-', 65)

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
            self.char_line('-', 65)

    def get_coins_in_account(self, val):
        """
            (type: String)
                Get coins on account balance\n
                Call method-setter: client_balance
        """
        self.char_line('-', 65)
        try:
            val = int(val)
            if self.client_balance >= val > 0:
                self.client_balance -= val
                print(f'Confirmed: you get {val} coins from your balance')
            else:
                print("Canceled: impossible operation.")
            print(f"Balance: {self.client_balance} coins")
            self.char_line('-', 65)
        except (ValueError, TypeError, ):
            print("Error, value should be integer")
            self.char_line('-', 65)

    def val_return(self):
        iban = str(self.__IBAN)
        name = str(self.__name)
        password = str(self.__account_password)
        coins = int(self.__account_coins)
        time = int(self.__time_deal)
        user = (iban, name, password, coins, time)
        return user

    def save_to_db(self):
        conn = sqlite3.connect('banca.db')
        cur = conn.cursor()
        cur.execute(f"DELETE FROM users WHERE iban ='{self.__IBAN}';")
        conn.commit()
        user = self.val_return()
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?);", user)
        conn.commit()

    @staticmethod
    def load_from_db():
        conn = sqlite3.connect('banca.db')
        cur = conn.cursor()

        Account.char_line('-', 65)
        choice = input('Enter the IBAN of the person you want to open: ')
        choice = 'UAUA390465000004789779135255'
        cur.execute(f"SELECT * FROM users WHERE iban = '{choice}';")
        one_result = cur.fetchone()

        return one_result


    def close_acc(self):
        self.char_line('-', 65)
        print(txt_dict.dictionary_of_visualisation.get('CLOSE'))
        while True:
            choice = input('Y/N: ')
            if choice == 'Y' or choice == 'y':
                print(f'\n\tYou get {self.__account_coins} coins.')
                self.char_line('-', 65)
                return

            elif choice == 'N' or choice == 'n':
                self.char_line('-', 65)
                continue
            else:
                print(txt_dict.dictionary_of_visualisation.get('CHOICE'))

