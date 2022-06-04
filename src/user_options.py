from authentication_level_enum import authentication_level
'''
Authentication_Level: 0 = member
Authentication_Level: 1 = advisor
Authentication_Level: 2 = system administrator
Authentication_Level: 3 = super administrator
'''

options_dict = {
    'Press 1 to update your password': 1,
    'Press 2 to add a new member': 1,
    'Press 3 to modify or update information of a member': 1,
    'Press 4 to search and retrieve information of a member': 1,
    'Press 5 to view the list of users and their roles': 2,
    'Press 6 to define and add a new advisor to the system': 2,
    'Press 7 to modify or update an existing advisor\'s account and profile': 2,
    'Press 8 to delete an existing advisor\'s account': 2,
    'Press 9 to reset an existing advisor\'s password (a temporary password)': 2,
    'Press 10 to make a backup of the system and restore a backup': 2,
    'Press 11 to see the logs of file(s) of the system': 2,
    'Press 12 to delete a member from the database': 2,
    'Press 13 to define and add a new administrator to the system': 3,
    'Press 14 to modify or update an existing administrator\'s account and profile': 3,
    'Press 15 to delete an existing administrator\'s account': 3,
    'Press 16 to reset an existing administrator\'s password (a temporary password)': 3,
    'Type \'exit\' to exit': 0
}

def show_options(auth_level):
    for key, value in options_dict.items():
        if (auth_level.value >= value):
            print(key)