import sqlite3
from utils.encryption import encrypt
import secret
import globals

class User():
    def __init__(self, user_tuple):
        self.employee_id = user_tuple[0]
        self.authentication_level = user_tuple[1]
        self.firstname = user_tuple[2]
        self.lastname = user_tuple[3]
        self.username = user_tuple[4]
        self.password = user_tuple[5]
        self.registration_date = user_tuple[6]

def login():
    connection = sqlite3.connect('pythonsqlite.db')
    cursor = connection.cursor()

    print("Login page")
    username = encrypt(input("Enter username: "), secret.SECRET_KEY )
    password = encrypt(input("Enter password: "), secret.SECRET_KEY )

    check_username_and_password = cursor.execute(
        'SELECT * FROM EMPLOYEE WHERE Username = ? AND Password = ?', (username, password,))

    user_tuple = check_username_and_password.fetchone()
    
    if check_username_and_password.fetchone() is not None:
        
        print(type(user_tuple))
        current_user = User(user_tuple)
        authentication_level = current_user.authentication_level
    
        if authentication_level == 1:
            return "advisor"
        elif authentication_level == 2:
            return "system_administrator"
        elif authentication_level == 3:
            return "super_administrator"
        else:
            return False
    else:
        return False


