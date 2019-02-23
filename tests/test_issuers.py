import pytest

from card_validator.issuers import get_issuer


def test_visa():
    assert get_issuer('4862876677853409') == 'Visa'


def test_mastercard():
    assert get_issuer('5462876677853409') == 'MasterCard'


def test_american_express():
    assert get_issuer('3472876677853409') == 'American Express'


def test_unknown_numbers():
    with pytest.raises(ValueError):
        get_issuer('9462876677853409')
