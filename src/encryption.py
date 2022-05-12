import string
import random

'''
caesar cipher
completely stolen btw
maybe we should write our own encryption, let's discuss that later
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
 
#check the above function

#testcase to check encryption

#text = "PYXIS"
#s = 4
#print ("Text  : " + text)
#print ("Shift : " + str(s))
#print ("Cipher: " + encrypt(text,s))
