import random
import re 

'''creates a random checksum id that can't start with 0 and is a string of 10 random digits. 
The last digit on the right is a checksum which must be equal to the remainder of the sum of the first 9 digits by 10
'''
def generate_checksum_id():
    checksum_id = str(random.randint(1, 9))
    for i in range(8):
        checksum_id += str(random.randint(0, 9))

    sum = 0
    for i in range(len(checksum_id)):
        sum += int(checksum_id[i])

    checksum_id += str(sum % 10)

    return checksum_id

#checks if given email is valid and following the format
def is_valid_mail(email):
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