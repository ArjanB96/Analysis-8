import datetime

class LogEvent:
    def __init__(self, username, description_of_activity, additional_information, suspicious):
        self.number = 1
        self.username = username
        self.date = datetime.date.today().strftime("%d-%m-%Y")
        self.time = datetime.datetime.now().strftime("%H:%H:%S")
        self.description_of_activity = description_of_activity
        self.additional_information = additional_information
        self.suspicious = suspicious

# def log_login():
#     log_event = 