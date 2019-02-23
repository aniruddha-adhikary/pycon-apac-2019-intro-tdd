# Introduction to Testing in Python

PyCon APAC 2019 (Manila, PH)

## Table of Contents


| Sl  | Branch   | Description                        | 
| --- | -------- | ---------------------------------- |
| 1   | `step-1` | Naive Testing                      |
| 2   | `step-2` | Dedicated Test Functions           |
| 3   | `step-3` | Running Tests Automatically        |
| 4   | `step-4` | Why consider writing tests         |
| 7   | `step-5` | Writing TestCase Classes           |
| 5   | `step-6` | Parametrizing your Tests           |
| 6   | `step-7` | Mocking the World Beyond           |
| 8   | `step-8` | Refactoring for Testing            |
| 9   | `step-9` | Measuring Test Coverage            |


## Business Logic

https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_.28IIN.29

| Issuer           | IIN ranges |
| ---------------- | ---------- |
| American Express | 34, 37     |
| MasterCard       | 51–55      |
| Visa             | 4          |

The card number has to start with the mentioned IIN range(s).

## Running Tests

```
$ python card_validator/issuers.py
```

## Tasks

1. Fix the `get_issuer` function in `card_validator/issuers.py` to fix a bug.
2. Add a test case for testing American Express cards.