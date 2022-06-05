import globals
from utils.encryption import encrypt
import utils.value_checks as value_checks, secret
import utils.database as db

def update_password():
    print("Update password")
    old_password = input("Enter old password: ") 

    # check if the old password is correct
    while not globals.current_user.password == old_password:
        print("Incorrect password")
        old_password = input("Enter old password: ") 

    # Display password rules in console
    password_rules()

    new_password = input("Enter new password: ")
    new_password_confirm = input("Confirm new password: ")

    # Check if the new password is valid
    while not value_checks.is_valid_password(new_password):
        new_password = input("Enter new password: ") 
        new_password_confirm = input("Confirm new password: ")

    # Check if the new password and the confirmation password are the same
    while new_password != new_password_confirm:
        print("Passwords do not match, try again")
        new_password = input("Enter new password: ") 
        new_password_confirm = input("Confirm new password: ")

    # Update the password in global current_user
    globals.current_user.password = new_password

    # Password to put in database is encrypted
    db.update_password(encrypt(globals.current_user.username, secret.SECRET_KEY), encrypt(new_password, secret.SECRET_KEY))

    print("Password updated")
    return

def password_rules():
    print("\nPassword has to follow the following rules:")
    print("* Must be at least 8 characters long")
    print("* Must contain at least one uppercase letter")
    print("* Must contain at least one lowercase letter")
    print("* Must contain at least one number")
    print("* Must contain at least one special character")
    print("* Must not contain any spaces\n")