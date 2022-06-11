from utils.database import connect_db, commit_and_close
from utils.encryption import decrypt_log_from_tuple
from utils.logging import check_notifications, log_log_view
from utils.encryption import encrypt
import secret
from utils.bcolors import *

def view_all_logs():
    # Logs current activity
    log_log_view()

    connection, cursor = connect_db()

    all_encrypted_logs = cursor.execute("SELECT * FROM LOGS")

    # Creates a new list and adds all the logs in it after decrypting
    all_decrypted_logs = []
    for enc_log_tuple in all_encrypted_logs:
        all_decrypted_logs.append(decrypt_log_from_tuple(enc_log_tuple))

    connection.close()

    # Prints all the logs
    print_logs(all_decrypted_logs)

def view_unread_flagged_logs():
    # Logs current activity
    log_log_view(True)

    connection, cursor = connect_db()

    # Gets all the unread flagged logs from the database
    all_unread_flagged_logs = cursor.execute("SELECT * FROM LOGS WHERE NOT Read AND Suspicious = ?", (encrypt("Yes", secret.SECRET_KEY),)).fetchall()

    # Creates a new list and adds all the logs in it after decrypting
    all_decrypted_logs = []
    for enc_log_tuple in all_unread_flagged_logs:
        all_decrypted_logs.append(decrypt_log_from_tuple(enc_log_tuple))

    print_logs(all_decrypted_logs)

    # Updates all the suspicious logs to read
    cursor.execute("UPDATE LOGS SET Read = True WHERE NOT Read AND Suspicious = ?", (encrypt("Yes", secret.SECRET_KEY),))

    commit_and_close(connection)

def view_log_options():
    # If there are notifications, we'd like to ask the admin if they wish to see the unread suspicious logs
    if check_notifications():
        print("\nPress 1 to view all the log(s)")
        print("Press 2 to view only the unread suspicious log(s)")
        print("Press 3 to go back")

        while True:
            user_input = input("\nEnter your option: ")
            if user_input == "1":
                return view_all_logs()
            elif user_input == "2":
                return view_unread_flagged_logs()
            elif user_input == "3":
                return
            else:
                print(f"{bcolors.FAIL}Incorrect input, please try again{bcolors.ENDC}\n")
                continue
    else:
        view_all_logs()

def print_logs(list_of_logs: list):
    print("Printing logs...")
    print('Log Id', 'Username', 'Date', 'Time', 'Description of Activity', 'Additional Information', 'Suspicious', sep=" | ")
    for decr_log_tuple in list_of_logs:
        print(decr_log_tuple[0], decr_log_tuple[1], decr_log_tuple[2], decr_log_tuple[3], decr_log_tuple[4], decr_log_tuple[5], decr_log_tuple[6], sep=" | ")