from card_validator.issuers import get_issuer

# Task 1: Make this a function
assert get_issuer('4862876677853409') == 'Visa'
print("Visa test passed!")
assert get_issuer('5462876677853409') == 'MasterCard'
print("MasterCard test passed!")
assert get_issuer('3462876677853409') == 'American Express'
print("All tests passed!")

# Task 2: Break down the function into three functions
# for testing Visa, MasterCard and American Express.
