import string
import random

'''
Encryption & Decryption
'''

def encrypt(text,s):
    result = ""
 
    for i in range(len(text)):
        char = text[i]

        # Encrypt digits
        if (char.isdigit()):
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
 
        # Decrypt digits
        if (char.isdigit()):
            result += chr((ord(char) - s-48) % 10 + 48)

        # Decrypt uppercase 
        elif (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        # Decrypt lowercase 
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result