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