'''
# 10952 A+B (5) - 다시 풀기
a, b = '', ''

while a != 0 and b != 0:
  a, b = map(int, input().split(' '));
  if a != 0 and b != 0:
    print(a + b);
'''
'''
# 10951 A+B (4) - 다시 풀기
# try, except에 대해 정리
import sys;

while True:
  try:
    a, b = map(int, sys.stdin.readline().rstrip().split(' '));
    print(a+b);
  except:
    break;
'''
"""
# 1110 더하기 사이클 - 다시 풀기: 15분 이내에 풀 수 있도록 + 예외처리 주의
'''
주어진 수 < 10: 앞에 0을 붙여 두자리 수로 바꿈
기본: 각 자리 숫자 더한 후 원래 숫자의 오른쪽 숫자와 더해서 나온 값을 이어붙임
이 과정을 반복해서 최초 숫자로 돌아오는 횟수를 구하기
'''
init = int(input());
val = init;
result, temp, count = '', '', 0;
while init != result:
  a, b, c, d = '', '', '', '';
  if val < 10:
    a = 0;
    b = val;
  else:
    a = val // 10;
    b = val % 10;
  temp = a + b
  if temp < 10:
    c = 0;
    d = temp;
  else:
    c = temp // 10;
    d = temp % 10;
  result = b * 10 + d;
  val = result;
  count += 1;
print(count);
"""