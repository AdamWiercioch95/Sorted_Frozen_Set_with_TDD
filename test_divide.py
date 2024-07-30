from decimal import Decimal

import pytest

from divide import divide


def test_division_with_positive_result():
    result = divide(10, 5)
    assert result == 2


def test_division_with_negative_result():
    result = divide(10, 5)
    assert result != 3


def test_division_by_zero_should_raise_error():
    with pytest.raises(ZeroDivisionError) as ctx_info:
        divide(10, 0)


def test_division_using_string_should_raise_error():
    with pytest.raises(TypeError) as ctx_info:
        divide(10, '1')


def test_division_using_digit_not_int_or_float():
    with pytest.raises(TypeError) as ctx_info:
        divide(Decimal(10), 2)
