def returnFunc(value, test):
    if value < 10:
        return 10

    sum = value + test

    return sum, test

this, that = returnFunc(40, 55)

print('this is sum of 2 params :', this)
print('this is second param :', that)