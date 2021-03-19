import mysql.connector
from mysql.connector import Error
import webbrowser
from email.mime.text import MIMEText
import smtplib
import ssl


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

    @staticmethod
    def mailer(c_mailbox: str, c_name: str, c_password: str):
        """
        resembles a customer's password via e-mail.\n
        :param c_mailbox: email address of client
        :param c_name: name of client
        :param c_password: clients account password
        :return: Non
        """
        sender = 'banca.bank@meta.ua'
        receivers = [c_mailbox]

        port = 465
        user = 'banca.bank@meta.ua'
        password = 'banca.bank21'

        msg = MIMEText(f"""
              Hello, dear {c_name}. 
        We have sent your password: {c_password}. 
        Thank you for your cooperation. 
        If you don't enter in our base, forget this letter.
        """)

        msg['Subject'] = 'Remember a password'
        msg['From'] = 'banca.bank@meta.ua'
        msg['To'] = 'sergandd@gmail.com'

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.meta.ua", port, context=context) as server:

            server.login(user, password)
            server.sendmail(sender, receivers, msg.as_string())

            print('mail successfully sent')


    @staticmethod
    def open_info_web():
        """Open web site with information about this program"""
        webbrowser.open('http://sergfreeman.zzz.com.ua/UA.banca.bank.html')

