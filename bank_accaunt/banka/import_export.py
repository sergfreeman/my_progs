from datetime import datetime


class ImportExport:
    def __init__(self, my_name, my_account_number, my_account_password, my_account_coins, my_operation_time):

        """
            Initial four class ImportExport params
                __name (type: String)
                    Name of clients
                __IBAN (type: String)
                    Unique account number
                __account_password (type: String)
                    Unique password
                __account_coins  (type: Integer)
                    Balance
                __my__operation_time (type: Integer)
                    Time of deal operation
        """
        self.__name = my_name
        self.__IBAN = my_account_number
        self.__account_password = my_account_password

        self.__account_coins = my_account_coins
        self.__account_coins = 0
        self.__operation_time = my_operation_time
        self.__my_operation_time = 0

    def ac_import(self):
        pass

    def ac_export(self):
        pass

    @staticmethod
    def get_time():
        current_time = round(datetime.timestamp(datetime.now()))
        print(current_time)
        return current_time

    @staticmethod
    def char_selector(str_line):
        str_tmp = ''
        for _ in range(0, len(str_line)):
            if str_line[_] != '*':
                str_tmp += str_line[_]
            else:
                return str_tmp

    @staticmethod
    def list_db_open():

        db_list = list()
        f = open('bank_db.banka', 'r')

        db_account_list = list(f)

        for element in range(len(db_account_list)):
            str_current_line = db_account_list[element]
            # print(str_current_line)

            the_key_iban = ImportExport.char_selector(str_current_line)
            str_current_line = str_current_line[len(the_key_iban) + 1:]
            db_account_list.append(the_key_iban)

            the_name_val = ImportExport.char_selector(str_current_line)
            str_current_line = str_current_line[len(the_name_val) + 1:]
            db_account_list.append(the_name_val)

            the_password_val = ImportExport.char_selector(str_current_line)
            str_current_line = str_current_line[len(the_password_val) + 1:]
            db_account_list.append(the_password_val)

            the_coins_val = ImportExport.char_selector(str_current_line)
            str_current_line = str_current_line[len(the_coins_val) + 1:]
            db_account_list.append(int(the_coins_val))

            the_time_val = ImportExport.char_selector(str_current_line)
            str_current_line = str_current_line[len(the_time_val) + 1:]
            db_account_list.append(int(the_time_val))

            # print(f'Name:{the_name_val}')
            # print(f'Password:{the_password_val}')
            # print(f'Coins:{the_coins_val}')
            # print(f'Time:{the_time_val}')
            # print(f'IBAN:{the_key_iban}')

            db_list.append([[the_key_iban], [the_name_val, the_password_val, the_coins_val, the_time_val]])


        f.close()
        # print(db_list)
        # print(db_list[1][1][0])
        return db_list

    # @staticmethod
    # def list_db_create():
    #
    #     db_account_list = list()
    #     f = open('bank_db.banka', 'r')
    #
    #     for element in f:
    #         str_current_line = element
    #         print(str_current_line)
    #
    #         the_key_iban = ImportExport.char_selector(str_current_line)
    #         str_current_line = str_current_line[len(the_key_iban) + 1:]
    #         db_account_list.append(the_key_iban)
    #
    #         the_name_val = ImportExport.char_selector(str_current_line)
    #         str_current_line = str_current_line[len(the_name_val) + 1:]
    #         db_account_list.append(the_name_val)
    #
    #         the_password_val = ImportExport.char_selector(str_current_line)
    #         str_current_line = str_current_line[len(the_password_val) + 1:]
    #         db_account_list.append(the_password_val)
    #
    #         the_coins_val = ImportExport.char_selector(str_current_line)
    #         str_current_line = str_current_line[len(the_coins_val) + 1:]
    #         db_account_list.append(int(the_coins_val))
    #
    #         the_time_val = ImportExport.char_selector(str_current_line)
    #         str_current_line = str_current_line[len(the_time_val) + 1:]
    #         db_account_list.append(int(the_time_val))
    #
    #         print(f'Name:{the_name_val}')
    #         print(f'Password:{the_password_val}')
    #         print(f'Coins:{the_coins_val}')
    #         print(f'Time:{the_time_val}')
    #         print(f'IBAN:{the_key_iban}')
    #
    #         break
    #
    #     f.close()
    #     print(db_account_list)
    #     return db_account_list

    @staticmethod
    def dict_db_unpacking(some_list):
        client_list = list()
        client_list = some_list.split(' ')
        print(client_list)

    @staticmethod
    def dict_bd_packing():
        pass


# ImportExport.list_db_create()
# ImportExport.list_db_open()

c = ImportExport()
