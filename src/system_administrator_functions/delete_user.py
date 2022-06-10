from system_administrator_functions import update_user_info as ua
import utils.database as db
from utils.bcolors import *

def delete_user(role):
    if role == "advisor":
        selected_user = ua.get_user_info("advisor")
    elif role == "admin":
        selected_user = ua.get_user_info("admin")

    if selected_user != None:
        print(f"{bcolors.WARNING}Are you sure you want to delete {selected_user[4]}?{bcolors.ENDC}")
        choice = input("Enter 'y' to delete or 'n' to cancel: ")
        while choice not in ["y", "n"]:
            print(f"{bcolors.FAIL}Enter a valid choice{bcolors.ENDC}")
            choice = input("Enter 'y' to delete or 'n' to cancel: ")

        if choice == "y":
            db.delete_user(selected_user[0])
            if role == "advisor":
                print(f"{bcolors.OKBLUE}Advisor deleted{bcolors.ENDC}")
            elif role == "admin":
                print(f"{bcolors.OKBLUE}Admin deleted{bcolors.ENDC}")

        elif choice == "n":
            print(f"{bcolors.OKBLUE}Canceled{bcolors.ENDC}")

        else:
            print(f"{bcolors.OKBLUE}Invalid choice{bcolors.ENDC}")

