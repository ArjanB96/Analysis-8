from random import choice
import utils.value_checks as value_checks

'''
    Create a random pass that:
        ○ must have a length of at least 8 characters
        ○ must be no longer than 30 characters
        ○ can contain letters (a-z), (A-Z), numbers (0-9), Special characters such as ~!@#$%&_-+=`|\(){}[]:;'<>,.?/
        ○ must have a combination of at least one lowercase letter, one uppercase letter, one digit, and one special character
        ○ can not contain spaces
'''

def generate_password():
    password = generate()

    while not value_checks.is_valid_password(password):
        password = generate()
    return password

def generate():
    password = ''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%&_-+=`|\'(){\}[]:;<>,.?/') for i in range(10)])
    return password
