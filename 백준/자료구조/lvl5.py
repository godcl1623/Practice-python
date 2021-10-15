'''
# 10818 최소, 최대 - 체크: sys.stdin.readline() int로 바꾸는법 조사
import sys;

numbers = int(input());
inputs = sys.stdin.readline().split(' ');
temp = [];

for i in range(numbers):
  temp.append(int(inputs[i]));

print(min(temp), max(temp));
'''
'''
# 2562 최댓값 - 체크: index() 사용법 조사
temp = [];

for i in range(9):
  temp.append(int(input()));

maxNum = max(temp);
indexNum = temp.index(maxNum) + 1;
print(maxNum);
print(indexNum);
'''
'''
# 2577 숫자의 갯수 - 체크: count() 사용법 조사
a = int(input());
b = int(input());
c = int(input());

tempList = list(str(a * b * c));
checkList = [i for i in range(10)];

for i in checkList:
  print(tempList.count(str(checkList[i])));
'''
'''
# 3052 나머지 - 체크: 자바스크립트 includes에 대응하는 in, not in 조건 조사
temp = [];
for i in range(10):
  temp.append(int(input()));

remains = [];
for i in temp:
  val = i % 42;
  if val not in remains:
    remains.append(val);

print(len(remains));
'''
'''
# 1546 평균
import sys;
numbers = int(input());
scores = sys.stdin.readline().split(' ');
temp = [];
for i in scores:
  temp.append(int(i));

newScores = [];
for i in temp:
  maxNum = max(temp);
  newScores.append(i / maxNum * 100);

print(sum(newScores)/len(newScores));
'''
'''
# 8958 OX퀴즈 - 체크: 15분 안에 풀기
numbers = int(input());

temp = [];
for i in range(numbers):
  temp.append(input());

for i in temp:
  count = 0;
  oCount = 0;
  current = '';
  for answer in list(i):
    if answer == 'O' and oCount == 0:
      oCount += 1;
      count += 1;
    elif answer == 'O' and oCount != 0:
      oCount += 1;
      count += oCount;
    else:
      oCount = 0;
      count += 0;
  print(count);
'''
'''
# 4344 평균은 넘겠지 - 체크: 소숫점 자릿수 제한하는 법 => 다시 풀기
import sys;
numbers = int(input());

temp = [];
for i in range(numbers):
  temp.append(sys.stdin.readline().rsplit());

for i in temp:
  numOfStudents = int(i[0]);
  scores = [];
  for j in i[1:]:
    scores.append(int(j));
  avgScore = sum(scores)/numOfStudents;
  count = 0;
  for j in scores:
    if j > avgScore:
      count += 1;
  print(f'{count/numOfStudents * 100:.3f}%');
'''
