'''
# 2739 구구단 - 체크: range 설정 문제
val = int(input());

for index in range(1, 10):
  print(f'{val} * {index} = {val * index}');
'''
'''
# 10950 A+B (3)
round = int(input());

for i in range(round):
  a, b = map(int, input().split(' '));
  print(a + b);
'''
'''
# 8393 합
lastNum = int(input());

temp = [];
for i in range(1, lastNum + 1):
  temp.append(i);

print(sum(temp));
'''
'''
# 15552 빠른 A+B - 다시 풀기
# 파이썬 sys.stdin.readline, .rstrip() 관련 내용 정리
import sys;

numbers = int(input());

for i in range(numbers):
  a, b = map(int, sys.stdin.readline().rstrip().split(' '));
  print(a + b);
'''
'''
# 2741 N 찍기
numbers = int(input());

for i in range(1, numbers + 1):
  print(i);
'''
'''
# 2742 기찍 N - 체크: range 역순 적용 방법
numbers = int(input());

for i in range(numbers, 0, -1):
  print(i);
'''
'''
# 11021 A+B (7)
numbers = int(input());

for i in range(1, numbers + 1):
  a, b = map(int, input().split(' '));
  print(f'Case #{i}: {a + b}');
'''
'''
# 11022 A+B (8)
numbers = int(input());

for i in range(1, numbers + 1):
  a, b = map(int, input().split(' '));
  print(f'Case #{i}: {a} + {b} = {a + b}');
'''
'''
# 2438 별 찍기 (1)
numbers = int(input());

for i in range(1, numbers + 1):
  print('*' * i);
'''
'''
# 2439 별 찍기 (2) - 체크: 스페이스바로 띄운 빈칸도 일단 문자열로 취급되는 것 같음
numbers = int(input());

for i in range(1, numbers + 1):
  print(' ' * (numbers - i) + '*' * i);
'''
'''
# 10871 X보다 작은 수 - 체크: join() 메서드의 사용 조건
numbers, cond = map(int, input().split(' '));
numList = list(map(int, input().split(' ')));
temp = [];

for elem in numList:
  if elem < cond:
    temp.append(str(elem));

print(' '.join(temp));
'''