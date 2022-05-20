import register_member

def advisor():
    print_advisor_choices()
    print("Press 5 to exit")
    advisor_choices()

def system_administator():
    print_advisor_choices()
    print_system_administator_choices()
    print("Press 16 to exit")


def super_administrator():
    print_advisor_choices()
    print_system_administator_choices()
    print_super_administrator_choices()


def print_advisor_choices():
    print("Press 1 to update password")
    print("Press 2 to add new member")
    print("Press 3 to modify or update information of a member")
    print("Press 4 to search and retrieve the information of a member")

def print_system_administator_choices():
    print("Press 5 to check the list of users and their roles")
    print("Press 6 to define and add a new advisor to the system")
    print("Press 7 to modify or update an existing advisor's account and profile")
    print("Press 8 to delete an existing advisor's account")
    print("Press 9 to reset an existing advisor's password (a temporary password)")
    print("Press 10 to make a backup of the system and restore a backup")
    print("Press 11 to see the logs file(s) of the system")
    print("Press 12 to add a new member to the system")
    print("Press 13 to modify or update the information of a member in the system")
    print("Press 14 to delete a member's record from the database")
    print("Press 15 to search and retrieve the information of a member")

def print_super_administrator_choices():
    print("Press 16 to define and add a new admin to the system")
    print("Press 17 to modify or update an existing admin's account and profile")
    print("Press 18 to delete an existing admin's account")
    print("Press 19 to reset an existing admin's password (a temporary password")
    print("Press 20 to exit")

def advisor_choices():
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Update password")
        elif choice == "2":
            print("Add new member")
            register_member.register_member()
        elif choice == "3":
            print("Modify or update information of a member")
        elif choice == "4":
            print("Search and retrieve the information of a member")
        elif choice == "5":
            break
        else:
            print("Please enter a valid choice")
        continue