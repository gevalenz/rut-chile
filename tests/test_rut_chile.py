import pytest
from rut_chile import rut_chile


class TestIsValidRutTests:

    @pytest.mark.parametrize("test_input, expected_value", [
        (None, ValueError),
        ("", ValueError),
        (" ", ValueError),
        ("k", ValueError),
        ("1", ValueError),
        ("*", ValueError),
        ("1-", ValueError),
        (".-", ValueError),
        ("1.", ValueError),
        ("1.11", ValueError),
        ("1.111K", ValueError),
        (".1", ValueError),
        ("123.K", ValueError),
        ("123.12-K", ValueError)
    ])
    def test_invalid_argument(self, test_input, expected_value):
        with pytest.raises(ValueError) as error:
            rut_chile.is_valid_rut(test_input)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("test_input, expected_value", [
        ("9868503-1", False),
        ("21518268-2", False),
        ("17175325-3", False),
        ("20930576-4", False),
        ("13402128-5", False),
        ("20737522-6", False),
        ("6842256-7", False),
        ("14983005-8", False),
        ("20247667-9", False),
        ("17832479-k", False),
        ("12667869-0", False)
    ])
    def test_invalid_rut(self, test_input, expected_value):
        assert rut_chile.is_valid_rut(test_input) == expected_value

    @pytest.mark.parametrize("test_input, expected_value", [
        ("00", True),
        ("0-0", True),
        ("1-9", True),
        ("98685030", True),
        ("9868503-0", True),
        ("9.868.503-0", True),
        ("21518268-1", True),
        ("17175325-2", True),
        ("20930576-3", True),
        ("13402128-4", True),
        ("20737522-5", True),
        ("6842256-6", True),
        ("14983005-7", True),
        ("20247667-8", True),
        ("17832479-9", True),
        ("12667869-k", True),
        ("12667869-K", True),
        ("12.667.869-K", True),
        ("12.667.869-k", True)
    ])
    def test_valid_rut(self, test_input, expected_value):
        assert rut_chile.is_valid_rut(test_input) == expected_value


class TestGetVerificationDigit:
    @pytest.mark.parametrize("test_input, expected_value", [
        (None, ValueError),
        ("", ValueError),
        (" ", ValueError),
        ("k", ValueError),
        ("1k", ValueError),
        ("*", ValueError),
        ("1-", ValueError),
        (".-", ValueError),
        ("12312-K", ValueError),
        ("12.312-K", ValueError),
    ])
    def test_invalid_argument(self, test_input, expected_value):
        with pytest.raises(ValueError) as error:
            rut_chile.get_verification_digit(test_input)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("test_input, expected_value", [
        ("0", "0"),
        ("1", "9"),
        ("9868503", "0"),
        ("21518268", "1"),
        ("17175325", "2"),
        ("20930576", "3"),
        ("13402128", "4"),
        ("20737522", "5"),
        ("6842256", "6"),
        ("14983005", "7"),
        ("20247667", "8"),
        ("17832479", "9"),
        ("12667869", "k")
    ])
    def test_valid_rut(self, test_input, expected_value):
        assert rut_chile.get_verification_digit(test_input) == expected_value


class TestGetCapitalizedVerificationDigit:
    @pytest.mark.parametrize("test_input, expected_value", [
        (None, ValueError),
        ("", ValueError),
        (" ", ValueError),
        ("k", ValueError),
        ("1k", ValueError),
        ("*", ValueError),
        ("1-", ValueError),
        (".-", ValueError),
        ("12312-K", ValueError),
        ("12.312-K", ValueError),
    ])
    def test_invalid_argument(self, test_input, expected_value):
        with pytest.raises(ValueError) as error:
            rut_chile.get_capitalized_verification_digit(test_input)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("test_input, expected_value", [
        ("0", "0"),
        ("1", "9"),
        ("9868503", "0"),
        ("21518268", "1"),
        ("17175325", "2"),
        ("20930576", "3"),
        ("13402128", "4"),
        ("20737522", "5"),
        ("6842256", "6"),
        ("14983005", "7"),
        ("20247667", "8"),
        ("17832479", "9"),
        ("12667869", "K")
    ])
    def test_valid_rut(self, test_input, expected_value):
        digit = rut_chile.get_capitalized_verification_digit(test_input)
        assert digit == expected_value


