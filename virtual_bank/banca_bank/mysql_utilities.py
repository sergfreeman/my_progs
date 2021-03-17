import mysql.connector
from mysql.connector import Error
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

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

    # @staticmethod
    # def mailer(mailbox, text):
        # import smtplib  # Импортируем библиотеку по работе с SMTP

        # Добавляем необходимые подклассы - MIME-типы
        # from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
        # from email.mime.text import MIMEText  # Текст/HTML
        # from email.mime.image import MIMEImage  # Изображения

        # addr_from = "banca.bank@meta.ua"  # Адресат
        # addr_to = "sergandd@gmail.com"  # Получатель
        # password = "banca.bank21"  # Пароль
        #
        # msg = MIMEMultipart()  # Создаем сообщение
        # msg['From'] = addr_from  # Адресат
        # msg['To'] = addr_to  # Получатель
        # msg['Subject'] = 'Тема сообщения'  # Тема сообщения
        #
        # body = "Текст сообщения"
        # msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст
        #
        # server = smtplib.SMTP('smtp.meta.ua', 465)
        #
        # # server = smtplib.SMTP('smtp.ukr.net', 2525)  # Создаем объект SMTP
        # # server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
        # server.starttls()  # Начинаем шифрованный обмен по TLS
        # server.login(addr_from, password)  # Получаем доступ
        # server.send_message(msg)  # Отправляем сообщение
        # server.quit()  # Выходим

    # @staticmethod
    # def mailer(mailbox, text):
    #     # -*- coding: cp1251 -*-
    #     import smtplib
    #     # from email.MIMEText import MIMEText
    #
    #     # отправитель
    #     me = 'banca.bank@meta.ua'
    #     # получатель
    #     you = mailbox
    #     # текст письма
    #     text = text
    #     # заголовок письма
    #     subj = 'Привет от Python'
    #
    #     # параметры SMTP-сервера
    #     server = "smtp.meta.ua"  # "smtp.bk.ru"
    #     port = 465
    #     user_name = "banca.bank@meta.ua"
    #     user_passwd = "banca.bank21"
    #
    #     msg = MIMEText(text, "", "cp1251")
    #     msg['Subject'] = subj
    #     msg['From'] = me
    #     msg['To'] = you
    #
    #     s = smtplib.SMTP(server, port)
    #     s.starttls()
    #     s.login(user_name, user_passwd)
    #     s.sendmail(me, you, msg.as_string())
    #     s.quit()
    #
