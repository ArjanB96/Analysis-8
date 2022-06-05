from enum import Enum

class authentication_level(Enum):
    MEMBER = 0
    ADVISOR = 1
    SYSTEM_ADMINISTRATOR = 2
    SUPER_ADMINISTRATOR = 3