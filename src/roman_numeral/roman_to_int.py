"""
Converts a Roman numeral string to its corresponding integer value.
"""

import re

def roman_to_int(s: str) -> int:
    """ Define roman numeral values in dictionary"""
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    # Validate input; empty or not a string
    if not isinstance(s, str) or not s:
        return 0
    # Validate input; is a roman numeral value
    if not re.fullmatch(r'^[IVXLCDM]+$', s):
        return None
    # Validate input; invalid roman numeral pattern
    invalid_patterns = re.compile(r'(IIII|VV|XXXX|LL|CCCC|DD|MMMM|IL|IC|ID|IM|VX|XD|XM|LC|LD|LM|DM)')
    if invalid_patterns.search(s):
        return None

    # Initialize variables
    result = 0
    prev_value = 0

    # Convert a Roman numeral string (s) into an integer value (result).
    for char in s:
        value = roman_dict[char]
        if value > prev_value:
            result += value - 2 * prev_value  # Adjust the previously added value
        else:
            result += value
        prev_value = value

    return result
