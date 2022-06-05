import advisor_functions.register_member as register_member, utils.database as database, utils.login as login
from utils.login import login
from user_options import read_options
from authentication_level_enum import authentication_level

while True:
    database.create_database()             #<- creates database if it's your first time running the program
    #register_member.register_member()
    
    role = login()

    if role == "advisor":
        read_options(authentication_level.ADVISOR)

    elif role == "system_administrator":
        read_options(authentication_level.SYSTEM_ADMINISTRATOR)

    elif role == "super_administrator":
        read_options(authentication_level.SUPER_ADMINISTRATOR)

    else:
        print("Incorrect username or password")
        continue
    
    break