from models.enums import log_user_options
from datetime import datetime
import utils.database as db
from utils.encryption import encrypt
import utils.value_checks as value_checks, secret
from utils.logging import log_user
from utils.bcolors import *

def create_advisor_or_admin(role):
    """
    This function creates an advisor or a system administrator account.
    """
    if role == "advisor":
        auth_level = 1
        authentication_level_enc = int(encrypt(str(1), secret.SECRET_KEY))
    elif role == "system_administrator":
        auth_level = 2
        authentication_level_enc = int(encrypt(str(2), secret.SECRET_KEY))

    # first name
    first_name = input("Enter first name: ")
    while not value_checks.is_valid_name(first_name):
        first_name = input(f"{bcolors.FAIL}Enter first name: {bcolors.ENDC}")
    first_name_enc = encrypt(first_name, secret.SECRET_KEY)
    
    # last name
    last_name = input("Enter last name: ")
    while not value_checks.is_valid_name(last_name):
        last_name = input(f"{bcolors.FAIL}Enter last name: {bcolors.ENDC}")
    last_name_enc = encrypt(last_name, secret.SECRET_KEY)
    
    # username
    username = input("Enter username: ")
    while not value_checks.is_valid_username(username):
        print(f"{bcolors.FAIL}Username length must be at least 6 characters long and at most 10 characters long.\nUsername must start with a letter.\nThe username may contain letters, numbers, underscores, apostrophes and periods.{bcolors.ENDC}")
        username = input(f"{bcolors.FAIL}Enter username: {bcolors.ENDC}")
    username_enc = encrypt(username, secret.SECRET_KEY)
    
    # password
    password = input("Enter password: ")
    while not value_checks.is_valid_password(password):
        print(f"{bcolors.FAIL}Password must be at least 8 characters long and at most 30 characters long.\nThe password may contain letters, numbers and special characters.\nThe password must have a combination of at least one lowercase letter, uppercase letter, one digit and one special character.{bcolors.ENDC}")
        password = input(f"{bcolors.FAIL}Enter password: {bcolors.ENDC}")
    password_enc = encrypt(password, secret.SECRET_KEY)
    
    # automatically add current date as registration date
    registration_date = str(datetime.today())
    
    # Encrypting first name, last name, street, house number, zip code, city, email, mobile phone
    db.insert_advisor(authentication_level_enc, first_name_enc, last_name_enc, username_enc, password_enc, registration_date)

    # Logs the creation of advisor
    log_user(log_user_options.CREATION, username, auth_level)

    if role == "advisor":
        print(f"{bcolors.OKBLUE}\nAdvisor registered{bcolors.ENDC}\n")
    elif role == "system_administrator":
        print(f"{bcolors.OKBLUE}\nSystem administrator registered{bcolors.ENDC}\n")