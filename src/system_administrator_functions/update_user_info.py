import utils.database as db
import utils.value_checks as value_checks
import secret
from utils.encryption import encrypt

def get_user_info(role):

    advisors_decrypted = db.view_users_and_roles("advisor")
    admins_decrypted = db.view_users_and_roles("admin")
    all_decrypted = db.view_users_and_roles("all")

    if role == "advisor":
        if advisors_decrypted == None or len(advisors_decrypted) == 0:
            print("\nNo advisors found")
            return

        #if advisors were found, print them        
        else:
            print(f"Following advisor(s) were found: \n")
            # print found advisors/admins with a number
            for i in range(len(advisors_decrypted)):
                print(f"{i}: {advisors_decrypted[i]}")

        # select an advisor
        while True:
            try:
                advisor_index = int(input("\nSelect an advisor: "))
                if advisor_index < len(advisors_decrypted) and advisor_index >= 0:
                    break
            except ValueError:
                print("\nInvalid input, try again")
                continue
            print("\nInvalid input, try again")

        # selected user is
        selected_user = advisors_decrypted[advisor_index]
        print(f"The selected advisor is {selected_user} \n")

    elif role == "admin":
        if admins_decrypted == None or len(admins_decrypted) == 0:
            print("\nNo admins found")
            return

        #if admins were found, print them
        else:
            print(f"Following admin(s) were found: \n")

            # print found advisors/admins with a number
            for i in range(len(admins_decrypted)):
                print(f"{i}: {admins_decrypted[i]}")

        # select an admin
        while True:
            try:
                admin_index = int(input("\nSelect an admin: "))
                if admin_index < len(admins_decrypted) and admin_index >= 0:
                    break
            except ValueError:
                print("\nInvalid input, try again")
                continue
            print("\nInvalid input, try again")

        # selected user is
        selected_user = admins_decrypted[admin_index]
        print(f"The selected admin is {selected_user} \n")

    return selected_user

def update_user_info(role):
    if role == "advisor":
        selected_user = get_user_info("advisor")
    elif role == "admin":
        selected_user = get_user_info("admin")
    
    if selected_user == None:
        return
        
    print_update_info()
    
    choice = input(f"\nEnter a number to edit a member's information: ")
    while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\nEnter a valid integer number representing a choice")
        choice = input(f"\nEnter a number to edit a member's information: ")
   
    # new id
    if choice == "1":
        new_employee_id = input("Enter new employee id: ")
        while not value_checks.is_valid_employee_id(new_employee_id):
            new_employee_id = input("Enter new employee_id: ")
        db.update_user(new_employee_id, role, encrypt(selected_user[2], secret.SECRET_KEY), 
        encrypt(selected_user[3], secret.SECRET_KEY), encrypt(selected_user[4], secret.SECRET_KEY), encrypt(selected_user[5], secret.SECRET_KEY), 
        selected_user[6], selected_user[0])
        print("Employee_id updated")
    

    # new first name
    elif choice == "2":
        new_first_name = input("Enter new first name: ")
        while not value_checks.is_valid_name(new_first_name):
            new_first_name = input("Enter new first name: ")
        db.update_user(selected_user[0], role, encrypt(new_first_name, secret.SECRET_KEY), encrypt(selected_user[3], 
        secret.SECRET_KEY), encrypt(selected_user[4], secret.SECRET_KEY), encrypt(selected_user[5], secret.SECRET_KEY),
        selected_user[6], selected_user[0])
        print("First name updated")

    # new last name
    elif choice == "3":
        new_last_name = input("Enter new last name: ")
        while not value_checks.is_valid_name(new_last_name):
            new_last_name = input("Enter new last name: ")
        db.update_user(selected_user[0], role, encrypt(selected_user[2], secret.SECRET_KEY), encrypt(new_last_name,
        secret.SECRET_KEY), encrypt(selected_user[4], secret.SECRET_KEY), encrypt(selected_user[5], secret.SECRET_KEY), selected_user[6], selected_user[0])
        print("Last name updated")
    
    # new username
    elif choice == "4":
        print("The user name must unique and can not be longer than 10 characters")
        new_username = input("Enter new username: ")
        while not value_checks.is_valid_username(new_username):
            new_username = input("Enter new username: ")
        db.update_user(selected_user[0], role, encrypt(selected_user[2], secret.SECRET_KEY), encrypt(selected_user[3],
        secret.SECRET_KEY), encrypt(new_username, secret.SECRET_KEY), encrypt(selected_user[5], secret.SECRET_KEY), selected_user[6], selected_user[0])
        print("Username updated")
    
    # new password
    elif choice == "5":
        new_password = input("Enter new password: ")
        while not value_checks.is_valid_password(new_password):
            print("Password not following the requirements, try again")
            new_password = input("Enter new password: ")
        db.update_user(selected_user[0], role, encrypt(selected_user[2], secret.SECRET_KEY), encrypt(selected_user[3],
        secret.SECRET_KEY), encrypt(selected_user[4], secret.SECRET_KEY), encrypt(new_password, secret.SECRET_KEY), selected_user[6], selected_user[0])
        print("Password updated")
    
    # new registration date
    elif choice == "6":
        new_registration_date = input("Enter new registration date: ")
        while not value_checks.is_valid_registration_date(new_registration_date):
            new_registration_date = input("Enter new registration date: ")  
        db.update_user(selected_user[0], role, encrypt(selected_user[2], secret.SECRET_KEY), encrypt(selected_user[3],
        secret.SECRET_KEY), encrypt(selected_user[4], secret.SECRET_KEY), encrypt(selected_user[5], secret.SECRET_KEY), new_registration_date, selected_user[0])
        print("Registration date updated")

    # exit
    elif choice == "7":
        return

def print_update_info():
    print("1. Edit employee id")
    print("2. Edit first name")
    print("3. Edit last name")
    print("4. Edit username")
    print("5. Edit password")
    print("6. Edit registration_date")
    print("7. Exit")