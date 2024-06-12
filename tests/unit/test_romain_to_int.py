# tests/test_roman_to_int.py

import pytest
from src.roman_numeral.roman_to_int import roman_to_int

def test_valid_roman_numerals_base():
    assert roman_to_int("I") == 1 
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10  
    assert roman_to_int("L") == 50
    assert roman_to_int("C") == 100
    assert roman_to_int("D") == 500
    assert roman_to_int("M") == 1000  

def test_valid_roman_numerals_combo():
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4    
    assert roman_to_int("IX") == 9
    assert roman_to_int("XII") == 12
    assert roman_to_int("XXVII") == 27
    assert roman_to_int("XLIV") == 44    
    assert roman_to_int("LIX") == 59
    assert roman_to_int("XCIII") == 93
    assert roman_to_int("CXLVI") == 146
    assert roman_to_int("DCCCXC") == 890  
    assert roman_to_int("MCMXCIV") == 1994 

def test_invalid_roman_numerals():
    assert roman_to_int("IIII") is None
    assert roman_to_int("VV") is None
    assert roman_to_int("XXXX") is None
    assert roman_to_int("LL") is None
    assert roman_to_int("CCCC") is None
    assert roman_to_int("DD") is None
    assert roman_to_int("MMMM") is None
    assert roman_to_int("IL") is None
    assert roman_to_int("IC") is None
    assert roman_to_int("ID") is None
    assert roman_to_int("IM") is None
    assert roman_to_int("VX") is None
    assert roman_to_int("XD") is None
    assert roman_to_int("XM") is None
    assert roman_to_int("LC") is None
    assert roman_to_int("LD") is None
    assert roman_to_int("LM") is None
    assert roman_to_int("DM") is None

def test_int_empty_string():
    assert roman_to_int("") == 0    

def test_non_string_inputs():
    assert roman_to_int("") == 0
    assert roman_to_int(None) == 0
    assert roman_to_int(1234) == 0
    assert roman_to_int([]) == 0
    assert roman_to_int({}) == 0
    assert roman_to_int(3.14) == 0

def test_non_roman_characters():
    assert roman_to_int("A") is None
    assert roman_to_int("123") is None
    assert roman_to_int("IIIIIIIII") is None
    assert roman_to_int("XYZ") is None
    assert roman_to_int("Roman") is None
    assert roman_to_int("MMMMMCMXCIX") is None
