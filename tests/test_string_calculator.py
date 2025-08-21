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