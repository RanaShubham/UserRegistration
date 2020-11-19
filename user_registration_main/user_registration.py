import re
from users_registration.user_registration_main.invalid_user_exception import InvalidUserDataException

class UserRegistration:
    #Regex patterns to match
    FIRST_NAME_PATTERN = "^[A-Z]{1}[a-z]{2,}$"
    LAST_NAME_PATTERN = "^[A-Z]{1}[a-z]{2,}$"

    @staticmethod
    def validate_user_data(pattern, user_input):
        '''
            Validates the input given by user.

        :param pattern: Pattern
        :type pattern: str
        :param user_input: User input
        :type user_input: str
        :return: None
        :rtype: None
        '''
        if not user_input:
            raise InvalidUserDataException("Field cannot be null.")
        if user_input.isspace():
           raise InvalidUserDataException("Field cannot be empty.")
        match_object = re.fullmatch(pattern, user_input)
        if not match_object:
            raise InvalidUserDataException("Invalid data entered.")
        return "happy"

def driver_function():
    first_name = input("Enter first name: ")
    UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, first_name)
    last_name = input("Enter last name: ")
    UserRegistration.validate_user_data(UserRegistration.LAST_NAME_PATTERN, last_name)

if  __name__ ==  "__main__":
    driver_function()