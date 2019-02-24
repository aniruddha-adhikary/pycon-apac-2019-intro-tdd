def main():
    number = input('Please enter credit card number: ')

    if number.startswith('81') and len(number) == 16:
        print('UnionPay Card')

    elif number.startswith('6011') \
            or number.startswith('64') \
            or number.startswith('65') \
            and 16 <= len(number) <= 19:
        print("Discover Card")

    elif number.startswith('636') or 16 <= len(number) <= 19:
        print('InterPayment card')

    else:
        print('Sorry, unable to recognize card!')


if __name__ == '__main__':
    main()
