# import mysql.connector
# from mysql.connector import Error
#
# class Tools:
#     connection = mysql.connector.connect(, 'zzz.com.ua', 'sergfreeman', 'mysqlSerg1980')



import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='zzz.com.ua', database='sergfreeman', password='mysqlSerg1980')
        if conn.is_connected():
            print('Connected to MySQL database')
            # conn.close()
    except Error as e:
        print(e)

    finally:
        pass

connect()