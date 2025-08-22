import pytest

from src.string_calculator import StringCalculator


@pytest.fixture
def calc():
    return StringCalculator()


def test_empty_string_returns_0(calc):
    assert calc.add("") == 0

def test_single_number_1_returns_value(calc):
    assert calc.add("1") == 1

def test_single_number_7_returns_value(calc):
    assert calc.add("7") == 7

def test_two_numbers_comma_delimiter(calc):
    assert calc.add("1,2") == 3

def test_multiple_amount_of_numbers(calc):
    assert calc.add("1,2,3,4,5") == 15

def test_newlines_are_delimiters(calc):
    assert calc.add("1\n2,3") == 6