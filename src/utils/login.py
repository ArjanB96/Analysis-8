from utils.database import connect_db
from utils.encryption import encrypt, decrypt_employee
from utils.logging import log_login
import secret
import globals
from models.user import User
from utils.bcolors import *

def login():
    '''
    Handles the login
    Returns whether the login was successful or not
    '''
    connection, cursor = connect_db()

    # If login was unsuccessful, the unencrypted username will be added to a log
    username = input("Enter username: ")

    username_enc = encrypt(username, secret.SECRET_KEY )
    password = encrypt(input("Enter password: "), secret.SECRET_KEY )
    try:
        check_username_and_password = cursor.execute(
            'SELECT * FROM EMPLOYEE WHERE Username = ? COLLATE NOCASE AND Password = ?', (username_enc, password,))
        user_tuple = check_username_and_password.fetchone()
        connection.close()

        if user_tuple is not None:
            globals.current_user = User(decrypt_employee(user_tuple))

            # Logs the successful login
            log_login()
            print(f"\n{bcolors.OKBLUE}Welcome {globals.current_user.username}!{bcolors.ENDC}\n")
            return True
        else:
            # Logs the unsuccuessful login with the username that was used to login
            log_login(False, username)
            print(f"{bcolors.FAIL}Incorrect username or password, try again{bcolors.ENDC}")
            return False
    except Exception as e:
        print(f"{bcolors.FAIL}Something went wrong: {e}{bcolors.ENDC}")
        return False