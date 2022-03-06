'''
# 오답 및 풀이 현황
1. Container with Most Water △(3/6)
2160. Minimum Sum of Four Digit Number After Splitting Digits(3/6)
'''
import time
start_time = time.time()
##################################################
num = 2436
strarr = [i for i in str(num)]
arr = list(map(int, strarr))
arr.sort()
new1 = []
new2 = []
for i in range(len(arr)):
  if i % 2 == 0:
    new1.append(arr[i])
  else:
    new2.append(arr[i])
str1 = ''
str2 = ''
for i in list(map(str, new1)):
  if i != '0':
    str1 += i
for i in list(map(str, new2)):
  if i != '0':
    str2 += i
if str1 == '':
  str1 = 0
if str2 == '':
  str2 = 0
print(int(str1) + int(str2))
##################################################
end_time = time.time()
print('time: ', end_time - start_time)