"""Module that provides common functionality regarding Chilean RUT
"""

import re


def is_valid_rut(rut: str) -> bool:
    """Determines if a given rut is valid

    Arguments:
        rut {str} -- Complete rut, including verification digit. It might
        contain dots and a dash

    Returns:
        bool -- True if rut is valid. False otherwise
    """

    format_regex = r"^((\d{1,3}(\.\d{3})+-)|\d+-?)(\d|k|K)$"  # Valid format
    if not rut or not re.match(format_regex, rut):
        return False

    rut = rut.replace(".", "").replace("-", "").lower()  # Standardize input
    return get_verification_digit(rut[:-1]) == rut[-1]


def get_verification_digit(rut: str, capitalize: bool = False) -> str:
    """Calculates the verification digit for a given rut

    Arguments:
        rut {str} -- Rut containing digits only. No dots nor verification
        digit allowed. If input is invalid, it raises and "Invalid input"
        exception

        capitalize {bool} -- Indicates if returned value must be a capital
        letter. False by default

    Returns:
        str -- Verification digit. It might be a digit, 'k' or 'K'.
    """
    format_regex = r"^\d+$"  # Regex to check valid format
    if not rut or not re.match(format_regex, rut):
        raise Exception("Invalid input")

    factors = [2, 3, 4, 5, 6, 7]  # Factors for calculating verification digit
    partial_sum = 0
    factor_pos = 0
    for digit in reversed(rut):
        partial_sum += int(digit) * factors[factor_pos]
        factor_pos = (factor_pos + 1) % 6

    verification_digit = (11 - partial_sum % 11) % 11
    if verification_digit == 10:
        if capitalize:
            return "K"
        return "k"
    return str(verification_digit)
