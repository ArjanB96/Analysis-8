import sqlite3

'''
This is a test to create a database and add a table with rows in it
'''


def create_database():
    # Connecting to sqlite
    connection = sqlite3.connect('pythonsqlite.db')
    
    # cursor 
    cursor = connection.cursor()
    
    # Drop the Test table if already exists.
    cursor.execute("DROP TABLE IF EXISTS MEMBER")
    
    # Create table MEMBER
    table = """ CREATE TABLE MEMBER (
                Member_Id INTEGER PRIMARY KEY,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25) NOT NULL,
                Street VARCHAR(255) NOT NULL,
                House_Number VARCHAR(255) NOT NULL,
                Zip_Code VARCHAR(6) NOT NULL,
                City VARCHAR(255) NOT NULL,
                Email_Address VARCHAR(255) NOT NULL,
                Phone_Number VARCHAR(255) NOT NULL,
                Registration_Date DATE NOT NULL
            ); """

    cursor.execute(table)
    
    print("Table is Ready")
    
    '''
    NOTE: We can create the User here later on
    table = """ CREATE TABLE USER (
                User_Id INTEGER PRIMARY KEY,
                etc. etc.
                '''

    connection.commit()


# create a function to enter input in database
def enter_data(member_id, first_name, last_name, street, house_number, zip_code, city, email, phone_number, registration_date):
    
    # Connecting to sqlite
    connection = sqlite3.connect('pythonsqlite.db')

    # cursor 
    cursor = connection.cursor()

    cursor.execute("INSERT INTO MEMBER (Member_Id, First_Name, Last_Name, Street, House_Number, Zip_Code, City, Email_Address, Phone_Number, Registration_Date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (member_id, first_name, last_name, street, house_number, zip_code, city, email, phone_number, registration_date))
    
    connection.commit()

    connection.close()