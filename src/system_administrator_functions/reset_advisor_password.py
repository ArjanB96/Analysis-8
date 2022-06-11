from models.enums import log_user_options
from system_administrator_functions import update_advisor_info as ua
import utils.database as db
import secret
from utils.encryption import encrypt
from utils.random_pass_generator import generate_password
from utils.logging import log_user

def reset_advisor_password():

    selected_advisor = ua.get_advisor_info()

    print(f"Are you sure you want to reset {selected_advisor[4]}'s password?")
    choice = input("Enter 'y' to reset or 'n' to cancel: ")
    while choice not in ["y", "n"]:
        print("Enter a valid choice")
        choice = input("Enter 'y' to reset or 'n' to cancel: ")
    
    if choice == "y":
        new_password = generate_password()
        print(f"password is now: {new_password}")
        db.reset_advisor_pass(encrypt(new_password, secret.SECRET_KEY), selected_advisor[0])
        
        # Logs password reset
        log_user(log_user_options.PASSWORD_RESET, selected_advisor[4], selected_advisor[1])

        print("Password reset")

    elif choice == "n":
        print("Canceled")

    else:    
        print("Invalid choice")


