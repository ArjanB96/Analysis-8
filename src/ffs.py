import advisor_functions.register_member as register_member, utils.database as database, utils.login as login
import advisor_functions.update_password as update_password
from utils.logging import check_notifications
from utils.login import login
from user_options import read_options
from models.enums import authentication_level
from utils.bcolors import *
import globals

while True:
    # creates database if it's your first time running the program and inserts the superadmin if it is not in the database
    database.create_database() 
    
    if (login()):
        #check authentication_level in global current_user
        authentication_lvl = globals.current_user.authentication_level
        changed_password = globals.current_user.changed_pass 
        check_notifications()
        
        if authentication_lvl == 1 and changed_password == False:
            read_options(authentication_level.ADVISOR)
        elif authentication_lvl == 2 and changed_password == False:
            read_options(authentication_level.SYSTEM_ADMINISTRATOR)
        elif authentication_lvl == 3 and changed_password == False:
            read_options(authentication_level.SUPER_ADMINISTRATOR)
        elif authentication_lvl == 1 and changed_password == True:
            print(f"{bcolors.WARNING}Your password has been reset, please input a new password{bcolors.ENDC}")
            update_password.update_password()
            read_options(authentication_level.ADVISOR)
        elif authentication_lvl == 2 and changed_password == True:
            print(f"{bcolors.WARNING}Your password has been reset, please input a new password{bcolors.ENDC}")
            update_password.update_password()
            read_options(authentication_level.SYSTEM_ADMINISTRATOR)
        else:
            print(f"{bcolors.FAIL}Incorrect username or password, try again{bcolors.ENDC}")
            continue
        break