'''
# 11654 아스키 코드 - 체크: 아스키 코드 출력 함수
# 문자 -> 코드: ord(), 코드 -> 문자: chr()
print(ord(input()));
'''
'''
# 11720 숫자의 합 - 다시 풀기: 더 간단하게 짜기
number = int(input());
numInputs = input();

temp = [];
for i in range(number):
  temp.append(int(numInputs[i:i+1]));

print(sum(temp));
'''
'''
# 10809 알파벳 찾기 - 체크: 알파벳 리스트 만들기
# string 모듈 ascii_lowercase
from string import ascii_lowercase;

S = input();
alpha = list(ascii_lowercase);
word = list(S);
temp = [];

for i in alpha:
  try:
    temp.append(str(word.index(i)));
  except:
    temp.append(str(-1));
print(' '.join(temp));
'''
'''
# 2675 문자열 반복
number = int(input());
temp = [];

for i in range(number):
  temp.append(input().split(' '));

result = [];
for i in temp:
  tempResult = [];
  for j in i[1]:
    tempResult.append(j*int(i[0]));
  result.append(''.join(tempResult));

for i in result:
  print(i);
'''
'''
# 1157 단어 공부 - 체크: 대소문자 구분하지 않는 문자열 비교
# 대문자, 소문자로 변환 후 비교
from string import ascii_lowercase;
S = input();
check = S.lower();

result = {};
for i in ascii_lowercase:
  count = check.count(i);
  if count != 0:
    result[i] = count;

keys = list(result.keys());
vals = list(result.values());
temp = [];
result = '';

for i in range(len(vals)):
  if vals[i] == max(vals):
    temp.append(i);
  if len(temp) != 1:
    result = '?';
  else:
    result = keys[temp[0]].upper();
print(result);
'''
'''
# 1152 단어의 갯수
sentence = input();
check = sentence.split(' ');
if check[0] == '':
  check.pop(0);
if check[-1] == '':
  check.pop(-1);
print(len(check));
'''
'''
# 2908 상수
inputs = input().split(' ');
nums = [];
for i in inputs:
  nums.append(int(i[::-1]));
print(max(nums));
'''
'''
# 5622 다이얼
from string import ascii_lowercase;

word = list(input().lower());
nums = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9];
phone = [i for i in range(10)]
phoneTime = [];
temp = [];
for i in word:
  wordIndex = ascii_lowercase.index(i);
  temp.append(nums[wordIndex]);
for i in phone:
  if i == 0:
    phoneTime.append(11);
  else:
    phoneTime.append(i+1);
result = [];
for i in temp:
  result.append(phoneTime[i]);
print(sum(result))
'''
# 2941 크로아티아 알파벳 - 다시풀기 + replace() 메서드 체크
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))