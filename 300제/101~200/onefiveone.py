'''
오답현황(~210725)
오답 없음

다시 풀어보기(~210730): 157 1번 풀이 완료
156 2번
157
'''
'''
151
리스트에는 네 개의 정수가 저장돼 있다.

리스트 = [3, -20, -3, 44]
for문을 사용해서 리스트의 음수를 출력하라.

-20
-3
'''
리스트 = [3, -20, -3, 44]
for 변수 in 리스트:
    if 변수 < 0:
        print('151, ', 변수);

'''
152
for문을 사용해서 3의 배수만을 출력하라.

리스트 = [3, 100, 23, 44]
3
'''
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
    if 변수 % 3 == 0:
        print('152, ', 변수);

'''
153
리스트에서 20 보다 작은 3의 배수를 출력하라

리스트 = [13, 21, 12, 14, 30, 18]
12
18
'''
리스트 = [13, 21, 12, 14, 30, 18]
for 변수 in 리스트:
    if 변수 < 20 and 변수 % 3 == 0:
        print(f'153, {변수}')

'''
154
리스트에서 세 글자 이상의 문자를 화면에 출력하라

리스트 = ["I", "study", "python", "language", "!"]
study
python
language
'''
리스트 = ["I", "study", "python", "language", "!"]
for var in 리스트:
    if len(var) >= 3:
        print(f'154, {var}')

'''
155
리스트에서 대문자만 화면에 출력하라.

리스트 = ["A", "b", "c", "D"]
A
D
(참고) isupper() 메서드는 대문자 여부를 판별합니다.

>> 변수 = "A"
>> 변수.isupper()
True
>> 변수 = "a"
>> 변수.isupper()
False
'''
리스트 = ["A", "b", "c", "D"]
for var in 리스트:
    if var.isupper():
        print(f'155, {var}')

'''
156
리스트에서 소문자만 화면에 출력하라.(for문을 쓰되 islower 없이 3가지 방법으로 풀어보기)

리스트 = ["A", "b", "c", "D"]
b
c
'''
리스트 = ["A", "b", "c", "D"]

'''
157
이름의 첫 글자를 대문자로 변경해서 출력하라.(단, 리스트 제외 2줄로 출력 + replace 사용하지 말고 풀어보기)

리스트 = ['dog', 'cat', 'parrot']
Dog
Cat
Parrot
(참고) upper() 메서드는 문자열을 대문자로 변경합니다.

>> 변수 = "a"
>> a.upper()
A
>> 변수 = "abc"
>> 변수.upper()
ABC
'''
리스트 = ['dog', 'cat', 'parrot']

'''
158
파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
hello
ex01
intro
'''
rist = ['hello.py', 'ex01.py', 'intro.hwp']
for var in rist:
    foo = var.split('.')
    print(f'158, {foo[0]}')

'''
159
파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
intra.h
define.h
'''
rist = ['intra.h', 'intra.c', 'define.h', 'run.py']
for var in rist:
    foo = var.split('.')
    if foo[1] == 'h':
        print(f'159, {var}')

'''
160
파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
intra.h
intra.c
define.h
'''
rist = ['intra.h', 'intra.c', 'define.h', 'run.py']
for var in rist:
    foo = var.split('.')
    if foo[1] == 'h' or foo[1] == 'c':
        print(f'160, {var}')