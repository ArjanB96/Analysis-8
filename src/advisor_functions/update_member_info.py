from advisor_functions.search_member_information import search_member_information
from models.enums import log_user_options
from utils.encryption import encrypt
import utils.value_checks as value_checks
import secret
import utils.database as db
from advisor_functions import search_member_information
from advisor_functions.register_member import choose_city
from utils.logging import log_member
from utils.bcolors import *

def update_member_info():

    list_of_members = search_member_information.search_member_information()

    if list_of_members == None or len(list_of_members) == 0:
        return

    else:
        # enter a key to select a member from the list_of_members
        key = input("\nEnter a number to select a member: ")

        # create an int to check if the key is an int
        try:
            key = int(key)
        except ValueError:
            print(f"{bcolors.FAIL}Incorrect input. Please try again{bcolors.ENDC}\n")
            return

        # if they key is in the range of list_of members
        while key not in range(len(list_of_members)):
            print("\nEnter a valid integer number representing a user")
            key = int(input(f"{bcolors.FAIL}\nEnter a number to select a member: {bcolors.ENDC}"))
        
        member = list_of_members[key]

        print(f"\nSelected member: {member}")

        print_update_info()
        choice = input(f"\nEnter a number to edit a member's information: ")
        while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            print(f"{bcolors.FAIL}\nEnter a valid integer number representing a choice{bcolors.ENDC}")
            choice = input(f"\nEnter a number to edit a member's information: ")
        
        # new member id
        if choice == "1":
            new_member_id = input("Enter new member_id: ")
            while not value_checks.is_valid_member_id(new_member_id):
                new_member_id = input("Enter new member_id: ")
            db.update_member(new_member_id, encrypt(member[1], secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY),encrypt(member[5], secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), member[9], member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"Member_Id": new_member_id})

            print(f"{bcolors.OKBLUE}\nMember_id updated{bcolors.ENDC}\n")
        
        # new first name
        elif choice == "2":
            new_first_name = input("Enter new first_name: ")
            while not value_checks.is_valid_name(new_first_name):
                new_first_name = input("Enter new first_name: ")
            db.update_member(member[0], encrypt(new_first_name, secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY),encrypt(member[5], secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), member[9], member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"First_Name": new_first_name})

            print(f"{bcolors.OKBLUE}\nFirst name updated{bcolors.ENDC}\n")
        
        # new last name
        elif choice == "3":
            new_last_name = input("Enter new last_name: ")
            while not value_checks.is_valid_name(new_last_name):
                new_last_name = input(f"Enter new last_name: ")
            db.update_member(member[0], encrypt(member[1], secret.SECRET_KEY), encrypt(new_last_name, secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY),encrypt(member[5], secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), member[9], member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"Last_Name": new_last_name})

            print(f"{bcolors.OKBLUE}\nLast_name updated{bcolors.ENDC}\n")
        
        # new street
        elif choice == "4":
            new_street = input("Enter new street: ")
            while not value_checks.is_valid_street(new_street):
                new_street = input("Enter new street: ")
            db.update_member(member[0], encrypt(member[1], secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(new_street, secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY),encrypt(member[5], secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), member[9], member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"Street": new_street})

            print(f"{bcolors.OKBLUE}\nStreet updated{bcolors.ENDC}\n")

        # new house number    
        elif choice == "5":
            new_house_number = input("Enter new house_number: ")
            while not value_checks.is_valid_house_number(new_house_number):
                new_house_number = input("Enter new house_number: ")
            db.update_member(member[0], encrypt(member[1], secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(new_house_number), secret.SECRET_KEY), encrypt(member[5], secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), member[9], member[0])
            
            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"House_Number": new_house_number})

            print(f"{bcolors.OKBLUE}\nHouse_number updated{bcolors.ENDC}\n")
        
        # new zip code
        elif choice == "6":
            new_zip_code = input("Enter new zip_code: ")
            while not value_checks.is_valid_zip_code(new_zip_code):
                new_zip_code = input("Enter new zip_code: ")
            db.update_member(member[0], encrypt(member[1], secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY), encrypt(new_zip_code, secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), member[9], member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"Zip_Code": new_zip_code})

            print(f"{bcolors.OKBLUE}\nZip code updated{bcolors.ENDC}\n")

        # new city
        elif choice == "7":
            new_city = choose_city()
            db.update_member(member[0], encrypt(member[1], secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY), encrypt(member[5], secret.SECRET_KEY), new_city, encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), member[9], member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"City": new_city})

            print(f"{bcolors.OKBLUE}\nCity updated{bcolors.ENDC}\n")

        # new email 
        elif choice == "8":
            new_email = input("Enter new email: ")
            while not value_checks.is_valid_mail(new_email):
                new_email = input("Enter new email: ")
            db.update_member(member[0], encrypt(member[1], secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY), encrypt(member[5], secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(new_email, secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), member[9], member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"Email": new_email})

            print(f"{bcolors.OKBLUE}\nEmail updated{bcolors.ENDC}\n")

        # new phone number
        elif choice == "9":
            new_phone_number = input("Enter new phone_number: ")
            while not value_checks.is_valid_phonenumber(new_phone_number):
                new_phone_number = input("Enter new phone number, we only accept the last 8 digits (e.g. +31-6-DDDDDDDD): ")
            db.update_member(member[0], encrypt(member[1], secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY), encrypt(member[5], secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(new_phone_number), secret.SECRET_KEY), member[9], member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"Phone_Number": new_phone_number})

            print(f"{bcolors.OKBLUE}\nPhone_number updated{bcolors.ENDC}\n")

        # new registration date
        elif choice == "10":
            print("example of registration date: 2022-06-06 13:40:36.916598")
            new_registration_date = input("Enter new registration_date: ")
            while not value_checks.is_valid_registration_date(new_registration_date):
                new_registration_date = input("Enter new new_registration_date_date: ")
            db.update_member(member[0], encrypt(member[1], secret.SECRET_KEY), encrypt(member[2], secret.SECRET_KEY), encrypt(member[3], secret.SECRET_KEY), 
            encrypt(str(member[4]), secret.SECRET_KEY), encrypt(member[5], secret.SECRET_KEY), encrypt(member[6], secret.SECRET_KEY), encrypt(member[7], secret.SECRET_KEY), 
            encrypt(str(member[8]), secret.SECRET_KEY), new_registration_date, member[0])

            # Logs the activity 
            log_member(log_user_options.MODIFIED, {"Registration_Date": new_registration_date})

            print(f"{bcolors.OKBLUE}\nRegistration date updated{bcolors.ENDC}\n")
            
        elif choice == "11":
            return
            
def print_update_info():
    print("1. Edit member id")
    print("2. Edit first name")
    print("3. Edit last name")
    print("4. Edit street")
    print("5. Edit house_number")
    print("6. Edit zip code")
    print("7. Edit city")
    print("8. Edit email")
    print("9. Edit phone number")
    print("10. Edit registration date")
    print("11. Exit")