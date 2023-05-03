def compoundInterest():
    n = int('10000')

    rate = int('7')

    years = int('10')

    for i in range(years):
        n = n + ((n * rate) / 100)
    print(n)
compoundInterest()