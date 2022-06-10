class User():
    def __init__(self, user_tuple: tuple):
        self.employee_id = user_tuple[0]
        self.authentication_level = user_tuple[1]
        self.firstname = user_tuple[2]
        self.lastname = user_tuple[3]
        self.username = user_tuple[4]
        self.password = user_tuple[5]
        self.registration_date = user_tuple[6]
        self.changed_pass = user_tuple[7]