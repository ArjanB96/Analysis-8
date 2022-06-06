from models.user import User

# current_user object
current_user : User = None

# Keeps track of the amount of failed login attempts. This will be used to check for suspicious activities
failed_login_attempts = 0