from advisor_functions.search_member_information import search_member_information
import globals
from utils.encryption import encrypt
import utils.value_checks as value_checks
import secret
import utils.database as db
from advisor_functions import search_member_information
from advisor_functions.register_member import choose_city
from utils.bcolors import *

def delete_member():


    list_of_members = search_member_information.search_member_information()

    if list_of_members == None or len(list_of_members) == 0:
        return

    else:
        # enter a key to select a member from the list_of_members
        key = input("\nEnter a number to select a member to delete: ")

        # create an int to check if the key is an int
        try:
            key = int(key)
        except ValueError:
            print(f"{bcolors.FAIL}Incorrect input. Please try again{bcolors.ENDC}\n")
            return

        # if they key is in the range of list_of members
        while key not in range(len(list_of_members)):
            print(f"\n{bcolors.FAIL}Enter a valid integer number representing a member{bcolors.ENDC}")
            key = int(input(f"\n{bcolors.FAIL}Enter a number to select a member: {bcolors.ENDC}"))
        
        member = list_of_members[key]

        print(f"{bcolors.WARNING}Are you sure you want to delete the member: {member[1]} {member[2]}?{bcolors.ENDC}")
        choice = input("Enter 'y' to delete or 'n' to cancel: ")
        while choice not in ["y", "n"]:
            print(f"{bcolors.FAIL}Enter a valid choice{bcolors.ENDC}")
            choice = input("Enter 'y' to delete or 'n' to cancel: ")

        if choice == "y":
            db.delete_member(member[0])
            print(f"{bcolors.OKBLUE}Member deleted{bcolors.ENDC}")

        elif choice == "n":
            print(f"{bcolors.OKBLUE}Canceled{bcolors.ENDC}")

        else:
            print(f"{bcolors.OKBLUE}Invalid choice{bcolors.ENDC}")