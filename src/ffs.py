import sqlite3
import random
import register_member, database, choices, login, secret, decryption

while True:
    #database.create_database()             #<- creates database if it's your first time running the program

    print(decryption.decrypt("iffiofjj", secret.SECRET_KEY))

    register_member.register_member()
    role = login.login()
    if role == "advisor":
        choices.advisor()
    elif role == "system_administrator":
        choices.system_administrator()
    elif role == "super_administrator":
            choices.super_administrator()
    else:
        print("Incorrect username or password")
        continue
    break
    