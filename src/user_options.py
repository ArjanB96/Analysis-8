from models.enums import authentication_level
from advisor_functions.register_member import *
from advisor_functions.update_password import *
from system_administrator_functions import * 
from advisor_functions import update_member_info, search_member_information
from system_administrator_functions import view_users_and_roles, update_user_info, reset_user_password, backup, view_logs
from system_administrator_functions import create_advisor_or_admin, delete_member
import globals
from system_administrator_functions import delete_user

'''
Authentication_Level: 0 = member
Authentication_Level: 1 = advisor
Authentication_Level: 2 = system administrator
Authentication_Level: 3 = super administrator
'''

options_dict = {
    'Press 1 to update your password': 1,
    'Press 2 to add a new member': 1,
    'Press 3 to modify or update information of a member': 1,
    'Press 4 to search and retrieve information of a member': 1,
    'Press 5 to view the list of users and their roles': 2,
    'Press 6 to define and add a new advisor to the system': 2,
    'Press 7 to modify or update an existing advisor\'s account and profile': 2,
    'Press 8 to delete an existing advisor\'s account': 2,
    'Press 9 to reset an existing advisor\'s password (a temporary password)': 2,
    'Press 10 to make a backup of the system and restore a backup': 2,
    'Press 11 to view the log file(s) of the system': 2,
    'Press 12 to delete a member from the database': 2,
    'Press 13 to define and add a new administrator to the system': 3,
    'Press 14 to modify or update an existing administrator\'s account and profile': 3,
    'Press 15 to delete an existing administrator\'s account': 3,
    'Press 16 to reset an existing administrator\'s password (a temporary password)': 3,
    'Type \'exit\' to exit': 0
}

def print_incorrect_input():
    print("Incorrect input. Please try again")

def show_options(auth_level):
    '''Shows all the options with the given authentication_level'''
    print("")
    for key, value in options_dict.items():
        if (auth_level.value >= value):
            print(key)

def read_options(auth_level):
    while True:
        show_options(auth_level)
        user_input = input("\nEnter your option: ")

        ### All of the options 

        ### Advisor options
        # Exit option
        if user_input.lower() == "exit":
            return

        # Update password
        elif user_input == "1":
            update_password()
            continue

        # Add new member    
        elif user_input == "2":
            register_member()
            continue

        # Modify / update information of member
        elif user_input == "3":
            update_member_info.update_member_info()
            continue
        
        # Search / retrieve information of member
        elif user_input == "4":
            search_member_information.search_member_information()
            continue
        
        ### System administrator options
        # if the authentication_level is lower than the needed authentication_level, print incorrect input as it shouldn't be available to them
        if auth_level.value < authentication_level.SYSTEM_ADMINISTRATOR.value:
            print_incorrect_input()
            continue

        # View list of users and their roles
        elif user_input == "5":
            view_users_and_roles.view_users_and_roles("all")
            continue
        
        # Define and add new advisor
        elif user_input == "6":
            create_advisor_or_admin.create_advisor_or_admin("advisor")
            continue
        
        # Modify / update advisor's account and profile
        elif user_input == "7":
            update_user_info.update_user_info("advisor")
            continue
        
        # Delete an advisor's account
        elif user_input == "8":
            delete_user.delete_user("advisor")
            continue

        # Reset advisor's password (a temporary password)
        elif user_input == "9":
            reset_user_password.reset_user_password("advisor")
            continue
        
        # Make backup of the system and restore
        elif user_input == "10":
            backup.show_options()
            continue
        
        # View the log file(s) 
        elif user_input == "11":
            view_logs.view_log_options()
            continue
        
        # Delete member 
        elif user_input == "12":
            delete_member.delete_member()
            continue
        
        ### Super administrator options
        # if the authentication_level is lower than the needed authentication_level, print incorrect input as it shouldn't be available to them
        if auth_level.value < authentication_level.SUPER_ADMINISTRATOR.value:
            print_incorrect_input
            continue

        # Define and add new administrator 
        elif user_input == "13":
            create_advisor_or_admin.create_advisor_or_admin("system_administrator")
            continue
        
        # Modify / update administrator's account and profile
        elif user_input == "14":
            update_user_info.update_user_info("admin")
            continue
        
        # Delete administrator
        elif user_input == "15":
            delete_user.delete_user("admin")
            continue
        
        # Reset administrator's password (a temporary password)
        elif user_input == "16":
            reset_user_password.reset_user_password("admin")
            continue

        # Incorrect input
        else:
            print_incorrect_input()
            continue