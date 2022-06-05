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
    regex = r'^[1-9][0-9]{3} ?(?!sa|sd|ss)[a-z]{2}$/i'
    if re.fullmatch(regex, zip_code):
        return True
    print("Invalid zip code, try again")
    return False


def is_valid_password(password):
    '''
    This function checks if the password is valid.
    The password: 
    ○ must have a length of at least 8 characters
    ○ must be no longer than 30 characters
    ○ can contain letters (a-z), (A-Z), numbers (0-9), Special characters such as ~!@#$%&_-+=`|\(){}[]:;'<>,.?/
    ○ must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special character
    ○ can not contain spaces
    '''
    regex = r'^((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_])\S{8,30})'
    
    if re.fullmatch(regex, password):
        return True
    else:
        print("Password not following the requirements, try again")
        return False

