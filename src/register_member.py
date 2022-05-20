from datetime import datetime
import functions, encryption
import database as db

'''
This is to register members. NOTE: members don't need a username/password as far as I know
'''

def register_member():
    #ask for first name, can not be empty
    #we have to think about how many characters we can have (to store in DB aswell) 25 for now
    first_name = input("Enter your first name: ")
    while not functions.is_valid_name(first_name):
        first_name = input("First name can not be empty. Enter your first name: ")
    
    #ask for last name, can not be empty
    #we have to think about how many characters we can have (to store in DB aswell) 25 for now
    last_name = input("Enter your last name: ")
    while not functions.is_valid_name(last_name):
        last_name = input("Last name can not be empty. Enter your last name: ")

    #ask for street, can not be empty
    #we have to think about how many characters we can have (to store in DB aswell) 40 for now
    street = input("Enter your street: ")
    while not functions.is_valid_street(street):
        street = input("Street can not be empty. Enter your street: ")

    #ask for house number
    #we have to think about how many characters we can have (to store in DB aswell) 10 for now
    house_number = input("Enter house number: ")
    while not functions.is_valid_house_number(house_number):
        house_number = input("Enter house number: ")

    #ask for zip code, can only be 6 length
    zip_code = input("Enter zip code: ")
    while not functions.is_valid_zip_code(zip_code):
        zip_code = input("Enter zip code: ")

    #ask for city (i'm not sure what the assignment means with 10 generated city names?)
    #we should write a validation if we make sure that we know what the assignment wants
    city = input("Enter city: ")

    #ask for email, it's checking if there's a '@' and a '.' in the email address
    email = input("Enter email: ")
    while not functions.is_valid_mail(email):
        email = input("Enter email: ")

    # check if the phone number is only 8 digits else try again
    mobile_phone = input("Enter mobile phone: ")
    while not functions.is_valid_phonenumber(mobile_phone):
        mobile_phone = input("Enter last 8 digits of mobile phone number (+31-6-DDDDDDDD): ")

    # automatically add current date as registration date
    registration_date = str(datetime.today())

    # generate a checksum id, including the checksum etc.
    checksum_id = functions.generate_checksum_id()

    # testing to encrypt email address, seems to work for now
    # we have to encrypt more things later on
    email_enc = encryption.encrypt(email, 1)

    # I'm sending the encrypted email to the database, but we should check what we are going encrypt and what not
    db.enter_data(checksum_id, first_name, last_name, street, house_number, zip_code, city, email_enc, mobile_phone, registration_date)
    print("Member registered")


