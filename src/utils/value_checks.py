import re

def is_valid_mail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    print("Invalid email, please try again")
    return False

def is_valid_phonenumber(phone_number):
    regex = r'[0-9]{8}'
    if re.fullmatch(regex, phone_number):
        return True
    print("Invalid phone number, please try again")
    return False

def is_valid_house_number(house_number):
    # Has to start with a digit which can't be 0. At most 5 digits and 2 optional letters from a-z (lower or uppercase)
    regex = r'^[1-9][0-9]{,4}([a-zA-Z]{,2})?$'
    if re.fullmatch(regex, house_number):
        return True
    print("Invalid house number, please try again")
    return False

def is_valid_name(name):
    if name != "" and len(name) <= 25:
        return True
    print("Invalid first name, try again")
    return False

def is_valid_street(street):
    if street != "" and len(street) <= 40:
        return True
    print("Invalid street, try again")
    return False

def is_valid_zip_code(zip_code):
    regex = r'^[1-9][0-9]{3} ?(?!sa|sd|ss)[a-z]{2}$/i'
    if re.fullmatch(regex, zip_code):
        return True
    print("Invalid zip code, try again")
    return False