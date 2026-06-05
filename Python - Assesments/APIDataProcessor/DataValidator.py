import re

#User defined exception
class InvalidFieldError(Exception):
    def __init__(self,fieldName,value):
        super().__init__(f"Invalid {fieldName}: {value}")
        self.fieldName=fieldName
        self.value=value


def validate_email(email):

    pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$"

    if(not re.match(pattern, email)):
        raise InvalidFieldError("email", email)
    
    return True


def validate_phone(phone):

    pattern=r"^[6-9][0-9]{9}$"

    if (not re.match(pattern, phone)):
        raise InvalidFieldError("phone",phone)
    
    return True


def validate_usn(usn):

    pattern=r"^25MCA\d{3}$"

    if (not re.match(pattern, usn)):
        raise InvalidFieldError("usn", usn)
    
    return True