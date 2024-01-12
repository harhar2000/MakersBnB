from lib.login_validator import LoginValidator
import pytest

def test_is_valid():
    validator = LoginValidator('user test', 'password test')
    assert validator.is_valid() == True

def test_is_not_valid_with_bad_user_name():
    validator_1 = LoginValidator("", 'password test')
    assert validator_1.is_valid() == False
    validator_2 = LoginValidator(None, 'password test')
    assert validator_2.is_valid() == False


def test_is_not_valid_with_bad_password():
    validator_1 = LoginValidator("user test", "")
    assert validator_1.is_valid() == False
    validator_2 = LoginValidator("user test", None)
    assert validator_2.is_valid() == False


def test_generate_errors():
    validator_1 = LoginValidator("", "")
    assert validator_1.generate_errors() == [
        "User must not be blank",
        "Password must not be blank"
    ]
    validator_2 = LoginValidator("user test", "")
    assert validator_2.generate_errors() == [
        "Password must not be blank"
    ]
    validator_3 = LoginValidator("", "password test")
    assert validator_3.generate_errors() == [
        "User must not be blank"
    ]

def test_get_valid_user_name_if_user_name_valid():
    validator = LoginValidator('user test', 'password test')
    assert validator.get_valid_user_name() == "user test"

def test_get_valid_user_name_refuses_if_invalid():
    validator = LoginValidator("", "password test")
    with pytest.raises(ValueError) as err:
        validator.get_valid_user_name()
    assert str(err.value) == "Cannot get valid user"


def test_get_valid_password_if_password_valid():
    validator = LoginValidator('user test', 'password test')
    assert validator.get_valid_user_password() == 'password test'

def test_get_valid_user_password_refuses_if_invalid():
    validator = LoginValidator("My title", "")
    with pytest.raises(ValueError) as err:
        validator.get_valid_user_password()
    assert str(err.value) == "Cannot get valid password"