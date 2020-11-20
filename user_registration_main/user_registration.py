import re
from users_registration.user_registration_main.invalid_user_exception import InvalidUserDataException

class UserRegistration:
    #Regex patterns to match
    FIRST_NAME_PATTERN = "^[A-Z]{1}[a-z]{2,}$"
    LAST_NAME_PATTERN = "^[A-Z]{1}[a-z]{2,}$"
    EMAIL_PATTERN = "^[a-z]{1,}([._+-][0-9]{1,})*[0-9]{0,}@([0-9]|[a-z]){1,}[.][a-z]{2,4}([.][a-z]{2,4}){0,1}$"
    PHONE_NUMBER_PATTERN = "^(91 ){0,1}[7-9][0-9]{9}$"
    PASSWORD_PATTERN = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$"

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
        user_input = str(user_input)
        if user_input.isspace():
           raise InvalidUserDataException("Field cannot be empty.")
        match_object = re.search(pattern, user_input)
        if not match_object:
            raise InvalidUserDataException("Invalid data entered.")
        return "happy"

def driver_function():
    '''
        Driver function to execute when running this program directly.

        :return: None
        :rtype: None
    '''
    first_name = input("Enter first name: ")
    UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, first_name)
    last_name = input("Enter last name: ")
    UserRegistration.validate_user_data(UserRegistration.LAST_NAME_PATTERN, last_name)
    email = input("Enter email: ")
    UserRegistration.validate_user_data(UserRegistration.EMAIL_PATTERN, email)
    phone_no:str = input("Enter valid phone number: ")
    UserRegistration.validate_user_data(UserRegistration.PHONE_NUMBER_PATTERN, phone_no)
    password = input("Enter password: ")
    UserRegistration.validate_user_data(UserRegistration.PASSWORD_PATTERN, password)

if  __name__ ==  "__main__":
    driver_function()