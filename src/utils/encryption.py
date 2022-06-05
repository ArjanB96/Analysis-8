import datetime
import re
from unittest import result
import secret

'''
Encryption & Decryption
'''

def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]

        # encrypt special 
        if ord(char) in range(33,48): 
            result += chr((ord(char) + s-33) % 15 + 33)

        # Encrypt digits
        elif (char.isdigit()):
            result += chr((ord(char) + s-48) % 10 + 48)

        # Encrypt uppercase
        elif (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
def decrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]

        # Decrypt special 
        if ord(char) in range(33,48): 
            result += chr((ord(char) - s-33) % 15 + 33)


        # Decrypt digits
        elif (char.isdigit()):
            result += chr((ord(char) - s-48) % 10 + 48)

        # Decrypt uppercase 
        elif (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        # Decrypt lowercase 
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result

def decrypt_employee(employee: tuple):
    return de_or_encrypt_employee(employee, decrypt)

def encrypt_employee(employee: tuple):
    return de_or_encrypt_employee(employee, encrypt)

def de_or_encrypt_employee(employee: tuple, function: object):
    result = (
        employee[0],                                        # employee_id
        int(function(str(employee[1]), secret.SECRET_KEY)),  # authentication_level
        function(employee[2], secret.SECRET_KEY),            # first_name
        function(employee[3], secret.SECRET_KEY),            # last_name
        function(employee[4], secret.SECRET_KEY),            # username
        function(employee[5], secret.SECRET_KEY),            # password
        employee[6]                                         # registration_date
    )
    return result