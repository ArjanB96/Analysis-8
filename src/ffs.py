import advisor_functions.register_member as register_member, utils.database as database, utils.login as login
from utils.logging import check_notifications
from utils.login import login
from user_options import read_options
from models.enums import authentication_level
import globals

while True:

    #create_database()             #<- creates database if it's your first time running the program

    if (login()):

        #check authentication_level in global current_user
        authentication_lvl = globals.current_user.authentication_level

        check_notifications()

        if authentication_lvl == 1:
            read_options(authentication_level.ADVISOR)
        elif authentication_lvl == 2:
            read_options(authentication_level.SYSTEM_ADMINISTRATOR)
        elif authentication_lvl == 3:
            read_options(authentication_level.SUPER_ADMINISTRATOR)
        else:
            print("Incorrect username or password, try again")
            continue
        break