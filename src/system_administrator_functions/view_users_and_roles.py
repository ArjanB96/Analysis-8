import globals
from utils.encryption import encrypt
import utils.value_checks as value_checks, secret
import utils.database as db
from models.enums import authentication_level

def view_users_and_roles():

    users_decrypted = db.view_users_and_roles()

    if len(users_decrypted) == 0:
        print("\nNo users found\n")
        return
    else:
        print("Following user(s) were found: \n")

        # print the username, first name, last name, email, role, and status
        for i in range(len(users_decrypted)):
            # convert enum to string
            print("_________________________________________")
            print(f"Username: {users_decrypted[i][4]}")
            print(f"First Name: {users_decrypted[i][2]}")
            print(f"Last Name: {users_decrypted[i][3]}")

            if users_decrypted[i][1] == 1:
                role = "Advisor"
            elif users_decrypted[i][1] == 2:
                role = "System Administrator"
            elif users_decrypted[i][1] == 3:
                role = "Super Administrator"

            print(f"Role: {role}")


    return users_decrypted


    

