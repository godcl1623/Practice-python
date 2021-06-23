"""
for val in range(10):
    if val % 2 != 0:
        if True:
            print('test')
        elif True:
            print('test2')
        else:
            print('test3')
        print(val)
        print(val)
        print(val)
        print(val)
"""
for val in range(10):
    if val % 2 == 0:
        continue
        if True:
            print('test')
        elif True:
            print('test2')
        else:
            print('test3')
        print(val)
        print(val)
        print(val)
        print(val)
    print('skipped codes, returing ', val)
    print('skipped codes, returing ', val)
    print('skipped codes, returing ', val)
    print('skipped codes, returing ', val)
