from unittest import TestCase

import pytest

from card_validator.issuers import get_issuer


class ValidCreditCardTest(TestCase):

    def test_visa(self):
        assert get_issuer('4862876677853409') == 'Visa'

    def test_mastercard(self):
        assert get_issuer('5462876677853409') == 'MasterCard'

    def test_american_express(self):
        assert get_issuer('3472876677853409') == 'American Express'


    def test_unknown_numbers(self):
        with pytest.raises(ValueError):
            get_issuer('9462876677853409')


class CardIssuerConfusionTest(TestCase):

    def test_visa(self):
        assert get_issuer('4862876677853409') == 'Visa'
        with pytest.raises(ValueError):
            assert get_issuer('5862876677853409') == 'MasterCard'

    def test_mastercard(self):
        with pytest.raises(ValueError):
            assert get_issuer('5062876677853409') == 'MasterCard'

        assert get_issuer('5162876677853409') == 'MasterCard'
        assert get_issuer('5262876677853409') == 'MasterCard'
        assert get_issuer('5362876677853409') == 'MasterCard'
        assert get_issuer('5462876677853409') == 'MasterCard'
        assert get_issuer('5562876677853409') == 'MasterCard'

        with pytest.raises(ValueError):
            assert get_issuer('5662876677853409') == 'MasterCard'

    def test_american_express(self):
        assert get_issuer('3472876677853409') == 'American Express'
