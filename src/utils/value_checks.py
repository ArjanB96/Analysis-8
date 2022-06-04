def is_valid_mail(email):
    '''
    Checks if given email is valid and follows the format
    '''
    if email.count("@") == 1 and email.count(".") == 1:
        return True
    else:
        print("Invalid email, try again")
        return False

def is_valid_phonenumber(mobile_phone):
    if len(mobile_phone) == 8:
        return True
    else:
        print("Invalid phonenumber, try again")
        return False


def is_valid_house_number(house_number):
    if len(house_number) < 10 and house_number.isdigit():
        return True
    else:
        print("Invalid housenumber, try again")
        return False

def is_valid_name(name):
    if name != "" and len(name) <= 25:
        return True
    else:
        print("Invalid first name, try again")
        return False

def is_valid_street(street):
    if street != "" and len(street) <= 40:
        return True
    else:
        print("Invalid street, try again")
        return False

def is_valid_zip_code(zip_code):
    # if length = 6 and first 4 digits are numbers and last 2 digits are letters
    if len(zip_code) == 6 and zip_code[0:4].isdigit() and zip_code[4:6].isalpha():
        return True
    else:
        print("Invalid zip code, try again")
        return False