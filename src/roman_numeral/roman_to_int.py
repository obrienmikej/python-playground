"""
Converts a Roman numeral string to its corresponding integer value.
"""

import re

def roman_to_int(s: str) -> int:
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    if not isinstance(s, str) or not s:
        return 0

    if not re.fullmatch(r'^[IVXLCDM]+$', s):
        return None
    invalid_patterns = re.compile(r'(IIII|VV|XXXX|LL|CCCC|DD|MMMM|IL|IC|ID|IM|VX|XD|XM|LC|LD|LM|DM)')
    if invalid_patterns.search(s):
        return None

    result = 0
    prev_value = 0

    for char in s:
        value = roman_dict[char]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value

    return result
