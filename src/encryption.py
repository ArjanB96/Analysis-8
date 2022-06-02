import string
import random

'''
caesar cipher
completely stolen btw
maybe we should write our own encryption, let's discuss that later

we still need make a function to decrypt the message
+ 
we have to store the shift value in a secrets file so we can decrypt the message
'''

def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 