# first import the mysql connector

import mysql.connector

# import the error module from mysql connector
from mysql.connector import Error

# define the connector function
def connect_fetch():
    '''function to connect and fetch  rows in a database'''

    # create a variable for the connector object
    conn = None

    try:
        conn = mysql.connector.connect(
           host='localhost',
           database = 'cape_codd',
           user = 'Alhaji',
           password = 'CHIDI@#@08160232043')
        # what to display once connection is successful
        print("connected to the database")

        # select query
        sql_select_query = "select*from buyer"
        # cursor variable
        cursor = conn.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()

        # print select output
        print("\nprinting each buyer record")
        for rows in records:
            print("Buyer name: ", rows[0])
            print("Department: ", rows[1])
            print("Position: ", rows[2])
            print("Supervisor: ", rows[3])



    except Error as e:
        print('not connecting due to : ',e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('database shutdown!!!')

connect_fetch()

