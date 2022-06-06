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
    # If login was unsuccessful, the unencrypted username will be added to a log
    username = input("Enter username: ")

    username_enc = encrypt(username, secret.SECRET_KEY )
    password = encrypt(input("Enter password: "), secret.SECRET_KEY )

    check_username_and_password = cursor.execute(
        'SELECT * FROM EMPLOYEE WHERE Username = ? AND Password = ?', (username_enc, password,))

    user_tuple = check_username_and_password.fetchone()

    if user_tuple is not None:
        globals.current_user = User(decrypt_employee(user_tuple))

        # Logs the successful login
        log_login()

        return True
    else:
        # Logs the unsuccuessful login with the username that was used to login
        log_login(False, username)
        print("Invalid username or password")
        
        return False