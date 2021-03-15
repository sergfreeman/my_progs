import mysql.connector
from mysql.connector import Error


class MySqlUtil:
    SITE, BASE, PASS = 'zzz.com.ua', 'sergfreeman', 'mysqlSerg1980'

    @staticmethod
    def create_connection(host_name, user_name, user_password):
        """
        :param host_name: path to the data base location
        :param user_name: name of admin
        :param user_password: password of admin
        :return: prepared connection
        """
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password)
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection

    @staticmethod
    def show_all():
        """
        Show all account table
        """
        try:
            connection = MySqlUtil.create_connection(MySqlUtil.SITE, MySqlUtil.BASE, MySqlUtil.PASS)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM sergfreeman.banca")
            rows = cursor.fetchall()
            for index, row in enumerate(rows):
                print(f'Line{index}:', row)
            cursor.close()
            connection.close()
        except Error as e:
            print(e)

    @staticmethod
    def params_from_iban(iban):
        """
        :param iban: KEY
        :return: VALUES of person with KEY-iban
        """
        try:
            connection = MySqlUtil.create_connection(MySqlUtil.SITE, MySqlUtil.BASE, MySqlUtil.PASS)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM sergfreeman.banca WHERE iban='{iban}'")
            answer = cursor.fetchall()
            cursor.close()
            connection.close()
            return answer
        except Error as e:
            print(e)

    @staticmethod
    def update_person(iban, name, password, coins, time, mail):
        """
            get VALUES:
            iban,name ->(str)\n
            password, coins, time ->(int)\n
            \n if iban is valid, update person VALUES in data base from KEY iban\n
            else create new person with current parameters
        """
        connection = MySqlUtil.create_connection(MySqlUtil.SITE, MySqlUtil.BASE, MySqlUtil.PASS)
        cursor = connection.cursor()

        # check iban for availability
        cursor.execute(f"SELECT * FROM sergfreeman.banca WHERE iban='{iban}'")
        is_valid = cursor.fetchall()

        if len(is_valid) == 0:
            using = f"""
            INSERT INTO sergfreeman.banca 
            (iban, name, password, coins, deal_time, mail) 
            VALUES 
            ('{iban}','{name}','{password}','{coins}','{time}', '{mail}')
            """
        else:
            using = f"""
            UPDATE sergfreeman.banca set
            iban = '{iban}',
            name = '{name}',
            password = '{password}',
            coins = '{coins}',
            deal_time = '{time}',
            mail = '{mail}'
            WHERE iban = '{iban}'
            """

        cursor.execute(f'{using}')
        pers_data = iban, name, password, coins, time, mail
        cursor.close()
        return pers_data

    @staticmethod
    def del_person_acc(iban):
        """get KEY iban(str):\n
            delete person with this iban"""
        try:
            connection = MySqlUtil.create_connection(MySqlUtil.SITE, MySqlUtil.BASE, MySqlUtil.PASS)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM sergfreeman.banca WHERE iban='{iban}';")
            cursor.close()
            connection.close()

        except Error as e:
            print(e)

    @staticmethod
    def is_unique_iban(iban):
        """
        check for unequal iban
        :param iban:(str)
        :return: True or False
        """
        connection = MySqlUtil.create_connection(MySqlUtil.SITE, MySqlUtil.BASE, MySqlUtil.PASS)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM sergfreeman.banca WHERE iban='{iban}'")
        tmp = len(cursor.fetchall())
        cursor.close()
        connection.close()
        if tmp == 0:
            return True
        else:
            return False
