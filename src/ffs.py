import sqlite3
import random
import register_member, database, choices, login, secret, decryption
from user_options import show_options
from authentication_level_enum import authentication_level

while True:
    #database.create_database()             #<- creates database if it's your first time running the program

    register_member.register_member()
    role = login.login()

    if role == "advisor":
        show_options(authentication_level.ADVISOR)

    elif role == "system_administrator":
        show_options(authentication_level.SYSTEM_ADMINISTRATOR)

    elif role == "super_administrator":
        show_options(authentication_level.SUPER_ADMINISTRATOR)

    else:
        print("Incorrect username or password")
        continue
    
    break
    