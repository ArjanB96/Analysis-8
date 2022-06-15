from models.log_event import LogEvent
import secret

'''
Encryption & Decryption
'''

special_characters = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-','{','}','[',']','|',':',';','"','<','>',',','.','?','/','~','`',"'",' ']

def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]

        # if char is in special_characters, shift in the list of special characters
        if char in special_characters:
            result += special_characters[(special_characters.index(char) + s) % len(special_characters)]
  
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

        # if char is in special_characters, shift in the list of special characters
        if char in special_characters:
            result += special_characters[(special_characters.index(char) - s) % len(special_characters)]

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

def de_or_encrypt_employee(employee: tuple, function: object):
    result = (
        employee[0],                                         # employee_id
        int(function(str(employee[1]), secret.SECRET_KEY)),  # authentication_level
        function(employee[2], secret.SECRET_KEY),            # first_name
        function(employee[3], secret.SECRET_KEY),            # last_name
        function(employee[4], secret.SECRET_KEY),            # username
        function(employee[5], secret.SECRET_KEY),            # password
        employee[6],                                         # registration_date
        employee[7]                                          # changed_pass
    )
    return result

def de_or_encrypt_member(member: tuple, function: object):
    result = (
        member[0],                                         # member_id
        function(member[1], secret.SECRET_KEY),            # first_name
        function(member[2], secret.SECRET_KEY),            # last_name
        function(member[3], secret.SECRET_KEY),            # street
        int(function(str(member[4]), secret.SECRET_KEY)),  # house_number
        function(member[5], secret.SECRET_KEY),            # zip_code
        function(member[6], secret.SECRET_KEY),            # city
        function(member[7], secret.SECRET_KEY),            # email_address
        int(function(str(member[8]), secret.SECRET_KEY)),  # phone_number
        member[9]                                          # registration_date
        )
    return result

def decrypt_employee(employee: tuple):
    return de_or_encrypt_employee(employee, decrypt)

def encrypt_employee(employee: tuple):
    return de_or_encrypt_employee(employee, encrypt)

def encrypt_log(log_event: LogEvent):
    result = LogEvent(
        encrypt(log_event.username, secret.SECRET_KEY),                
        encrypt(log_event.description_of_activity, secret.SECRET_KEY), 
        encrypt(log_event.additional_information, secret.SECRET_KEY),
        encrypt(log_event.suspicious, secret.SECRET_KEY)
    )
    return result

def decrypt_log_from_tuple(log_event: tuple):
    result = (
        log_event[0],                               #Log_Id
        decrypt(log_event[1], secret.SECRET_KEY),   # Username
        log_event[2],                               # Date
        log_event[3],                               # Time
        decrypt(log_event[4], secret.SECRET_KEY),   # Description_Of_Activity
        decrypt(log_event[5], secret.SECRET_KEY),   # Additional_Information
        decrypt(log_event[6], secret.SECRET_KEY),   # Suspicious
        log_event[7]                                # Read
    )
    return result