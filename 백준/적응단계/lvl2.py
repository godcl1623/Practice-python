'''
# lvl2 1330 두 수 비교하기
usrInput = map(int, input().split(' '));
a, b = usrInput;

if a > b:
  print('>');
elif a < b:
  print('<');
else:
  print('==');
'''

'''
# lvl2 9498 시험 성적
usrInput = int(input());

if 90 <= usrInput <= 100:
  print('A');
elif 80 <= usrInput < 90:
  print('B');
elif 70 <= usrInput < 80:
  print('C');
elif 60 <= usrInput < 70:
  print('D');
else:
  print('F');
'''
'''
# lvl2 2753 윤년
val = int(input());

if (val % 4 == 0 and val % 100 != 0) or val % 400 == 0:
  print(1);
else:
  print(0);
'''

'''
# lvl2 14681 사분면 고르기
a = int(input());
b = int(input());

if a > 0:
  if b > 0:
    print(1);
  else:
    print(4);
else:
  if b > 0:
    print(2);
  else:
    print(3);
'''

'''
# lvl2 2884 알람 시계 - 체크: 예외처리를 미리 생각하지 못함
# 필수 조건: 원래 설정된 시간을 45분 앞서게 바꿈
usrInput = map(int, input().split(' '));
hour, minu = usrInput;
calMinu = minu - 45;

if calMinu >= 0:
  print(hour, calMinu);
else:
  if hour - 1 >= 0:
    print(hour - 1, 60 + calMinu);
  else:
    print(23, 60 + calMinu);
'''