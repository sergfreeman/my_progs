import mysql_tool.connector
from mysql_tool.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql_tool.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection('zzz.com.ua', "sergfreeman", "mysqlSerg1980")



# import mysql.connector
# mydb = mysql.connector.connect (
#     host = 'localhost',
#     user = 'root',
#     port = '3306',
#     passwd = 'serg1980'
#     )
# print (mydb)
