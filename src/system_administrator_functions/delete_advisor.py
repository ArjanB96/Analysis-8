from models.enums import log_backup_options, log_user_options
from system_administrator_functions import update_advisor_info as ua
from utils.logging import log_user
import utils.database as db

def delete_advisor():

    selected_advisor = ua.get_advisor_info()

    print(f"Are you sure you want to delete {selected_advisor[4]}?")
    choice = input("Enter 'y' to delete or 'n' to cancel: ")
    while choice not in ["y", "n"]:
        print("Enter a valid choice")
        choice = input("Enter 'y' to delete or 'n' to cancel: ")

    if choice == "y":
        # if selected advisor authentication level is 2 or higher, the advisor cannot be deleted
        if selected_advisor[1] >= 2:
            print("You cannot delete an administrator or higher")
        elif selected_advisor[1] == 1:
            db.delete_advisor(selected_advisor[0])

            # Logs the advisor's deletion
            log_user(log_user_options.DELETION, selected_advisor[4], selected_advisor[1])

            print("Advisor deleted")

    elif choice == "n":
        print("Canceled")

    else:
        print("Invalid choice")
