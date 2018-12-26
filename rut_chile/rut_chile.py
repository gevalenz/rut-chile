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

    if not __is_rut_input_valid(rut):
        raise ValueError("invalid input")
    rut = __clean_rut(rut)
    return get_verification_digit(rut[:-1]) == rut[-1]


def get_verification_digit(rut: str, capitalize: bool = False) -> str:
    """Calculates the verification digit for a given rut

    Arguments:
        rut {str} -- Rut containing digits only. No dots nor verification
        digit allowed. If input is invalid, it raises and "ValueError"
        exception

        capitalize {bool} -- Indicates if returned value must be a capital
        letter (default: {False})

    Returns:
        str -- Verification digit. It might be a digit, 'k' or 'K'.
    """
    if not __is_rut_format_valid_to_get_verification_digit(rut):
        raise ValueError("invalid input")

    partial_sum = __get_partial_sum_for_verification_digit_computation(rut)
    verification_digit = __get_verification_digit_from_partial_sum(partial_sum, capitalize)
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

    if not __is_rut_input_valid(rut):
        raise ValueError("invalid input")
    rut = __clean_rut(rut)

    if with_dots:
        formatted_rut = __add_thousands_separator(rut[:-1])
    else:
        formatted_rut = rut[:-1]

    formatted_rut = '-'.join([formatted_rut, rut[-1]])

    if upper:
        formatted_rut = formatted_rut.upper()

    return formatted_rut


def __is_rut_input_valid(rut: str) -> bool:
    return rut and __is_well_formatted(rut)


def __is_well_formatted(rut: str) -> bool:
    format_regex = r"^((\d{1,3}(\.\d{3})+-)|\d+-?)(\d|k|K)$"  # Valid format
    return re.match(format_regex, rut) is not None


def __is_rut_format_valid_to_get_verification_digit(rut: str) -> bool:
    format_regex = r"^\d+$"
    return rut and re.match(format_regex, rut)


def __get_partial_sum_for_verification_digit_computation(rut: str) -> int:
    factors = [2, 3, 4, 5, 6, 7]  # Factors for calculating verification digit
    partial_sum = 0
    factor_pos = 0
    for digit in reversed(rut):
        partial_sum += int(digit) * factors[factor_pos]
        factor_pos = (factor_pos + 1) % 6
    return partial_sum


def __get_verification_digit_from_partial_sum(partial_sum: int, capitalize: bool) -> str:
    verification_digit = (11 - partial_sum % 11) % 11
    if verification_digit == 10:
        if capitalize:
            return "K"
        return "k"
    return verification_digit


def __clean_rut(rut: str) -> bool:
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
