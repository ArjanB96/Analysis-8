import re
import utils.database as db

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
    '''
    ○ First digit can not be a 0
    ○ Second 3 digits can be 0-9
    ○ Last 2 letters can't be 'sa', 'sd' or 'ss' (due to the world war 2)
    ○ zip_code must be length 6 (or 7 if there's a space between the first 4 digits and the last 2 letters)

    '''
    regex = r'^[1-9][0-9]{3} ?(?!sa|sd|ss|SA|SD|SS|sA|sD|sS|Sa|Sd|Ss)[a-zA-Z]{2}$'
    if re.fullmatch(regex, zip_code):
        return True
    print("Invalid zip code, try again")
    return False

def is_valid_city(city):
    # if city is an integer >=1 and <=10 return True
    
    if city.isdigit() and int(city) in range(1, 11):
        return True
    print("Invalid city, try again")
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

def is_valid_member_id(member_id):
    '''
    This function checks if the member_id is valid.
    The member_id: 
    ○ must be an integer
    ○ can't start with 0
    ○ must be exactly 10 random digits
    ○ last digit on the right is a checksum which must be equal to the remainder of the sum of the first 9 digits by 10
    ○ can not be a duplicate
    '''
    all_member_ids = db.check_all_member_ids()

    # count first 9 digits
    sum = 0
    for i in range(len(member_id)):
        if i < 9:
            sum += int(member_id[i])
        else:
            break

    regex = r'^[1-9][0-9]{9}$'
    if re.fullmatch(regex, member_id) and sum % 10 == int(member_id[9]):
        if int(member_id) not in all_member_ids:
            return True
        elif int(member_id) in all_member_ids:
            print("Member id already exists, try again")
            return False
        else:
            print("Invalid member id, try again")
            return False

def is_valid_registration_date(registration_date):
    '''
    This function checks if the registration_date is valid.
    The registration_date: 
    ○ must be a string of the format YYYY-MM-DD
    ○ must be a valid date
    ○ example: 2022-06-06 13:40:36.916598
    '''
    regex = r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{6}$'
    if re.fullmatch(regex, registration_date):
        return True
    print("Invalid registration_date, try again")
