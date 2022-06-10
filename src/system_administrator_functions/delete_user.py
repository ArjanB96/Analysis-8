from system_administrator_functions import update_user_info as ua
import utils.database as db

def delete_user(role):
    if role == "advisor":
        selected_user = ua.get_user_info("advisor")
    elif role == "admin":
        selected_user = ua.get_user_info("admin")

    if selected_user != None:
        print(f"Are you sure you want to delete {selected_user[4]}?")
        choice = input("Enter 'y' to delete or 'n' to cancel: ")
        while choice not in ["y", "n"]:
            print("Enter a valid choice")
            choice = input("Enter 'y' to delete or 'n' to cancel: ")

        if choice == "y":
            db.delete_user(selected_user[0])
            if role == "advisor":
                print("Advisor deleted")
            elif role == "admin":
                print("Admin deleted")

        elif choice == "n":
            print("Canceled")

        else:
            print("Invalid choice")

