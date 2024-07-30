import pytest

from phonebook import Phonebook


@pytest.fixture(scope='function')
def phonebook():
    """Return empty Phonebook instance"""
    yield Phonebook()
