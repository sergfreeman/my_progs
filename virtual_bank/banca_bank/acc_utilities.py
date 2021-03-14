from random import randint


class Utilities:
    @staticmethod
    def generate_alpha():
        """(type: String) Generate random upper case literal from A to Z"""
        return chr(randint(65, 91))

    @staticmethod
    def generate_number():
        """(type: String) Generate random number from 0 to 9"""
        return randint(0, 10)

    @staticmethod
    def char_line(symbol, quantity):
        """Drawing symbol line"""
        print(f'{symbol}' * quantity)

    @staticmethod
    def pass_valid(valid_password):
        print("Please, enter your password: ", end='')
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

    @staticmethod
    def enter_password():
        """Input password method"""
        while True:
            try:
                tmp_password = input('(ten numbers without a space):')
                if len(tmp_password) == 1:
                    if tmp_password.find(' ') and tmp_password.isdigit():
                        break
                    else:
                        print("Error, password couldn't contain white space or symbol.")
                        continue
                else:
                    print('Error, password length should be ten numbers.')
            except ValueError:
                print("Type error")
        return int(tmp_password)
