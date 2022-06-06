import sqlite3
from datetime import datetime
from utils.encryption import encrypt_employee
from models.enums import authentication_level
from models.log_event import LogEvent

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
    
    # Create table MEMBER
    table = """ CREATE TABLE IF NOT EXISTS MEMBER (
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
    
    # Create table EMPLOYEE
    table_employee = """ CREATE TABLE IF NOT EXISTS EMPLOYEE (
                Employee_Id INTEGER PRIMARY KEY,
                Authentication_Level TINYINT NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25) NOT NULL,
                Username ChAR(25) NOT NULL,
                Password CHAR(25) NOT NULL,
                Registration_Date DATE NOT NULL
            ); """
    cursor.execute(table_employee)

    # Create table LOGS
    table_logs = """    
        CREATE TABLE IF NOT EXISTS LOGS (
            Log_Id INTEGER PRIMARY KEY,
            Username VARCHAR(20),
            Date DATETIME NOT NULL,
            Time DATETIME NOT NULL,
            Description_Of_Activity VARCHAR(200) NOT NULL,
            Additional_Information VARCHAR(200),
            Suspicious VARCHAR(3) NOT NULL,
            Read BOOLEAN NOT NULL
        );"""
    cursor.execute(table_logs)

    # Inserts hardcoded Superadmin with username: superadmin and password: Admin321!
    super_admin_tuple_enc = encrypt_employee((1, authentication_level.SUPER_ADMINISTRATOR.value, "Super", "Administrator", "superadmin", "Admin321!", datetime.today()))
    cursor.execute("INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?, ?, ?, ?)", (super_admin_tuple_enc[0], super_admin_tuple_enc[1], super_admin_tuple_enc[2], super_admin_tuple_enc[3], super_admin_tuple_enc[4], super_admin_tuple_enc[5], super_admin_tuple_enc[6]))

    advisor_tuple_enc = encrypt_employee((2, authentication_level.ADVISOR.value, "Arjan", "B", "Advisor_Arjan", "Wachtwoord123", datetime.today()))
    cursor.execute("INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?, ?, ?, ?)", (advisor_tuple_enc[0], advisor_tuple_enc[1], advisor_tuple_enc[2], advisor_tuple_enc[3], advisor_tuple_enc[4], advisor_tuple_enc[5], advisor_tuple_enc[6]))
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

def update_password(username, password):
    # Connecting to sqlite
    connection = sqlite3.connect('pythonsqlite.db')

    # Cursor 
    cursor = connection.cursor()

    cursor.execute("""UPDATE EMPLOYEE SET Password = ? WHERE Username = ?""", (password, username))
    
    connection.commit()
    connection.close()

def insert_log(log_event: LogEvent):
    # Connecting to sqlite
    connection = sqlite3.connect('pythonsqlite.db')

    # Cursor 
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO LOGS (Username, Date, Time, Description_Of_Activity, Additional_Information, Suspicious, Read) 
    VALUES (?, ?, ?, ?, ?, ?, ?)""", (log_event.username, log_event.date, log_event.time, log_event.description_of_activity, log_event.additional_information, log_event.suspicious, False))
    
    connection.commit()
    connection.close()