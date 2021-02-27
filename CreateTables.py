import  mysql.connector
from mysql.connector import Error

def create_table():
    conn=None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='Alhaji',
            password='CHIDI@#@08160232043',
            database='BANKACCOUNT'
        )
        mydb = conn.cursor()
        customerTable = "CREATE TABLE customer(customerId INT AUTO_INCREMENT PRIMARY KEY, firstname varchar (50)," \
                        "lastname varchar (30),middlename VARCHAR (30), dob DATE, mobile_number INTEGER UNIQUE ," \
                        "occupation varchar (30))"

        accountTable =  "CREATE TABLE account(accountnumber INT UNIQUE PRIMARY KEY, customerid INT," \
                         "type VARCHAR(255), status VARCHAR(255), openingDate DATE,"\
                         "FOREIGN KEY (customerid) references customer(customerid))"

        transactionTable = "CREATE TABLE transaction(transaction  INT PRIMARY KEY, accountNumber INT," \
                           " date DATE, type  VARCHAR(50) , amount INT , medium VARCHAR(50), " \
                           "FOREIGN  KEY (accountNumber) REFERENCES  account(accountNumber))"
        # mydb.execute (customerTable)
        mydb.execute (accountTable)
        mydb.execute (transactionTable)

        if conn.is_connected():
            print("table is created")
    except Error as e:
            print("Table cannot be created due to", e)
    finally:
        if conn is not None and conn.is_connected():
                conn.close()
                print("database shutdown!")

def main():
    create_table()

if __name__== '__main__':
    main()