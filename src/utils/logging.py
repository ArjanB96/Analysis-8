from models.enums import log_user_options
from models.log_event import LogEvent
from models.user import User
from utils.encryption import encrypt_log
import globals
from utils.database import insert_log

def log_login(successful = True, unsuccessful_username=""):
    '''
    Logs the 
    NOTE: if the login is not successful, unsuccessful_username should be given as a paramater
    '''
    if successful:
        username = globals.current_user.username
        description = "Logged in"
        additional_info = ""
    else:
        username = "..."
        description = "Unsuccessful login"
        additional_info = f"username: \"{unsuccessful_username}\" is used for a login attempt with wrong password"

    # Inserts an encrypted LogEvent object into the database
    insert_log(encrypt_log(LogEvent(username, description, additional_info, "No")))

def log_member(user_option: log_user_options, changed_values: dict = None):
    ''''
    Logs any member changes such as creating, modifying or deleting a member\n
    NOTE: when log_user_options.MODIFIED is used, changed_values should be the dictionary with the newly changed values:\n
    { "<variable_name>": its_value }\n
    EXAMPLE:\n
    Case: ZIP code and first name have changed to 1234AB and Puk\n
    { "Zip_Code": "1234AB", "First_Name": "Puk" }
    '''
    username = globals.current_user.username

    # If user is created
    if (user_option == log_user_options.CREATION):
        description = "New member has been created"

        # Inserts an encrypted LogEvent object into the database
        insert_log(encrypt_log(LogEvent(username, description, "", "No")))
        return
    # If user is deleted
    elif (user_option == log_user_options.DELETION):
        description = "Member has been deleted"

        # Inserts an encrypted LogEvent object into the database
        insert_log(encrypt_log(LogEvent(username, description, "", "No")))
        return
    # If user is modified
    else:
        description = "Member information has been modified"
        additional_info = "The modified value(s) is/are: "

        if changed_values == None:
            return
        
        for key, value in changed_values.items():
            additional_info += f"{key} to {str(value)}. "

        # Inserts an encrypted LogEvent object into the database
        insert_log(encrypt_log(LogEvent(username, description, additional_info, "No")))

def log_user(user_option: log_user_options, user: User, changed_values: dict = None):
    ''''
    Logs any user changes such as creating, modifying or deleting a advisor or system administrator\n
    NOTE: when log_user_options.MODIFIED is used, changed_values should be the dictionary with the newly changed values:\n
    { "<variable_name>": its_value }\n
    EXAMPLE:\n
    Case: password and first name have changed to W3@kPa$$w0rD and Puk\n
    { "Password": "W3@kPa$$w0rD", "First_Name": "Puk" }
    '''
    username = globals.current_user.username
    
    # If user is created 
    if user_option == log_user_options.CREATION:
        description = f"{'Advisor' if user.authentication_level == 1 else 'System Administrator'} account has been created"
        additional_info = f"Username: '{user.username}'"
    # If user is deleted
    elif user_option == log_user_options.DELETION:
        description = f"{'Advisor' if user.authentication_level == 1 else 'System Administrator'} account has been deleted"
        additional_info = f"'{user.username}' has been deleted"
    # If user is modified
    else:
        description = f"{'Advisor' if user.authentication_level == 1 else 'System Administrator'} account has been modified"
        additional_info = f"Info of '{user.username}' has been modified: "

        if changed_values == None:
            return
        
        for key, value in changed_values.items():
            additional_info += f"{key} to {str(value)}. "
    
    # Inserts an encrypted LogEvent object into the database
    insert_log(encrypt_log(LogEvent(username, description, additional_info, "No")))