import custommodule

def rspGame(me, yours):
    if me == '가위':
        if yours == '가위':
            return '비겼다'
        elif yours == '바위':
            return '졌다'
        else:
            return '이겼다'
    elif me == '바위':
        if yours == '가위':
            return '이겼다'
        elif yours == '바위':
            return '비겼다'
        else:
            return '졌다'
    elif me == '보':
        if yours == '가위':
            return '졌다'
        elif yours == '바위':
            return '이겼다'
        else:
            return '비겼다'
    else:
        return '반칙쓰지마'

value1 = custommodule.rsp()
value2 = custommodule.rsp()
print('나는 {}, 너는 {}. 결과는 내가 {}'.format(value1, value2, rspGame(value1, value2)))