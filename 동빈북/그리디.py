'''
오답 목록
1번 큰 수의 법칙: (문제풀이)시간 초과
3번 1이 될 때까지: (문제풀이)시간 초과
'''
import time
start_time = time.time()

end_time = time.time()
print('time :', end_time - start_time)
'''
오답 내역
#######################################################
1. 큰 수의 법칙(p.92)
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
to_add = []
max_num = max(nums)
sub_max = 0
if nums.count(max_num) == 1 and m == k:
  to_add.append(nums.pop(nums.index(max_num)))
else:
  to_add.append(nums.pop(nums.index(max_num)))
  sub_max = max(nums)
  num_sub = nums.count(sub_max)
  for i in range(num_sub):
    to_add.append(sub_max)
loop = m // (k + 1)
result = 0
if nums.count(max_num) == 1 and m == k:
  result = to_add[0]*k
else:
  for i in range(loop):
    result += (to_add[0] * k)
  result += to_add[1] * loop
print(result)
#######################################################
3. 1이 될 때까지
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