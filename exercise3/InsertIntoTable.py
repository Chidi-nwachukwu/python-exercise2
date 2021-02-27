# first import the mysql connector

import mysql.connector

# import the error module from mysql connector
from mysql.connector import Error

# define the connector function
def connect_insert():
    '''function to connect and fetch  rows in a database'''

    # create a variable for the connector object
    conn = None

    try:
        conn = mysql.connector.connect(
           host='localhost',
           database = 'baron',
           user = 'Alhaji',
           password = 'CHIDI@#@08160232043')
        # what to display once connection is successfull
        print("connected to the database")
        if conn.is_connected():
            print("Connected to database")
            db_cursor=conn.cursor()
            sql = "INSERT INTO Human(name , color, gender, Bloodgroup) VALUES (%s, %s, %s, %s)"
            # create a list variable to contain all th values we want to insert into the database
            val = [
            ('Hannah', 'White', 'Female', 'B-'),
            ('Michael', 'Brown', 'Male', '0-'),
            ('Sandy', 'Black', 'Male', 'O+'),
            ( 'Green', 'Yellow', 'Male', 'AB'),
            ( 'Richard', 'Black', 'Male', 'B+')
            ]
            db_cursor.executemany(sql,val)
            conn.commit()
            print(db_cursor.rowcount, "rows was inserted")
            db_cursor.close()
    except Error as e:
        print('connection failed due to the following : ', e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('disconnected from database!!!')
connect_insert()