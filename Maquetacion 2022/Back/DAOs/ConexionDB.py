import mysql, mysql.connector
from mysql.connector import Error

def getConnection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port = '3306',
                                             database='DebuggingSI',
                                             user='debugging',
                                             password='debug1234')
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

def closeConnection(connection):
    if connection.is_connected():
        connection.close()
