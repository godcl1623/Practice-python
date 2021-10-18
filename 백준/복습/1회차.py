'''
# lvl2 2884
import sys;

h, m = map(int, sys.stdin.readline().rsplit());

if h >= 0 and m >= 45:
  print(h, m - 45);
elif h > 0 and m < 45:
  print(h - 1, m + 15);
elif h == 0 and m < 45:
  print(23, m + 15);
'''
'''
# lvl3 15552 빠른 A+B
import sys;

t = int(sys.stdin.readline());
for _ in range(t):
  a, b = map(int, sys.stdin.readline().rstrip().split());
  print(a+b);
'''
'''
# lvl4 10952 A+B (5)
import sys;
flag = True;

while flag:
  a, b = map(int, sys.stdin.readline().rstrip().split());
  if a != 0 and b != 0:
    print(a + b);
  else:
    flag = False;
'''
'''
# lvl4 10951 A+B (4)
import sys;

while True:
  try:
    a, b = map(int, sys.stdin.readline().rstrip().split());
    print(a + b);
  except:
    break;
'''
'''
# lvl4 1110 더하기 사이클 - 다시풀기(비효율화)
n = input();
check = n;
cycle = 0;
new = '';
while new != n:
  cycle += 1;
  if int(check) < 10:
    check = '0' + str(int(check));
    temp = str(int(check[0]) + int(check[1]));
    if int(temp) >= 10:
      check = check[1] + temp[1];
      new = str(int(check));
    else:
      check = check[1] + temp;
      new = str(int(check));
  else:
    temp = str(int(check[0]) + int(check[1]));
    if int(temp) >= 10:
      check = check[1] + temp[1];
      new = str(int(check));
    else:
      check = check[1] + temp;
      new = str(int(check));
print(cycle)
'''
'''
# lvl5 8958 OX퀴즈
import sys;
cases = int(sys.stdin.readline());
point = 0;
count = 0;
for i in range(cases):
  res = list(sys.stdin.readline().rstrip());
  for j in res:
    if j == 'O':
      count += 1;
      point += count;
    else:
      count = 0;
  print(point)
  point = 0;
  count = 0;
'''
'''
# lvl5 4344 평균은 넘겠지
import sys;

cases = int(sys.stdin.readline());
for _ in range(cases):
  case = list(map(int, sys.stdin.readline().rstrip().split()));
  students = case[0];
  scores = case[1:];
  avgScore = sum(scores) / students;
  upAvg = [];
  for i in scores:
    if i > avgScore:
      upAvg.append(i);
  upAvgStudents = len(upAvg) / students * 100;
  print(f'{upAvgStudents:.3f}%');
'''
'''
# lvl6 1065 한수 - 다시풀기(비효율화)
case = int(input());

def han(case):
  if case < 100:
    return case;
  elif case >= 100:
    default = 99;
    for i in range(100, case + 1):
      number = list(str(i));
      diff = int(number[0]) - int(number[1]);
      result = [];
      flag = False;
      for j in range(len(number)):
        if j > 0:
          result.append(int(number[j-1]) - int(number[j]));
      for k in result:
        if k == diff:
          flag = True;
        else:
          flag = False;
      if flag:
        default += 1;
    return default;

print(han(case));
'''
'''
# lvl7 11720 숫자의 합
numbers = int(input());
numInput = list(input());
result = 0;
for i in numInput:
  result += int(i);
print(result);
'''
'''
# lvl7 2941 크로아티아 알파벳 - 다시풀기(비효율화)
word = input();
target = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='];
for i in target:
  after = word.replace(i, '*');
  word = after;
result = list(word);
print(len(result));
'''
'''
# lvl19 18258 큐 2
import sys;
from collections import deque;
cmds = int(sys.stdin.readline());
queue = deque([]);

for _ in range(cmds):
  cmd = sys.stdin.readline().rstrip().split();
  if cmd[0] == 'push':
    queue.append(int(cmd[1]));
  elif cmd[0] == 'pop':
    if not queue:
      print(-1);
    else:
      print(queue.popleft());
  elif cmd[0] == 'size':
    print(len(queue));
  elif cmd[0] == 'empty':
    if not queue:
      print(1);
    else:
      print(0);
  elif cmd[0] == 'front':
    if not queue:
      print(-1);
    else:
      print(queue[0]);
  elif cmd[0] == 'back':
    if not queue:
      print(-1);
    else:
      print(queue[-1]);
'''
'''
# lvl19 11866 요세푸스 문제 0 - 다시풀기(비효율화, 런타임 에러 발생)
import sys;
from collections import deque;
n, k = map(int, sys.stdin.readline().rstrip().split());
circle = deque([i+1 for i in range(n)]);
targetIdx = circle.index(k);
target = circle[targetIdx];
yo = [];
while len(yo) != n:
  if circle[0] == target:
    yo.append(str(circle.popleft()));
    if len(circle) >= k:
      target = circle[targetIdx];
    else:
      circle.extend(circle*k);
      target = circle[targetIdx];
  else:
    circle.rotate(-1);
print(f"<{', '.join(yo)}>");
'''
# lvl19 1966번 프린터 큐 - 다시 풀기(못 풂)