print('숫자와 연산자를 입력해 주세요 >')

def calculator(num1, op, num2):
    if op == '더하기':
        return num1 + num2
    elif op == '빼기':
        return num1 - num2
    elif op == '나누기':
        return num1 / num2
    elif op == '곱하기':
        return num1 * num2
    else:
        return '취소'

firstInput = input()
opInput = input()
secondInput = input()

print(calculator(int(firstInput), opInput, int(secondInput)))