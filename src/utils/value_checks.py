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
    if len(house_number) < 10 and house_number.isdigit():
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
    regex = r'^[1-9][0-9]{3} ?(?!sa|sd|ss)[a-z]{2}$i'
    if re.fullmatch(regex, zip_code):
        return True
    print("Invalid zip code, try again")
    return False

def is_valid_password(password):
    #regex atleast 8 characters, atleast 1 number, atleast 1 lowercase letter, atleast 1 special character and atleast 1 uppercase letter at most 30 characters
    regex = r'^((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{8,30})'
    
    if re.fullmatch(regex, password):
        return True
    else:
        print("Password not following the requirements, try again")
        return False

