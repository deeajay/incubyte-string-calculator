import pytest

from src.string_calculator import StringCalculator


@pytest.fixture
def calc():
    return StringCalculator()


def test_empty_string_returns_0(calc):
    assert calc.add("") == 0