from enum import Enum

class authentication_level(Enum):
    MEMBER = 0
    ADVISOR = 1
    SYSTEM_ADMINISTRATOR = 2
    SUPER_ADMINISTRATOR = 3

class log_user_options(Enum):
    CREATION = "created"
    MODIFIED = "modified"
    DELETION = "deleted"
    PASSWORD_RESET = "password reset"

class log_backup_options(Enum):
    CREATION = "created"
    RESTORATION = "restored"

class log_lookup_options(Enum):
    MEMBER = "member"
    USER = "user"