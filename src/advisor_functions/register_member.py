from datetime import datetime
from models.enums import log_user_options
import utils.value_checks as value_checks, secret
from utils.encryption import encrypt
import utils.database as db
from utils.checksum import generate_checksum_id
from utils.logging import log_member
from utils.bcolors import *

def register_member():
    
    # first name
    first_name = input("Enter your first name: ")
    while not value_checks.is_valid_name(first_name):
        first_name = input("First name can not be empty. Enter your first name: ")
    first_name_enc = encrypt(first_name, secret.SECRET_KEY)
    
    # last name
    last_name = input("Enter your last name: ")
    while not value_checks.is_valid_name(last_name):
        last_name = input("Last name can not be empty. Enter your last name: ")
    last_name_enc = encrypt(last_name, secret.SECRET_KEY)

    # street
    street = input("Enter your street: ")
    while not value_checks.is_valid_street(street):
        street = input("Street can not be empty. Enter your street: ")
    street_enc = encrypt(street, secret.SECRET_KEY)

    # house number
    house_number = input("Enter house number: ")
    while not value_checks.is_valid_house_number(house_number):
        house_number = input("Enter house number: ")
    house_number_enc = encrypt(house_number, secret.SECRET_KEY)

    # zip code
    zip_code = input("Enter zip code: ")
    while not value_checks.is_valid_zip_code(zip_code):
        zip_code = input("Enter zip code: ")
    zip_code_enc = encrypt(zip_code, secret.SECRET_KEY)

    # a function to choose city to re-use it in changing information
    city = choose_city()
    
    # email
    email = input("Enter email: ")
    while not value_checks.is_valid_mail(email):
        email = input("Enter email: ")
    email_enc = encrypt(email, secret.SECRET_KEY)

    # phone number
    mobile_phone = input("Enter mobile phone: ")
    while not value_checks.is_valid_phonenumber(mobile_phone):
        mobile_phone = input("Enter last 8 digits of mobile phone number (+31-6-DDDDDDDD): ")
    mobile_phone_enc = encrypt(mobile_phone, secret.SECRET_KEY)

    # automatically add current date as registration date
    registration_date = str(datetime.today())

    # generate a checksum id, including the checksum etc.
    checksum_id = generate_checksum_id()

    # Encrypting first name, last name, street, house number, zip code, city, email, mobile phone
    db.insert_member(checksum_id, first_name_enc, last_name_enc, street_enc, house_number_enc, zip_code_enc, city, email_enc, mobile_phone_enc, registration_date)

    # Logs the member creation
    log_member(log_user_options.CREATION)

    print(f"{bcolors.OKBLUE}\nMember registered{bcolors.ENDC}\n")

def choose_city():
        print("\nChoose your city:\n")
        list_of_cities = ["Rotterdam", "Dordrecht", "Zwijndrecht", "Papendrecht", "Ridderkerk", "Barendrecht", "Amsterdam", "Den Haag", "Leiden", "Utrecht"]
        i = 0
        while i < len(list_of_cities):
            print(i + 1, ":", list_of_cities[i])
            i += 1
        city = input("\nEnter the number of your city: ")
        while not value_checks.is_valid_city(city):
            city = input(f"{bcolors.FAIL}Enter the number of your city: {bcolors.ENDC}")
        print(city)
        city = encrypt(list_of_cities[int(city)-1], secret.SECRET_KEY)
        return city