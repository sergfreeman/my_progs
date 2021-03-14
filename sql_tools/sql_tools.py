import mysql.connector
from mysql.connector import Error

from random import randint


class MySqlTools:

    THE_SITE, THE_BASE, THE_PASS = 'zzz.com.ua', 'sergfreeman', 'mysqlSerg1980'

    @staticmethod
    def create_connection(host_name, user_name, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password)

            # print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection


    @staticmethod
    def show_all():
        try:

            connection = MySqlTools.create_connection(MySqlTools.THE_SITE, MySqlTools.THE_BASE, MySqlTools.THE_PASS)
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
    def show_from_iban(iban):
        try:

            connection = MySqlTools.create_connection(MySqlTools.THE_SITE, MySqlTools.THE_BASE, MySqlTools.THE_PASS)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM sergfreeman.banca WHERE iban='{iban}'")

            c = cursor.fetchall()
            print(c)
            cursor.close()
            connection.close()
        except Error as e:
            print(e)



    @staticmethod
    def update_person(iban, name, password, coins, time):
        """
            get values:
            iban,name ->(str)\n
            password, coins, time ->(int)\n
            \n update person values in data base from key IBAN
        """
        connection = MySqlTools.create_connection(MySqlTools.THE_SITE, MySqlTools.THE_BASE, MySqlTools.THE_PASS)
        cursor = connection.cursor()

        UPDATE = f"""
            UPDATE sergfreeman.banca set 
            iban = '{iban}',
            name = '{name}', 
            password = '{password}',
            coins = '{coins}',
            deal_time = '{time}'
            WHERE iban = '{iban}'
            """

        cursor.execute(f'{UPDATE}')
        pers_data = iban, name, password, coins, time
        cursor.close()
        return pers_data


mysql_tool = MySqlTools()
mysql_tool.show_all()
# mysql_tool.show_from_iban('zero_iban')
mysql_tool.update_person('newIban', 'random value', randint(1,10), randint(1,50), randint(1,1000))