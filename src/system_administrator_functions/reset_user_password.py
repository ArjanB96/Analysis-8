from system_administrator_functions import update_user_info as ua
import utils.database as db
import secret
from utils.encryption import encrypt
from utils.random_pass_generator import generate_password

def reset_user_password(role):
    if role == "advisor":
        selected_user = ua.get_user_info("advisor")
    elif role == "admin":
        selected_user = ua.get_user_info("admin")

    print(f"Are you sure you want to reset {selected_user[4]}'s password?")
    choice = input("Enter 'y' to reset or 'n' to cancel: ")
    while choice not in ["y", "n"]:
        print("Enter a valid choice")
        choice = input("Enter 'y' to reset or 'n' to cancel: ")
    
    if choice == "y":
        new_password = generate_password()
        print(f"password is now: {new_password}")
        db.reset_user_pass(encrypt(new_password, secret.SECRET_KEY), selected_user[0])
        print("Password reset")

    elif choice == "n":
        print("Canceled")

    else:    
        print("Invalid choice")