class TestFormatRutWithDots:
    @pytest.mark.parametrize("test_input, expected_value", [
        (None, ValueError),
        ("", ValueError),
        (" ", ValueError),
        ("k", ValueError),
        ("ab", ValueError),
        ("*", ValueError),
        ("1-", ValueError),
        (".-", ValueError),
        ("1.", ValueError),
        ("1.11", ValueError)
    ])
    def test_invalid_argument(self, test_input, expected_value):
        with pytest.raises(ValueError) as error:
            rut_chile.format_rut_with_dots(test_input)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("test_input, expected_value", [
        ("12", "1-2"),
        ("123", "12-3"),
        ("1234", "123-4"),
        ("12345", "1.234-5"),
        ("123456", "12.345-6"),
        ("1234567", "123.456-7"),
        ("12345678", "1.234.567-8"),
        ("123456789", "12.345.678-9"),
        ("123456789k", "123.456.789-k"),
    ])
    def test_valid_rut(self, test_input, expected_value):
        assert rut_chile.format_rut_with_dots(test_input) == expected_value


class TestFormatCapitalizedRutWithDots:
    @pytest.mark.parametrize("test_input, expected_value", [
        (None, ValueError),
        ("", ValueError),
        (" ", ValueError),
        ("k", ValueError),
        ("ab", ValueError),
        ("*", ValueError),
        ("1-", ValueError),
        (".-", ValueError),
        ("1.", ValueError),
        ("1.11", ValueError)
    ])
    def test_invalid_argument(self, test_input, expected_value):
        with pytest.raises(ValueError) as error:
            rut_chile.format_capitalized_rut_with_dots(test_input)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("test_input, expected_value", [
        ("12", "1-2"),
        ("123", "12-3"),
        ("1234", "123-4"),
        ("12345", "1.234-5"),
        ("123456", "12.345-6"),
        ("1234567", "123.456-7"),
        ("12345678", "1.234.567-8"),
        ("123456789", "12.345.678-9"),
        ("123456789k", "123.456.789-K"),
    ])
    def test_valid_rut(self, test_input, expected_value):
        rut = rut_chile.format_capitalized_rut_with_dots(test_input)
        assert rut == expected_value


class TestFormatRutWithoutDots:
    @pytest.mark.parametrize("test_input, expected_value", [
        (None, ValueError),
        ("", ValueError),
        (" ", ValueError),
        ("k", ValueError),
        ("ab", ValueError),
        ("*", ValueError),
        ("1-", ValueError),
        (".-", ValueError),
        ("1.", ValueError),
        ("1.11", ValueError)
    ])
    def test_invalid_argument(self, test_input, expected_value):
        with pytest.raises(ValueError) as error:
            rut_chile.format_rut_without_dots(test_input)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("test_input, expected_value", [
        ("12", "1-2"),
        ("123", "12-3"),
        ("1234", "123-4"),
        ("12345", "1234-5"),
        ("123456", "12345-6"),
        ("1234567", "123456-7"),
        ("12345678", "1234567-8"),
        ("123456789", "12345678-9"),
        ("123456789k", "123456789-k"),
    ])
    def test_valid_rut(self, test_input, expected_value):
        assert rut_chile.format_rut_without_dots(test_input) == expected_value


class TestFormatCapitalizedRutWithoutDots:
    @pytest.mark.parametrize("test_input, expected_value", [
        (None, ValueError),
        ("", ValueError),
        (" ", ValueError),
        ("k", ValueError),
        ("ab", ValueError),
        ("*", ValueError),
        ("1-", ValueError),
        (".-", ValueError),
        ("1.", ValueError),
        ("1.11", ValueError)
    ])
    def test_invalid_argument(self, test_input, expected_value):
        with pytest.raises(ValueError) as error:
            rut_chile.format_capitalized_rut_without_dots(test_input)
        assert type(error.value) is expected_value

    @pytest.mark.parametrize("test_input, expected_value", [
        ("12", "1-2"),
        ("123", "12-3"),
        ("1234", "123-4"),
        ("12345", "1234-5"),
        ("123456", "12345-6"),
        ("1234567", "123456-7"),
        ("12345678", "1234567-8"),
        ("123456789", "12345678-9"),
        ("123456789k", "123456789-K"),
    ])
    def test_valid_rut(self, test_input, expected_value):
        rut = rut_chile.format_capitalized_rut_without_dots(test_input)
        assert rut == expected_value
