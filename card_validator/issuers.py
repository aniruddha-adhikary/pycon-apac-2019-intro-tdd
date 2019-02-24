"""
Business Logic

https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_.28IIN.29

| Issuer           | IIN ranges | regular expression |
| ---------------- | ---------- | ------------------ |
| American Express | 34, 37     | ^3[47]             |
| MasterCard       | 51–55      | ^5[1-5]            |
| Visa             | 4          | ^4                 |
"""
import re

import requests


class LocalCreditCardChecker:
    PATTERNS = {
        'Visa': re.compile(r'^4'),
        'MasterCard': re.compile(r'^5[1-5]'),
        'American Express': re.compile(r'^347'),
    }

    def get_issuer(self, number: str):

        for issuer, pattern in self.PATTERNS.items():
            if pattern.match(number):
                return issuer

        raise ValueError("Unknown Card Type")


class RemoteCreditCardChecker:
    def get_issuer(self, number):
        response = requests.post(number)
        response.raise_for_status()

        data = response.json()

        return data['issuest']


def get_issuer(number: str):
    return LocalCreditCardChecker().get_issuer(number)


def get_issuer_from_api(number: str):
    return RemoteCreditCardChecker().get_issuer(number)
