import sqlite3
import encryption, decryption, secret

def login():
    connection = sqlite3.connect('pythonsqlite.db')
    cursor = connection.cursor()

    username = encryption.encrypt(input("Enter username: "), secret.SECRET_KEY )
    password = encryption.encrypt(input("Enter password: "), secret.SECRET_KEY )

    check_username_and_password = cursor.execute(
        'SELECT * FROM EMPLOYEE WHERE Username = ? AND Password = ?', (username, password,))

    if check_username_and_password.fetchone() is None:
        return False

    else:
        check_authentication_level = cursor.execute(
            'SELECT Authentication_Level FROM EMPLOYEE WHERE Username = ? AND Password = ?', (username, password,))
        authentication_level = check_authentication_level.fetchone()[0]

        if authentication_level == 1:
            return "advisor"
        elif authentication_level == 2:
            return "system_administrator"
        elif authentication_level == 3:
            return "super_administrator"
        else:
            return False
