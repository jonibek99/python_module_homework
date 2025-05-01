# Round a decimal number to the nearest integer
import math

def round_to_nearest_integer(number):
    """
    Rounds a decimal number to the nearest integer.

    Args:
        number (float): The decimal number.

    Returns:
        int: The nearest integer.
    """
    return round(number)
a=float(input())
print(round_to_nearest_integer(a))