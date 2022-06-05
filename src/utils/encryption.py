import datetime
import re
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
    '''
    Given a tuple with encrypted values, returns a tuple with the decrypted values\n
    NOTE: the employee_id and registration_date will NOT be decrypted
    '''
    result = (
        employee[0],                                        # employee_id
        int(decrypt(str(employee[1]), secret.SECRET_KEY)),  # authentication_level
        decrypt(employee[2], secret.SECRET_KEY),            # first_name
        decrypt(employee[3], secret.SECRET_KEY),            # last_name
        decrypt(employee[4], secret.SECRET_KEY),            # username
        decrypt(employee[5], secret.SECRET_KEY),            # password
        employee[6]                                         # registration_date
    )
    
    return result