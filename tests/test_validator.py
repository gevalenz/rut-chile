import pytest
from rut_chile import rut_chile


class TestIsValidRutTests:

    @pytest.mark.parametrize("test_input, expected", [
        (None, False),
        ("", False),
        (" ", False),
        ("k", False),
        ("1", False),
        ("*", False),
        ("1-", False),
        (".-", False),
        ("1.", False),
        ("1.11", False),
        ("1.111K", False),
        (".1", False),
        ("123.K", False),
        ("123.12-K", False)
    ])
    def test_invalid_argument(self, test_input, expected):
        assert rut_chile.is_valid_rut(test_input) == expected

    @pytest.mark.parametrize("test_input, expected", [
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
    def test_invalid_rut(self, test_input, expected):
        assert rut_chile.is_valid_rut(test_input) == expected

    @pytest.mark.parametrize("test_input, expected", [
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
    def test_valid_rut(self, test_input, expected):
        assert rut_chile.is_valid_rut(test_input) == expected


class TestGetVerificationDigit:
    @pytest.mark.parametrize("test_input", [
        (None),
        (""),
        (" "),
        ("k"),
        ("1k"),
        ("*"),
        ("1-"),
        (".-"),
        ("12312-K"),
        ("12.312-K"),
    ])
    def test_invalid_argument(self, test_input):
        with pytest.raises(Exception) as excinfo:
            rut_chile.get_verification_digit(test_input)
        assert str(excinfo.value) == 'Invalid input'

    @pytest.mark.parametrize("test_input, expected", [
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
    def test_valid_rut(self, test_input, expected):
        assert rut_chile.get_verification_digit(test_input) == expected
