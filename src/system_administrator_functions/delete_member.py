from advisor_functions.search_member_information import search_member_information
import globals
from utils.encryption import encrypt
import utils.value_checks as value_checks
import secret
import utils.database as db
from advisor_functions import search_member_information
from advisor_functions.register_member import choose_city

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
            print("Incorrect input. Please try again")
            return

        # if they key is in the range of list_of members
        while key not in range(len(list_of_members)):
            print("\nEnter a valid integer number representing a member")
            key = int(input("\nEnter a number to select a member: "))
        
        member = list_of_members[key]

        print(f"Are you sure you want to delete the member: {member[1]} {member[2]}?")
        choice = input("Enter 'y' to delete or 'n' to cancel: ")
        while choice not in ["y", "n"]:
            print("Enter a valid choice")
            choice = input("Enter 'y' to delete or 'n' to cancel: ")

        if choice == "y":
            db.delete_member(member[0])
            print("Member deleted")

        elif choice == "n":
            print("Canceled")

        else:
            print("Invalid choice")