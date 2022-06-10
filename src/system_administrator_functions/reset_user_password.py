from system_administrator_functions import update_user_info as ua
import utils.database as db
import secret
from utils.encryption import encrypt
from utils.random_pass_generator import generate_password
from utils.bcolors import *

def reset_user_password(role):
    if role == "advisor":
        selected_user = ua.get_user_info("advisor")
    elif role == "admin":
        selected_user = ua.get_user_info("admin")
    if selected_user != None:
        print(f"{bcolors.WARNING}Are you sure you want to reset {selected_user[4]}'s password?{bcolors.ENDC}")
        choice = input("Enter 'y' to reset or 'n' to cancel: ")
        while choice not in ["y", "n"]:
            print(f"{bcolors.FAIL}Enter a valid choice{bcolors.ENDC}")
            choice = input("Enter 'y' to reset or 'n' to cancel: ")
        
        if choice == "y":
            new_password = generate_password()
            print(f"{bcolors.OKBLUE}\npassword is now: {new_password}{bcolors.ENDC}")
            db.reset_user_pass(encrypt(new_password, secret.SECRET_KEY), selected_user[0])
            print(f"{bcolors.OKBLUE}Password reset{bcolors.ENDC}\n")

        elif choice == "n":
            print(f"{bcolors.OKBLUE}\nCanceled{bcolors.ENDC}\n")

        else:    
            print(f"{bcolors.OKBLUE}Invalid choice{bcolors.ENDC}\n")


