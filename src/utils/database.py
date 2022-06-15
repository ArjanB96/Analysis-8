import sqlite3
from datetime import datetime
from secret import SECRET_KEY
from utils.encryption import encrypt, encrypt_employee, decrypt, de_or_encrypt_member, de_or_encrypt_employee
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
    connection, cursor = connect_db()
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
                Employee_Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Authentication_Level TINYINT NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25) NOT NULL,
                Username ChAR(25) NOT NULL,
                Password CHAR(25) NOT NULL,
                Registration_Date DATE NOT NULL,
                Changed_Pass BOOLEAN NOT NULL
            ); """
    cursor.execute(table_employee)

    # Create table LOGS
    table_logs = """    
        CREATE TABLE IF NOT EXISTS LOGS (
            Log_Id INTEGER PRIMARY KEY,
            Username VARCHAR(20),
            Date DATETIME NOT NULL,
            Time DATETIME NOT NULL,
            Description_Of_Activity VARCHAR(50) NOT NULL,
            Additional_Information VARCHAR(100),
            Suspicious VARCHAR(3) NOT NULL,
            Read BOOLEAN NOT NULL
        );"""
    cursor.execute(table_logs)

    # Inserts hardcoded Superadmin, if it doesn't exist yet, with username: superadmin and password: Admin321!
    super_admin_tuple_enc = encrypt_employee((1, authentication_level.SUPER_ADMINISTRATOR.value, "Super", "Administrator", "superadmin", "Admin321!", datetime.today(), False))
    cursor.execute("""
        INSERT INTO EMPLOYEE(Employee_Id, Authentication_Level, First_Name, Last_Name, Username, Password, Registration_Date, Changed_Pass) 
        SELECT ?, ?, ?, ?, ?, ?, ?, ?
        WHERE NOT EXISTS(SELECT 1 FROM EMPLOYEE WHERE Employee_Id = 1);""", 
        (super_admin_tuple_enc[0], super_admin_tuple_enc[1], super_admin_tuple_enc[2], super_admin_tuple_enc[3], super_admin_tuple_enc[4], super_admin_tuple_enc[5], super_admin_tuple_enc[6], False))
    
    commit_and_close(connection)

# function to enter input in database
def insert_member(member_id, first_name, last_name, street, house_number, zip_code, city, email, phone_number, registration_date):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO MEMBER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (member_id, first_name, last_name, street, house_number, zip_code, city, email, phone_number, registration_date))
    commit_and_close(connection)

def insert_advisor(authentication_level, first_name, last_name, username, password, registration_date):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (None, authentication_level, first_name, last_name, username, password, registration_date, False))
    commit_and_close(connection)

def update_password(username, password):
    connection, cursor = connect_db()
    cursor.execute("""UPDATE EMPLOYEE SET Password = ?, Changed_Pass = ? WHERE Username = ?""", (password, False, username))
    commit_and_close(connection)

def update_member(member_id, first_name, last_name, street, house_number, zip_code, city, email, phone_number, registration_date, member_id_old):
    connection, cursor = connect_db() 
    cursor.execute("""UPDATE MEMBER SET Member_Id = ?, First_Name = ?, Last_Name = ?, Street = ?, House_Number = ?, Zip_Code = ?, City = ?, Email_Address = ?, Phone_Number = ?, 
    Registration_Date = ? WHERE Member_Id = ?""",(member_id, first_name, last_name, street, house_number, zip_code, city, email, phone_number, registration_date, member_id_old))
    commit_and_close(connection)

def update_user(employee_id, role, first_name, last_name, username, password, registration_date, employee_id_old):
    connection, cursor = connect_db() 
    if role == "advisor":
        auth_level = int(encrypt(str(1), SECRET_KEY))
    elif role == "admin":
        auth_level = int(encrypt(str(2), SECRET_KEY))
    if role == "advisor" or "admin":
        cursor.execute("""UPDATE EMPLOYEE SET Employee_Id = ?, Authentication_Level = ?, First_Name = ?, Last_Name = ?, Username = ?, Password = ?, Registration_Date = ?, 
        Changed_Pass = ? WHERE Employee_Id = ?""", (employee_id, auth_level, first_name, last_name, username, password, registration_date, False, employee_id_old))
    #cursor.execute("""UPDATE EMPLOYEE SET Employee_Id = ?, Authentication_Level = ?, First_Name = ?, Last_Name = ?, Username = ?, Password = ?, Registration_Date = ?, 
    #Changed_Pass = ? WHERE Employee_Id = ?""",(employee_id, auth_level, first_name, last_name, username, password, registration_date, False, employee_id_old))
    commit_and_close(connection)

