from models.enums import log_lookup_options
import utils.database as db
from utils.logging import log_lookup
from utils.bcolors import *

def search_member_information():

    members_decrypted = db.show_all_members()

    if len(members_decrypted) == 0:
        print(f"{bcolors.FAIL}\nNo members found\n{bcolors.ENDC}")
        return

    # search for a member with a keyword, e.g. first name, last name, email, etc.
    keyword = input("Enter a keyword to search for: ").lower()

    # Logs current activity
    log_lookup(log_lookup_options.MEMBER, keyword)

    # if keyword matches with any of the members_decrypted, put that member in a list
    i = 0
    found_members = []
    while i < len(members_decrypted):
        if keyword in str(members_decrypted[i][0]).lower() or keyword in members_decrypted[i][1].lower() or keyword in members_decrypted[i][2].lower() or keyword in members_decrypted[i][3].lower() or keyword in str(members_decrypted[i][4]).lower() or keyword in members_decrypted[i][5].lower() or keyword in members_decrypted[i][6].lower() or keyword in members_decrypted[i][7].lower() or keyword in str(members_decrypted[i][8]).lower() or keyword in members_decrypted[i][9].lower():
            found_members.append(members_decrypted[i])
        i += 1

    # if no members were found, print that no members were found
    if len(found_members) == 0:
        print(f"{bcolors.FAIL}No members were found{bcolors.ENDC}")
        return

    #if members were found, print them        
    else:
        print("Following member(s) were found: \n")
        # print found members with a number
        for i in range(len(found_members)):
            print(f"{i}: {found_members[i]}")

    return found_members


    

