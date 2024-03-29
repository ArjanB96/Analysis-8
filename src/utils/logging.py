import secret
from models.enums import log_user_options, log_backup_options, log_lookup_options
from models.log_event import LogEvent
from utils.encryption import encrypt_log, encrypt
import globals
from utils.database import insert_log, connect_db
from utils.bcolors import *

def log_login(successful = True, unsuccessful_username=""):
    '''
    Logs the 
    NOTE: if the login is not successful, unsuccessful_username should be given as a paramater
    '''
    if successful:
        globals.failed_login_attempts = 0
        username = globals.current_user.username
        description = "Logged in"
        additional_info = ""
    else:
        globals.failed_login_attempts += 1

        username = "..."
        description = "Unsuccessful login"
        additional_info = f"username: \"{unsuccessful_username}\" is used for a login attempt with wrong password"

    # Inserts an encrypted LogEvent object into the database
    insert_log(encrypt_log(LogEvent(username, description, additional_info, "No")))

    # Every 3 failed login attempts, logs the failed attempts as suspicious
    if globals.failed_login_attempts % 3 == 0 and globals.failed_login_attempts != 0:
        username = "..."
        description = "Unsuccessful login"
        additional_info = "Multiple failed login attempts"
        insert_log(encrypt_log(LogEvent(username, description, additional_info, "Yes")))

def log_member(user_option: log_user_options, changed_values: dict = None):
    '''
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

def log_user(user_option: log_user_options, user_username: str, user_auth_level: int,changed_values: dict = None):
    '''
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
        description = f"{'Advisor' if user_auth_level == 1 else 'System Administrator'} account has been created"
        additional_info = f"Username: \"{user_username}\""
    # If user is deleted
    elif user_option == log_user_options.DELETION:
        description = f"{'Advisor' if user_auth_level == 1 else 'System Administrator'} account has been deleted"
        additional_info = f"\"{user_username}\" has been deleted"
    # If user is modified
    elif user_option == log_user_options.MODIFIED:
        description = f"{'Advisor' if user_auth_level == 1 else 'System Administrator'} account has been modified"
        additional_info = f"Info of \"{user_username}\" has been modified: "

        if changed_values == None:
            return
        
        for key, value in changed_values.items():
            additional_info += f"{key} to {str(value)}. "
    # If user's password is reset to a temporary password
    else:
        description = f"{'Advisor' if user_auth_level == 1 else 'System Administrator'} password has been reset"
        additional_info = f"Passowrd of \"{user_username}\" has been reset with a temporary password"
    
    # Inserts an encrypted LogEvent object into the database
    insert_log(encrypt_log(LogEvent(username, description, additional_info, "No")))

def log_backup(backup_option: log_backup_options):
    '''
    Logs whether a backup has been created or restored
    '''
    username = globals.current_user.username 
    description = f"Backup {'created' if backup_option == log_backup_options.CREATION else 'restored'}"

    # Inserts an encrypted LogEvent into the database
    insert_log(encrypt_log(LogEvent(username, description, "", "No")))

def log_lookup(lookup_option: log_lookup_options, member_lookup_search = ""):
    '''
    Logs a member or user lookup activity. 
    NOTE: If member option is chosen, member_lookup_search should be given which is the decrypted lookup that the user performed
    '''
    username = globals.current_user.username
    description = f"{'Member' if lookup_option == log_lookup_options.MEMBER else 'User'} looked up"

    if lookup_option == log_lookup_options.MEMBER:
        additional_info = f"The keyword used to search was: {member_lookup_search}"
    else:
        additional_info = ""
    
    # Inserts an encrypted LogEvent into the database
    insert_log(encrypt_log(LogEvent(username, description, additional_info, "No")))

def log_log_view(suspicious_viewed = False):
    '''
    Logs the 'view logs' activity
    '''
    username = globals.current_user.username
    description = f"{'Suspicious' if suspicious_viewed else ''} Log file(s) viewed"
    insert_log(encrypt_log(LogEvent(username, description, "", "No")))

def log_password_change(new_password: str):
    '''
    Logs the change of the password of the current user
    '''
    username = globals.current_user.username
    description = f"Changed their own password"
    additional_info = f"Password changed into: {new_password}"
    insert_log(encrypt_log(LogEvent(username, description, additional_info, "No")))

def log_view_list_of_users():
    '''
    Logs the view of the list of users and their roles activity
    '''
    username = globals.current_user.username
    description = "Viewed users and their role(s)"
    insert_log(encrypt_log(LogEvent(username, description, "", "No")))

def check_notifications():
    '''
    Checks if the user is an admin. If the user is an admin. It will print the amount of unread suspicious logs if there are any. Otherwise doesn't print anything. 
    Returns True if there are notifications, else False
    '''

    # Only Admins can view the log(s) and thus only they should see the notifications
    if globals.current_user.authentication_level <= 1:
        return False
    
    connection, cursor = connect_db()

    # Gets the row count
    unread_flagged_logs_count = cursor.execute("SELECT Count(*) FROM LOGS WHERE NOT Read AND Suspicious = ?", (encrypt("Yes", secret.SECRET_KEY),)).fetchone()[0]

    if unread_flagged_logs_count > 0:
        print(f"\n{bcolors.WARNING}ALERT!\nThere are unread suspicious activities.\nAmount of unread suspicious activities:{bcolors.ENDC}", unread_flagged_logs_count)
        connection.close()
        return True
    return False
