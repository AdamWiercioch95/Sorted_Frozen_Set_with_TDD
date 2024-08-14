from unittest.mock import Mock

from doubles_kata.my_service import MyService, Request
from doubles_kata.single_sign_on import SingleSignOnRegistry, SSOToken


def test_hello_name():
    stub_registry = Mock(SingleSignOnRegistry)
    my_service = MyService(stub_registry)
    response = my_service.handle(Request(name='Jarosław'), SSOToken())
    assert response.text == 'Hello Jarosław'


# spy test
def test_single_sign_on():
    spy_registry = Mock(SingleSignOnRegistry)
    my_service = MyService(spy_registry)
    token = SSOToken()
    my_service.handle(Request(name='Jarosław'), token)
    spy_registry.is_valid.assert_called_with(token)


def test_single_sign_on_with_invalid_token():
    spy_registry = Mock(SingleSignOnRegistry)
    spy_registry.is_valid.return_value = False
    my_service = MyService(spy_registry)
    token = SSOToken()
    response = my_service.handle(Request(name='Jarosław'), token)
    spy_registry.is_valid.assert_called_with(token)
    assert response.text == "Please sign in"


def confirm_token(correct_token):
    def is_valid(actual_token):
        if actual_token != correct_token:
            raise ValueError('Wrong token received')

    return is_valid


def test_single_sign_on_receives_correct_token():
    mock_registry = Mock(SingleSignOnRegistry)
    correct_token = SSOToken()
    mock_registry.is_valid = Mock(side_effect=confirm_token(correct_token))
    my_service = MyService(mock_registry)
    my_service.handle(Request(name='Jarosław'), correct_token)
    mock_registry.is_valid.assert_called()
