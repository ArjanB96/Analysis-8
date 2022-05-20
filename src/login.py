def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "admin":
        print("Welcome admin!")
        return "super_administrator"


'''
still to do:
    - integrate with DB

if login = advisor, return "advisor"
if login = _administator, return "system_administator"
if login = super_administrator, return "super_administrator"
'''