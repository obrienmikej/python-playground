from typing import List

def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)
    
    # Start from the last digit and move backwards
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If all the digits are 9, we will end up here
    return [1] + digits