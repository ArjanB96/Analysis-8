import random
import register_member, database

'''
Did not touch this so far :P
'''

while True:
    print("Press 1 to enter new member")
    print("Press 2 to see all members")
    print("Press 3 to exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        register_member.register_member()
    elif choice == "2":
        print("All members:")
    elif choice == "3":
        break
    else:
        print("Please enter a valid choice")
        continue

