"""Module that provides common functionality regarding Chilean RUT
"""

import re


def is_valid_rut(rut: str) -> bool:
    """Determines if a given rut is valid

    Arguments:
        rut {str} -- Complete rut, including verification digit. It might
        contain dots and a dash.

    Returns:
        bool -- True if rut is valid. False otherwise.

    Raises:
        ValueError: when input is not valid to be processed.
    """
    __raise_error_if_rut_input_format_not_valid(rut)
    rut = __clean_rut(rut)
    return get_verification_digit(rut[:-1]) == rut[-1]


def get_verification_digit(rut: str) -> str:
    """Calculates the verification digit for a given rut

    Arguments:
        rut {str} -- Rut containing digits only. No dots nor verification
        digit allowed.

    Returns:
        str -- Verification digit. It might be a digit or 'k'.

    Raises:
        ValueError: when input is not valid to be processed.
    """
    __raise_error_if_input_to_get_verification_digit_not_valid(rut)
    partial_sum = __get_partial_sum_for_verification_digit_computation(rut)
    return __get_verification_digit_from_partial_sum(partial_sum)


def get_capitalized_verification_digit(rut: str) -> str:
    """Calculates the capitalized verification digit for a given rut

    Arguments:
        rut {str} -- Rut containing digits only. No dots nor verification
        digit allowed.

    Returns:
        str -- Verification digit. It might be a digit or 'K'.

    Raises:
        ValueError: when input is not valid to be processed.
    """
    return get_verification_digit(rut).upper()


def format_rut_with_dots(rut: str) -> str:
    """Formats RUT, adding dots and dash

    Arguments:
        rut {str} -- RUT to be formatted

    Returns:
        str -- Formatted RUT.

    Raises:
        ValueError: when input is not valid to be processed.
    """
    __raise_error_if_rut_input_format_not_valid(rut)
    formatted_rut = __clean_rut(rut)
    formatted_rut = __add_dash_to_rut(rut)
    base_rut = __add_thousands_separator(formatted_rut[:-2])
    return base_rut + formatted_rut[-2:]


def format_capitalized_rut_with_dots(rut: str) -> str:
    """Formats RUT, adding dots, dash and capitalized verification digit

    Arguments:
        rut {str} -- RUT to be formatted

    Returns:
        str -- Formatted RUT.

    Raises:
        ValueError: when input is not valid to be processed.
    """
    return format_rut_with_dots(rut).upper()


def format_rut_without_dots(rut: str) -> str:
    """Formats RUT, adding dash

    Arguments:
        rut {str} -- RUT to be formatted

    Returns:
        str -- Formatted RUT.

    Raises:
        ValueError: when input is not valid to be processed.
    """
    __raise_error_if_rut_input_format_not_valid(rut)
    formatted_rut = __clean_rut(rut)
    return __add_dash_to_rut(formatted_rut)


def format_capitalized_rut_without_dots(rut: str) -> str:
    """Formats RUT, adding dash and capitalized verification digit

    Arguments:
        rut {str} -- RUT to be formatted

    Returns:
        str -- Formatted RUT.

    Raises:
        ValueError: when input is not valid to be processed.
    """
    return format_rut_without_dots(rut).upper()


def __raise_error_if_rut_input_format_not_valid(rut: str):
    if not __is_rut_input_valid(rut):
        raise ValueError("invalid input")


def __is_rut_input_valid(rut: str) -> bool:
    return rut and __is_well_formatted(rut)


def __is_well_formatted(rut: str) -> bool:
    format_regex = r"^((\d{1,3}(\.\d{3})+-)|\d+-?)(\d|k|K)$"
    return re.match(format_regex, rut) is not None


def __raise_error_if_input_to_get_verification_digit_not_valid(rut: str):
    if not __is_rut_format_valid_to_get_verification_digit(rut):
        raise ValueError("invalid input")


def __is_rut_format_valid_to_get_verification_digit(rut: str) -> bool:
    format_regex = r"^\d+$"
    return rut and re.match(format_regex, rut)


def __get_partial_sum_for_verification_digit_computation(rut: str) -> int:
    factors = [2, 3, 4, 5, 6, 7]
    partial_sum = 0
    factor_position = 0
    for digit in reversed(rut):
        partial_sum += int(digit) * factors[factor_position]
        factor_position = (factor_position + 1) % 6
    return partial_sum


def __get_verification_digit_from_partial_sum(partial_sum: int) -> str:
    verification_digit = (11 - partial_sum % 11) % 11
    return str(verification_digit) if verification_digit < 10 else 'k'


def __clean_rut(rut: str) -> bool:
    return rut.replace(".", "").replace("-", "").lower()


def __add_thousands_separator(rut: str) -> str:
    if len(rut) < 4:
        return rut
    digit_groups = __generate_digit_groups(rut)
    return ".".join(digit_groups)


def __generate_digit_groups(rut: str) -> []:
    digit_groups = __add_most_significant_digits_group(rut) + \
                   __generate_least_significant_digit_groups(rut)
    return digit_groups


def __add_most_significant_digits_group(rut: str) -> []:
    digit_group = []
    if len(rut) % 3 > 0:
        digit_group.append(rut[:len(rut) % 3])
    return digit_group


def __generate_least_significant_digit_groups(rut: str) -> []:
    digit_groups = []
    for i in range(int(len(rut) / 3)):
        start = len(rut) % 3 + 3 * i
        digit_groups.append(rut[start:start + 3])
    return digit_groups


def __add_dash_to_rut(rut: str) -> str:
    return '-'.join([rut[:-1], rut[-1]])
