from acc_utilities import Utilities
import txt_dict
from datetime import datetime


class Account(Utilities):
    def __init__(
            self,
            my_account_number: str,
            my_name: str,
            my_account_password: int,
            my_account_coins: int,
            my_time: str,
            my_mail: str
                ):
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
                __time_deal (type: String)
                    Registration date
                __mail (type: String)
                    Contact email
        """
        self.__name = my_name
        self.__IBAN = my_account_number
        self.__account_password = my_account_password
        self.__account_coins = my_account_coins
        self.__time_deal = my_time
        self.__mail = my_mail

    # deposit interest per day
    DEPOSIT_INTEREST = 1

    @classmethod
    def create_name(cls) -> str:
        """
            __name (type: String)
                Create name for new account from two parts (first name and last name).\n
                Both parts must have more than two and less than 50 alphabet sign.\n
                This name used by client logs.\n
                :return name

        """
        Account.char_line('-', 65)
        print("CREATE NEW ACCOUNT")
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
    def create_iban(cls) -> str:
        """ Create new unique account value IBAN (International Bank Account Number)
            https://uk.wikipedia.org/wiki/International_Bank_Account_Number \n
            :return IBAN
        """
        country_cod = 'UA'
        control_alpha = f'{Account.generate_alpha()}{Account.generate_alpha()}'
        bank_code = '390465'
        five_zero = '00000'
        account_number = ''

        # for digit in range(13):
        while len(account_number) < 14:
            # account_number += str(Account.generate_number())
            account_number = f'{account_number}{(str(Account.generate_number()))}'
        cls.__IBAN = f'{country_cod}{control_alpha}{bank_code}{five_zero}{account_number}'
        return cls.__IBAN

    @classmethod
    def create_password(cls):
        """
            __account_password (type: int)\n
            Create and confirm a new account password.\n
            Contains ten numbers without a space.
            :return confirm_password
        """
        while True:
            Account.char_line('-', 65)
            print('SET YOUR PASSWORD')
            cls.__account_password = cls.enter_password()
            print('CONFIRM YOUR PASSWORD')
            confirm_password = cls.enter_password()

            if cls.__account_password == confirm_password:
                return confirm_password
            else:
                print('PASSWORD COULD NOT CONFIRMED, TRY AGAIN.')

    @staticmethod
    def create_email() -> str:
        """Input email method,\n
        :return tmp_email"""
        while True:
            try:
                Account.char_line('-', 65)
                print('SET YOUR EMAIL')
                tmp_mail = input('(contact e-mail for remember your password):')
                if len(tmp_mail) < 320:
                    if tmp_mail.find(' '):
                        break
                    else:
                        print("Error, email couldn't contain white space.")
                        continue
                else:
                    print('Error, email length should be less then 320 symbols.')
            except ValueError:
                print("Type error")
        Account.char_line('-', 65)
        print(f'''
 Well done. You are our new Client! {txt_dict.dictionary_of_visualisation.get('WELCOME')}
                ''')
        return tmp_mail

    def __repr__(self):
        """Create representation of main object values"""
        return f"""
        |-----------------------------------------|     
        |        Private Client information       |
        |-----------------------------------------|
             Client: {self.__name}
               IBAN: {self.__IBAN}                
           password: {self.__account_password}    
              coins: {self.__account_coins} 
         registered: {self.__time_deal}  
             e-mail: {self.__mail}       
        |-----------------------------------------|
        """

    @property
    def client_balance(self):
        """(type: int) Getter of client balance"""
        return self.__account_coins

    @client_balance.setter
    def client_balance(self, val: int):
        """(type: Setter) Setter of client balance"""
        self.__account_coins = val

    @property
    def client_email(self):
        """(type: String) Getter of client email"""
        return self.__mail

    def multi_getter(self, parameter: str):
        """
        :param parameter: type of client param
        :return: value of parameter
        """
        try:
            if parameter == 'iban':
                return self.__IBAN
            elif parameter == 'name':
                return self.__name
            elif parameter == 'password':
                return self.__account_password
            elif parameter == 'coins':
                return self.__account_coins
            elif parameter == 'time':
                return self.__time_deal
            elif parameter == 'email':
                return self.__mail
        except Exception.args:
            pass

    def multi_setter(self, parameter: str, value):
        """
        :param value:
        :param parameter: type of client param
        :return: value of parameter
        """
        try:
            if parameter == 'iban':
                self.__IBAN = value
            elif parameter == 'name':
                self.__name = value
            elif parameter == 'password':
                self.__account_password = value
            elif parameter == 'coins':
                self.__account_coins += value
            elif parameter == 'time':
                self.__time_deal = value
            elif parameter == 'email':
                self.__mail = value
        except Exception.args:
            pass

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
        password = int(self.__account_password)
        coins = int(self.__account_coins)
        time = int(self.__time_deal)
        mail = str(self.__mail)
        user = (iban, name, password, coins, time, mail)
        return user

    def close_acc(self):
        self.char_line('-', 65)
        print(txt_dict.dictionary_of_visualisation.get('CLOSE'))
        while True:
            choice = input(f"""\t\t\tY/N: """)
            if choice == 'Y' or choice == 'y':
                self.char_line('-', 65)
                print(f'You get {self.__account_coins} coins.')
                print(f'CLOSE ACCOUNT ({self.__IBAN}): DONE.')
                return 'YES'

            elif choice == 'N' or choice == 'n':
                self.char_line('-', 65)
                return 'NO'
            else:
                print(txt_dict.dictionary_of_visualisation.get('CHOICE'))

