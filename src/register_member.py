from datetime import datetime
import functions, encryption
import database as db

'''
This is to register members. NOTE: members don't need a username/password as far as I know
'''

def register_member():
    #ask for first name, can not be empty
    first_name = input("Enter your first name: ")
    while first_name == "":
        first_name = input("First name can not be empty. Enter your first name: ")
    
    #ask for last name, can not be empty
    last_name = input("Enter your last name: ")
    while last_name == "":
        last_name = input("Last name can not be empty. Enter your last name: ")

    #ask for street, can not be empty
    street = input("Enter your street: ")
    while street == "":
        street = input("Street can not be empty. Enter your street: ")

    #ask for house number (not sure if we want to do this isdigit() check, since housenumbers can be: 1a, 1b etc.)
    house_number = input("Enter house number: ")
    while not house_number.isdigit():
        house_number = input("Enter house number: ")

    #ask for zip code, can only be 6 length
    zip_code = input("Enter zip code: ")
    while len(zip_code) != 6:
        zip_code = input("Enter zip code: ")

    #ask for city (i'm not sure what the assignment means with 10 generated city names?)
    city = input("Enter city: ")

    #ask for email, it's checking if there's a '@' and a '.' in the email address
    email = input("Enter email: ")
    while not email.count("@") == 1 or not email.count(".") == 1:
        email = input("Enter email: ")

    #ask for mobile phone (+31-6-DDDDDDDD)  only DDDDDDDD to be entered by the user.
    # check if the phone number is only 8 digits else try again
    while True:
        mobile_phone = input("Enter last 8 digits of mobile phone number (+31-6-DDDDDDDD): ")
        if len(mobile_phone) == 8:
            break       
        else:
            print("Please enter a valid phone number, only the 8 digits after +31-6-")
            continue

    # automatically add current date as registration date
    registration_date = str(datetime.today())

    checksum_id = functions.generate_checksum_id()

    # encrypt the phone number and adress details
    # testing with email for now
    email_enc = encryption.encrypt(email, 1)

    # I'm sending the encrypted email to the database, but we should check what we are going encrypt and what not
    db.enter_data(checksum_id, first_name, last_name, street, house_number, zip_code, city, email_enc, mobile_phone, registration_date)
    print("Member registered")


