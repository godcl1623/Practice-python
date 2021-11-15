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
############################################################
n, m = map(int, input().split())
a, b, d = map(int, input().split())
field = [list(map(int, input().split())) for i in range(n)]
field_rec = [[0]*m for i in range(n)]
field_rec[a][b] = 1
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3
count = 1
turn_time = 0
while True:
  turn_left()
  na = a + da[d]
  nb = b + db[d]
  if field_rec[na][nb] == 0 and field[na][nb] == 0:
    field_rec[na][nb] = 1
    a = na
    b = nb
    count += 1
    turn_time = 0
    continue
  else:
    turn_time += 1
  if turn_time == 4:
    na = a - da[d]
    nb = b - db[d]
    if field[na][nb] == 0:
      a, b = na, nb
    else:
      break
    turn_time = 0
print(count)
############################################################
end_time = time.time()
print('time: ', end_time - start_time)