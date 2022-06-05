import globals
from utils.encryption import encrypt
import utils.value_checks as value_checks, secret

def update_password():
    print("Update password")
    old_password = input("Enter old password: ") 
    old_password_enc = encrypt(old_password, secret.SECRET_KEY)

    while not globals.current_user.password == old_password_enc:
        print("Incorrect password")
        old_password = input("Enter old password: ") 

    print("\nPassword has to follow the following rules:")
    print("* Must be at least 8 characters long")
    print("* Must contain at least one uppercase letter")
    print("* Must contain at least one lowercase letter")
    print("* Must contain at least one number")
    print("* Must contain at least one special character")
    print("* Must not contain any spaces\n")

    new_password = input("Enter new password: ")
    new_password_confirm = input("Confirm new password: ")

    while not value_checks.is_valid_password(new_password):
        new_password = input("Enter new password: ") 
        new_password_confirm = input("Confirm new password: ")

    while new_password != new_password_confirm:
        print("Passwords do not match, try again")
        new_password = input("Enter new password: ") 
        new_password_confirm = input("Confirm new password: ")

    print(f"new password is: {new_password}")
    new_password_enc = encrypt(new_password, secret.SECRET_KEY)
    print(f"new password encrypted is: {new_password_enc}")
    #new_password_enc = encrypt(new_password, secret.SECRET_KEY)
    #globals.current_user.password = new_password_enc
    print("Password updated")

    #print(f"Current: {globals.current_user.password}")
    return