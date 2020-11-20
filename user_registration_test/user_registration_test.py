import pytest
from users_registration.user_registration_main.invalid_user_exception import InvalidUserDataException
from  users_registration.user_registration_main.user_registration import UserRegistration

def test_validate_user_data_when_input_is_empty_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data("Regex", "  ")
    assert str(error_type.value) == "Field cannot be empty.", "Failed because no exception was raised."

def test_validate_user_data_when_input_is_None_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data("Regex", None)
    assert str(error_type.value) == "Field cannot be null.", "Failed because no exception was raised."

def test_validate_user_data_when_first_name_correct_should_return_str_happy():
    return_value = UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "Shubham")
    assert  return_value, "Failed first name is invalid."

def test_validate_user_data_when_first_name_starts_with_small_letter_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "shubham")
    assert  str(error_type.value) == "Invalid data entered.", "Failed because no exception was raised."

def test_validate_user_data_when_first_name_is_too_short_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "Sh")
    assert str(error_type.value) == "Invalid data entered.", "Failed because no exception was raised."

def test_validate_user_data_when_last_name_correct_should_return_str_happy():
    return_value = UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "Rana")
    assert return_value, "Failed because last name was invalid"

def test_validate_user_data_when_last_name_starts_with_small_letter_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "rana")
    assert str(error_type.value) == "Invalid data entered.", "Failed because no exception was raised."

def test_validate_user_data_when_last_name_is_too_short_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "ra")
    assert str(error_type.value) == "Invalid data entered.", "Failed because no exception was raised."

@pytest.mark.parametrize (
    'valid_email, result', [
        ("abc@yahoo.com", True),
        ("abc-100@yahoo.com", True),
        ("abc.100@yahoo.com", True),
        ("abc111@abc.com", True),
        ("abc-100@abc.net", True),
        ("abc.100@abc.com.au", True),
        ("abc@1.com", True),
        ("abc@gmail.com.com", True),
        ("abc+100@gmail.com", True) ])
def test_validate_user_data_when_email_is_valid_should_return_happy(valid_email, result):
    return_value = UserRegistration.validate_user_data(UserRegistration.EMAIL_PATTERN, valid_email)
    assert return_value == result , "Failed because no exception was raised."

@pytest.mark.parametrize (
    'Invalid_email', [
        "abc",
        "abc@.com.my",
        "abc123@gmail.a",
        "abc123@.com",
        "abc123@.com.com",
        ".abc@abc.com",
        "abc()*@gmail.com",
        "abc@%*.com",
        "abc..2002@gmail.com",
        "abc.@gmail.com",
        "abc@abc@gmail.com",
        "abc@gmail.com.1a",
        "abc@gmail.com.aa.au"
    ])
def test_validate_user_data_when_email_is_invalid_should_throw_InvalidUserDataException(Invalid_email):
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.EMAIL_PATTERN, Invalid_email)
    assert str(error_type.value) == "Invalid data entered.", "Failed because no exception was raised."

def test_validate_user_data_when_phone_num_correct_should_return_str_happy():
    return_value = UserRegistration.validate_user_data(UserRegistration.PHONE_NUMBER_PATTERN, 8249167335)
    assert  return_value, "Failed because number entered is invalid."

def test_validate_user_data_when_phone_num_correct_with_countrycode_should_return_str_happy():
    return_value = UserRegistration.validate_user_data(UserRegistration.PHONE_NUMBER_PATTERN, '91 8249167335')
    assert  return_value, "Failed because phone number entered is invalid."

def test_validate_user_data_when_phone_num_with_no_space_separated_countrycode_should_return_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.PHONE_NUMBER_PATTERN, 918249167335)
    assert error_type.value.__str__() == "Invalid data entered.", "Failed because no exception was raised."

def test_validate_user_data_when_invalid_phone_should_return_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.PHONE_NUMBER_PATTERN, 918335)
    assert error_type.value.__str__() == "Invalid data entered.", "Failed because no exception was raised."

def test_validate_user_data_when_entered_valid_password_should_return_str_happy():
    return_value = UserRegistration.validate_user_data(UserRegistration.PASSWORD_PATTERN, "atqp3377M@")
    assert  return_value, "Failed because entered invalid password. "

def test_validate_user_data_when_invalid_password_with_less_than_eight_chars_should_return_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.PASSWORD_PATTERN, "Atq1p$")
    assert error_type.value.__str__() == "Invalid data entered.", "Failed because no exception was raised."

def test_validate_user_data_when_invalid_password_with_no_upper_case_chars_should_return_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.PASSWORD_PATTERN, "atqpqwqw1$")
    assert error_type.value.__str__() == "Invalid data entered.", "Failed because no exception was raised."

def test_validate_user_data_when_invalid_password_with_no_number_should_return_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.PASSWORD_PATTERN, "atqpqwqw$")
    assert error_type.value.__str__() == "Invalid data entered.", "Failed because no exception was raised."