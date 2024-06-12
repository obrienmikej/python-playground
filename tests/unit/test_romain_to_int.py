import pytest
from src.roman_numeral import roman_to_int

def test_roman_to_int_valid_cases():
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MMMCMXCIX") == 3999

def test_roman_to_int_empty_string():
    assert roman_to_int("") == 0

def test_roman_to_int_invalid_string():
    assert roman_to_int("IIII") is None
    assert roman_to_int("VV") is None
    assert roman_to_int("IC") is None
    assert roman_to_int("A") is None
    assert roman_to_int("123") is None
    assert roman_to_int(" ") is None
    assert roman_to_int("IIIIIIIIIIII") is None

def test_roman_to_int_non_string_input():
    assert roman_to_int(1234) == 0
    assert roman_to_int(None) == 0
    assert roman_to_int([]) == 0
    assert roman_to_int({}) == 0