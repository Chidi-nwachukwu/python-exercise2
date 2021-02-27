# first import the mysql connector

import mysql.connector

# import the error module from mysql connector
from mysql.connector import Error
customerid = int(input("Enter customer id"))
firstname = input("Enter firstname")
lastname =  input("Enter lastname")
middlename =  input("Enter middle name")
date = input("enter the date")
number = int(input('Enter number'))
occupation = input("Occupation")
def connect_insert():
    '''function to connect and fetch  rows in a database'''

    # create a variable for the connector object
    conn = None

    try:
        conn = mysql.connector.connect(
           host='localhost',
           database = 'BANKACCOUNT',
           user = 'Alhaji',
           password = 'CHIDI@#@08160232043')
        # what to display once connection is successfull
        print("connected to the database")
        if conn.is_connected():
            print("Connected to database")
            mydb = conn.cursor()
            sql = "INSERT INTO customer(customerid, firstname, lastname, middlename,dob,mobile_number,occupation) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            # create a list variable to contain all th values we want to insert into the database
            val = [(customerid, firstname, lastname, middlename, date, number, occupation)]
            mydb.executemany(sql,val)
            conn.commit()

            print(mydb.rowcount, "row was counted")
            mydb.close()

            print("Printing each buyer record")
    except Error as e:
        print("Not connecting to the database due to", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("database shutdown!")


connect_insert()
# from mysql.connector import MySQLConnection, Error
# from python_mysql_dbconfig import read_db_config
#
# def insert_book(title, isbn):
#     query = "INSERT INTO books(title,isbn) " \
#             "VALUES(%s,%s)"
#     args = (title, isbn)
#
#     try:
#         db_config = read_db_config()
#         conn = MySQLConnection(**db_config)
#
#         cursor = conn.cursor()
#         cursor.execute(query, args)
#
#         if cursor.lastrowid:
#             print('last insert id', cursor.lastrowid)
#         else:
#             print('last insert id not found')
#
#         conn.commit()
#     except Error as error:
#         print(error)
#
#     finally:
#         cursor.close()
#         conn.close()
#
# def main():
#    insert_book('A Sudden Light','9781439187036')
#
# if __name__ == '__main__':
#     main()