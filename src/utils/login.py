import sqlite3
from utils.encryption import encrypt, decrypt_employee
from utils.logging import log_login
import secret
import globals
from models.user import User

def login():
    '''
    Handles the login
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
        # Logs the successful login
        log_login()
        return True
    else:
        return False