import pytest
from users_registration.user_registration_main.invalid_user_exception import InvalidUserDataException
from  users_registration.user_registration_main.user_registration import UserRegistration

def test_validate_user_data_when_first_name_correct_should_return_str_happy():
    return_value = UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "Shubham")
    assert  return_value == "happy"

def test_validate_user_data_when_first_name_starts_with_small_letter_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "shubham")
    assert  str(error_type.value) == "Invalid data entered."

def test_validate_user_data_when_first_name_is_null_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "")
    assert  str(error_type.value) == "Field cannot be null."

def test_validate_user_data_when_first_name_is_empty_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "  ")
    assert str(error_type.value) == "Field cannot be empty."

def test_validate_user_data_when_first_name_is_too_short_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "Sh")
    assert str(error_type.value) == "Invalid data entered."


def test_validate_user_data_when_last_name_correct_should_return_str_happy():
    return_value = UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "Rana")
    assert return_value == "happy"


def test_validate_user_data_when_last_name_starts_with_small_letter_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "rana")
    assert str(error_type.value) == "Invalid data entered."


def test_validate_user_data_when_last_name_is_null_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "")
    assert str(error_type.value) == "Field cannot be null."


def test_validate_user_data_when_last_name_is_empty_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "  ")
    assert str(error_type.value) == "Field cannot be empty."


def test_validate_user_data_when_last_name_is_too_short_should_throw_InvalidUserDataException():
    with pytest.raises(InvalidUserDataException) as error_type:
        UserRegistration.validate_user_data(UserRegistration.FIRST_NAME_PATTERN, "ra")
    assert str(error_type.value) == "Invalid data entered."

@pytest.mark.parametrize (
    'valid_email, result', [
        ("abc@yahoo.com", "happy"),
        ("abc-100@yahoo.com", "happy"),
        ("abc.100@yahoo.com", "happy"),
        ("abc111@abc.com", "happy"),
        ("abc-100@abc.net", "happy"),
        ("abc.100@abc.com.au", "happy"),
        ("abc@1.com", "happy"),
        ("abc@gmail.com.com", "happy"),
        ("abc+100@gmail.com", "happy") ])
def test_validate_user_data_when_email_is_valid_should_return_happy(valid_email, result):
    return_value = UserRegistration.validate_user_data(UserRegistration.EMAIL_PATTERN, valid_email)
    assert return_value == result

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
    assert str(error_type.value) == "Invalid data entered."