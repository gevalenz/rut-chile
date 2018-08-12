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

    if not rut or not __is_well_formatted(rut):
        return False
    rut = __clean_rut(rut)
    return get_verification_digit(rut[:-1]) == rut[-1]


def get_verification_digit(rut: str, capitalize: bool = False) -> str:
    """Calculates the verification digit for a given rut

    Arguments:
        rut {str} -- Rut containing digits only. No dots nor verification
        digit allowed. If input is invalid, it raises and "Invalid input"
        exception

        capitalize {bool} -- Indicates if returned value must be a capital
        letter (default: {False})

    Returns:
        str -- Verification digit. It might be a digit, 'k' or 'K'.
    """
    format_regex = r"^\d+$"  # Regex to check valid format
    if not rut or not re.match(format_regex, rut):
        return None
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


def format_rut(rut: str, with_dots: bool = False, upper: bool = True) -> str:
    """Formats RUT according to the options

    Arguments:
        rut {str} -- RUT to be formatted

    Keyword Arguments:
        with_dots {bool} -- Indicates whether to add dot separators
        (default: {False})
        upper {bool} -- Indicates if result should be in uppercase
        (default: {True})

    Returns:
        str -- Formatted RUT. If input is not valid, returns None
    """

    if not rut or not __is_well_formatted(rut):
        return None
    rut = __clean_rut(rut)

    if with_dots:  # Add dots
        formatted_rut = __add_thousands_separator(rut[:-1])
    else:
        formatted_rut = rut[:-1]

    formatted_rut = '-'.join([formatted_rut, rut[-1]])  # Add dash

    if upper:
        formatted_rut = formatted_rut.upper()

    return formatted_rut


def __is_well_formatted(rut: str) -> bool:
    if not rut:
        raise ValueError("rut cannot be None")
    format_regex = r"^((\d{1,3}(\.\d{3})+-)|\d+-?)(\d|k|K)$"  # Valid format
    return re.match(format_regex, rut) is not None


def __clean_rut(rut: str) -> bool:
    if not rut or not __is_well_formatted(rut):
        raise ValueError("rut must be well formatted")
    return rut.replace(".", "").replace("-", "").lower()  # Standardize input


def __add_thousands_separator(rut: str) -> str:
    if len(rut) < 4:
        return rut

    digit_groups = []
    if len(rut) % 3 > 0:  # Most significant group of digits
        digit_groups.append(rut[:len(rut) % 3])
    for i in range(int(len(rut) / 3)):  # Generate 3-digit groups
        start = len(rut) % 3 + 3 * i
        digit_groups.append(rut[start:start + 3])
    return ".".join(digit_groups)
