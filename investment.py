def invest(amount, rate, time):
    print('principal amount: ${}'.format(amount))
    print('annual rate of return: {}'.format(rate))
    for y in range(1, time + 1):
        amount = amount + (amount * rate)
        print('year {0}: ${1}'.format(y, amount))
    print()

invest(100,.05,8)
invest(2000,.025,5)
