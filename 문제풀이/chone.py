'''
array = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [8, 7, 6, 5, 4, 3, 2, 1]
arr3 = [3, 2, 4, 5, 6, 1, 8, 7]

# def piano(arr):
#   result = ''
#   for i in range(len(arr) - 1):
#     if arr[i+1] == arr[i] + 1:
#       result = 'ascending'
#     elif arr[i] == arr[i+1] + 1:
#       result = 'descending'
#     else:
#       result = 'mixed'
#   print(result)

def piano(arr):
  temp = []
  result = ''
  for i in range(len(arr) - 1):
    temp.append(arr[i+1] - arr[i])
  for j in range(len(temp) - 1):
    if temp[j] == 1 and temp[j+1] == 1 and temp[j - 1] == 1:
      result = 'ascending'
    elif temp[j] == -1 and temp[j+1] == -1 and temp[j-1] == 1:
      result = 'descending'
    else:
      result = 'mixed'
  return result

import random

randArr = random.sample(range(1, 9), 8)
print(piano(randArr), randArr)
'''
n, m = list(map(int, input().split(' '))) # 공백을 기준으로 두 숫자가 입력됐을 때 각각 배열에 입력함 + n과 m에 각각 할당
data = list(map(int, input().split(' ')))

result = 0
length = len(data) # data 길이를 이용해 3중반복문 수행

# count = 0
# i, j 고정시킨 채 k 바꿔가면서 테스트 진행 => k 다 돌면 j 하나 바꾸고 j + k 다 돌면 i 하나 바꾸는 방식
for i in range(0, length):
	for j in range(i + 1, length):
		for k in range(j + 1, length):
			sum_value = data[i] + data[j] + data[k]
			if sum_value <= m:
				# result에는 무조건 가장 큰 값이 할당됨
				result = max(result, sum_value)

print(result)