"""
Business Logic

https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_.28IIN.29

| Issuer           | IIN ranges |
| ---------------- | ---------- |
| American Express | 34, 37     |
| MasterCard       | 51–55      |
| Visa             | 4          |
"""


def get_issuer(number: str):
    if number.startswith('4'):
        return 'Visa'

    second_digit = number[1]

    if number.startswith('3') and second_digit in ('4', '7'):
        return "American Express"

    if number.startswith('5') and second_digit in ('1', '2', '3', '4', '5'):
        return "MasterCard"

    raise ValueError("Unknown Card Type")
