import  mysql.connector
from mysql.connector import Error

def create_database():
    conn=None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='Alhaji',
            password='CHIDI@#@08160232043'
        )
        mydb = conn.cursor()
        mydb.execute("CREATE DATABASE BANKACCOUNT")

        if conn.is_connected():
            print("connected!!")
    except Error as e:
        print("the error is:", e)
    finally:
        conn.close()
        print("database closed")

def main():
    create_database()

if __name__=='__main__':
    main()