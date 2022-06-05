from distutils.log import Log
from pydoc import describe
from models.log_event import LogEvent
import globals

def log_successful_login():
    if globals.current_user is None: 
        return
    username = globals.current_user.username
    description = "Logged in"
    suspicious = "No"

def log_unsuccessful_login(username):
    description = ""
    additional_info = ""
    suspicious = "Yes"

def log_login(successful = True, username=""):
    if successful:
        username = globals.current_user.username
        description = "Logged in"
        additional_info = ""
        suspicious = "No"
    else:
        description