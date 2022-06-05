from msilib.schema import AdminExecuteSequence
import sqlite3
from datetime import datetime
from utils.encryption import encrypt
from authentication_level_enum import authentication_level
import secret

'''
This is the code to create a database and add a member table and a employee table
If the database stops working, you can delete the database and re-create it with the following code
A super administrator is hardcoded, following the assignment instructions

Authentication_Level: 0 = member
Authentication_Level: 1 = advisor
Authentication_Level: 2 = system administrator
Authentication_Level: 3 = super administrator
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
                Street VARCHAR(40) NOT NULL,
                House_Number INTEGER(10) NOT NULL,
                Zip_Code VARCHAR(6) NOT NULL,
                City VARCHAR(40) NOT NULL,
                Email_Address VARCHAR(40) NOT NULL,
                Phone_Number INTEGER(8) NOT NULL,
                Registration_Date DATE NOT NULL
            ); """
    cursor.execute(table)
    
    # Drop the Test table if already exists.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # Create table EMPLOYEE
    table_employee = """ CREATE TABLE EMPLOYEE (
                Employee_Id INTEGER PRIMARY KEY,
                Authentication_Level INTEGER(1) NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25) NOT NULL,
                Username ChAR(25) NOT NULL,
                Password CHAR(25) NOT NULL,
                Registration_Date DATE NOT NULL
            ); """
    cursor.execute(table_employee)

    # Drop the Test table if already exists.
    cursor.execute("DROP TABLE IF EXISTS LOGS")

    # Create table LOGS
    table_logs = """    
        CREATE TABLE LOGS (
            Log_Id INTEGER PRIMARY KEY,
            Username VARCHAR(20),
            Date DATETIME,
            Time DATETIME,
            Description_Of_Activity VARCHAR(200),
            Additional_Information VARCHAR(200),
            Suspicious VARCHAR(3)
        );"""
    cursor.execute(table_logs)

    first_name_enc = encrypt("Super", secret.SECRET_KEY)
    last_name_enc = encrypt("Administrator", secret.SECRET_KEY)
    username_enc = encrypt("superadmin", secret.SECRET_KEY)
    password_enc = encrypt("Admin321!", secret.SECRET_KEY)

    first_name_enc2 = encrypt("Arjan", secret.SECRET_KEY)
    last_name_enc2 = encrypt("B", secret.SECRET_KEY)
    username_enc2 = encrypt("Advisor_Arjan", secret.SECRET_KEY)
    password_enc2 = encrypt("Wachtwoord123", secret.SECRET_KEY)

    date_today = datetime.today()
    cursor.execute("INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?, ?, ?, ?)", (1, authentication_level.SUPER_ADMINISTRATOR.value, first_name_enc, last_name_enc, username_enc, password_enc, date_today))
    
    cursor.execute("INSERT INTO EMPLOYEE (Employee_Id, Authentication_Level, First_Name, Last_Name, Username, Password, Registration_Date) VALUES (?, ?, ?, ?, ?, ?, ?)", (2, authentication_level.ADVISOR.value, first_name_enc2, last_name_enc2, username_enc2, password_enc2, date_today))
    # Commit the changes
    connection.commit()
    
    # Close the connection
    connection.close()


# create a function to enter input in database
def insert_member(member_id, first_name, last_name, street, house_number, zip_code, city, email, phone_number, registration_date):
    
    # Connecting to sqlite
    connection = sqlite3.connect('pythonsqlite.db')

    # cursor 
    cursor = connection.cursor()

    cursor.execute("INSERT INTO MEMBER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (member_id, first_name, last_name, street, house_number, zip_code, city, email, phone_number, registration_date))
    
    connection.commit()

    connection.close()

def insert_log(log_event):
    # Connecting to sqlite
    connection = sqlite3.connect('pythonsqlite.db')

    # Cursor 
    cursor = connection.cursor()

    