def delete_user(employee_id):
        connection, cursor = connect_db() 
        cursor.execute("""DELETE FROM EMPLOYEE WHERE Employee_Id = ?""", (employee_id,))
        commit_and_close(connection)

def delete_member(member_id):
    connection, cursor = connect_db() 
    cursor.execute("""DELETE FROM MEMBER WHERE Member_Id = ?""", (member_id,))
    commit_and_close(connection)

def show_all_members():
    connection, cursor = connect_db() 
    cursor.execute("SELECT * FROM MEMBER")
    members = cursor.fetchall()
    connection.close()
    members_decrypted = []
    for member in members:
        member_decrypted = de_or_encrypt_member(member, decrypt)
        members_decrypted.append(member_decrypted)
    return members_decrypted

def check_all_member_ids():
    connection, cursor = connect_db()
    cursor.execute("SELECT Member_Id FROM MEMBER")
    members = cursor.fetchall()
    members = [member[0] for member in cursor.execute("SELECT Member_Id FROM MEMBER")]
    connection.close()
    return members

def check_all_employee_ids():
        connection, cursor = connect_db()    
        cursor.execute("SELECT Employee_Id FROM EMPLOYEE")
        employees = cursor.fetchall()
        employees = [employee[0] for employee in cursor.execute("SELECT Employee_Id FROM EMPLOYEE")]
        connection.close()
        return employees

def check_all_usernames():
        connection, cursor = connect_db() 
        cursor.execute("SELECT Username FROM EMPLOYEE")
        members = cursor.fetchall()
        members = [member[0] for member in cursor.execute("SELECT Username FROM EMPLOYEE")]
        connection.close()
        return members

def view_users_and_roles(role):   
        if role == "advisor":     	
            auth_level = int(encrypt(str(1), SECRET_KEY))
        elif role == "admin":
            auth_level = int(encrypt(str(2), SECRET_KEY))
        connection, cursor = connect_db()
        if role == "advisor" or role == "admin": 
            cursor.execute("SELECT * FROM EMPLOYEE WHERE Authentication_Level = ?", (auth_level,))
        elif role == "all":
            cursor.execute("SELECT * FROM EMPLOYEE")
        employees = cursor.fetchall()
        employees_decrypted = []
        for employee in employees:
            employee_decrypted = de_or_encrypt_employee(employee, decrypt)
            employees_decrypted.append(employee_decrypted)
        connection.close()
        return employees_decrypted


def reset_user_pass(password, employee_id):
        connection, cursor = connect_db()
        cursor.execute("""UPDATE EMPLOYEE SET Password = ?, Changed_Pass = ? WHERE Employee_Id = ?""", (password, True, employee_id))
        commit_and_close(connection)

def insert_log(log_event: LogEvent):
    connection, cursor = connect_db()
    cursor.execute("""INSERT INTO LOGS (Username, Date, Time, Description_Of_Activity, Additional_Information, Suspicious, Read) 
    VALUES (?, ?, ?, ?, ?, ?, ?)""", (log_event.username, log_event.date, log_event.time, log_event.description_of_activity, log_event.additional_information, log_event.suspicious, False))
    commit_and_close(connection)

def connect_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    # Connecting to sqlite
    connection = sqlite3.connect('pythonsqlite.db')

    # cursor 
    cursor = connection.cursor()
    return connection, cursor


def commit_and_close(connection):
    connection.commit()
    connection.close()