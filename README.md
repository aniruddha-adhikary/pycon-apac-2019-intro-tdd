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

## Installing Prerequisites

```
$ pip install -r requirements.txt
```

## Running Tests

```
$ pytest
```

## API Spec

Hosted on: `http://tuxboy.pythonanywhere.com`.

```
POST /api/v3/checkNumber
number=2329582342313
```

```python
import requests

response = requests.post('http://tuxboy.pythonanywhere.com/api/v3/checkNumber', data={'number': '123'})
```

## Tasks

1. Use the `RemoteCreditCardChecker` class to get the issuer.
2. Write tests for `RemoteCreditCardChecker`.
3. Turn off the internet / Wi-Fi.
4. Feel like hope probably ran out.
5. Start mocking.