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

def test_newlines_with_large_numbers(calc):
    assert calc.add("300\n501,1000") == 1801

def test_custom_single_char_delimiter(calc):
    assert calc.add("//;\n1;2") == 3

def test_none_returns_0(calc):
    assert calc.add(None) == 0

def test_spaces_are_ignored(calc):
    assert calc.add("1, 2,3") == 6

def test_leading_trailing_spaces(calc):
    assert calc.add(" 4 ,5 ") == 9

def test_multiple_char_custom_delimiter(calc):
    assert calc.add("//***\n1***2***3") == 6

def test_consecutive_delimiters_ignore_empty(calc):
    assert calc.add("1,,2") == 3

def test_custom_delimiter_dot(calc):
    assert calc.add("//.\n2.3.4") == 9

def test_custom_single_char_delimiter(calc):
    assert calc.add("//;\n1;2") == 3

def test_negative_numbers_raise_with_list(calc):
    with pytest.raises(Exception) as exc:
        calc.add("1,-2,3,-4")
    assert "Negative numbers not allowed: -2, -4" in str(exc.value)

def test_when_single_negative_number_present(calc):
    with pytest.raises(Exception) as exc:
        calc.add("1,2,3,-4")
    assert "Negative numbers not allowed: -4" in str(exc.value)

def test_when_zero_with_negative_number_present(calc):
    assert calc.add("1,2,3,-0") == 6