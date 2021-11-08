'''
그리드 실전 1
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
nums_max = nums[-1]
nums_sub = nums[-2]
loop = m // (k + 1)
left = m - (k + 1) * loop
result = 0
for i in range(loop):
  result += nums_max * k
  result += nums_sub
print(result)
'''
'''
그리드 실전 2
n, m = map(int, input().split())
mins = []
for _ in range(n):
  cardSet = list(map(int, input().split()))
  mins.append(min(cardSet))
print(max(mins))
'''
'''
그리드 실전 3
n, k = map(int, input().split())
count = 0
while True:
  if n % k == 0:
    n /= k
    count += 1
    if n == 1:
      break
    else:
      continue
  else:
    n -= 1
    count += 1
    if n == 1:
      break
    else:
      continue
print(count)
'''
import time
start_time = time.time()

end_time = time.time()
print('time: ', end_time - start_time)