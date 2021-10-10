'''
# 15596 정수 N개의 합 - 다른 방법으로 다시 풀어보기
def solve(a: list):
  return sum(a);
소스코드:
def solve(a):
    ans = 0
    return ans
'''
'''
# 4673 셀프 넘버
nums = [i for i in range(1, 10001)];

def d(n):
  tempList = list(str(n));
  result = n;
  for i in tempList:
    result += int(i);
  return result;

temp = [];
for number in nums:
  if d(number) <= 10000:
    temp.append(d(number));

resultList = [];
for number in nums:
  if number not in temp:
    resultList.append(number);

for i in resultList:
  print(i);
'''
'''
# 1065 한수 - 다시 풀기: 15분 이내로
num = int(input());

def han(num: int):
  temp = list(str(num));
  lst = [];
  for i in temp:
    lst.append(int(i));
  if len(lst) == 1:
    return True;
  elif len(lst) == 2:
    return True;
  else:
    diff = lst[0] - lst[1];
    result = '';
    for index in range(len(lst) - 1):
      if lst[index] - lst[index+1] == diff:
        result = True;
      else:
        result = False;
    return result;

testLst = [i for i in range(1, num+1)];
count = 0;
for i in testLst:
  if han(i):
    count += 1;
print(count);
'''