import pytest
from users_registration.user_registration_main.invalid_user_exception import InvalidUserDataException
from  users_registration.user_registration_main.user_registration import UserRegistration

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