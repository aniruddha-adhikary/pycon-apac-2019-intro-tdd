from card_validator.issuers import get_issuer


# Why is Pytest not recognizing these tests?


def visa_test():
    assert get_issuer('4862876677853409') == 'Visa'


def mastercard_test():
    assert get_issuer('5462876677853409') == 'MasterCard'


def american_express_test():
    assert get_issuer('3462876677853409') == 'American Express'
