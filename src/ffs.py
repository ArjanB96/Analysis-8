import random
import register_member, database, choices, login

if __name__ == "__main__":
    
    while True:
        role = login.login()
        if role == "advisor":
            choices.advisor()
        elif role == "system_administrator":
            choices.system_administrator()
        elif role == "super_administrator":
            choices.super_administrator()
        else:
            print("Incorrect username or password")
            continue
        break
    

'''
advisors can:
- update their own password
add new member to the system
modify or update information of a member in the system
search and retrieve the information of a member
'''