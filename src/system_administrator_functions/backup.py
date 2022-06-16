from zipfile import ZipFile
from utils.logging import log_backup
from models.enums import log_backup_options
from utils.bcolors import *

def show_options():
    print("\nPress 1 to create a backup")
    print("Press 2 to restore a backup")
    print("Press 3 to go back")

    while True:
        user_option = input("\nEnter your option: ")

        # Create backup
        if user_option == "1":
            create_backup()
            return

        # Restore backup
        elif user_option == "2":
            restore_backup()
            return

        # Go back to previous page (main page)
        elif user_option == "3":
            return

        else: 
            print(f"{bcolors.FAIL}Incorrect input, please try again{bcolors.ENDC}\n")
            continue

def create_backup():
    # Creates the backup.zip file if it doesn't exist yet, and if it exists, overwrites everything that's in the zip
    try:
        with ZipFile('data/backup.zip', 'w') as backup_zip:
            # Adds the database to the backup zip
            backup_zip.write('data/pythonsqlite.db')
    except:
        with ZipFile('../data/backup.zip', 'w') as backup_zip:
            # Adds the database to the backup zip
            backup_zip.write('../data/pythonsqlite.db')
            
    # Logs the backup creation
    log_backup(log_backup_options.CREATION)

    print(f"{bcolors.OKBLUE}\nBackup has been successfully made\n{bcolors.ENDC}")

def restore_backup():
    try:
        # Extracts the database file and overwrites it
        with ZipFile('data/backup.zip', 'r') as backup_zip:
            backup_zip.extractall()

        # Logs the backup restoration
        log_backup(log_backup_options.RESTORATION)

        print(f"{bcolors.OKBLUE}\nBackup has been successfully restored\n{bcolors.ENDC}")

    except Exception as exc:
        print(f"{bcolors.FAIL}Restoring from backup failed.\nError: {exc}{bcolors.ENDC}")