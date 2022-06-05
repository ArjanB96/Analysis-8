import sqlite3
from utils.encryption import decrypt, encrypt, decrypt_employee
import secret
import globals
from models.user import User

def login():
    '''
    Handles the login\n
    Returns whether the login was successful or not
    '''
    connection = sqlite3.connect('pythonsqlite.db')
    cursor = connection.cursor()

    print("Login page")
    username = encrypt(input("Enter username: "), secret.SECRET_KEY )
    password = encrypt(input("Enter password: "), secret.SECRET_KEY )

    check_username_and_password = cursor.execute(
        'SELECT * FROM EMPLOYEE WHERE Username = ? AND Password = ?', (username, password,))

    user_tuple = check_username_and_password.fetchone()

    if user_tuple is not None:
        globals.current_user = User(decrypt_employee(user_tuple))
        return True
    else:
        return False