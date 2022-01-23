'''
# 동빈북 p.111 예제 4-1 상하좌우
n = int(input())
ver, hor = 1, 1
hor_dir = ['L', 'R']
hor_dir_val = [-1, 1]
ver_dir = ['U', 'D']
ver_dir_val = [-1, 1]
dirs = list(input().split())
for i in dirs:
  if i == 'L' or i == 'R':
    plus = hor_dir_val[hor_dir.index(i)]
    if hor + plus < 1 or hor + plus > n:
      continue
    else:
      hor += plus
  else:
    plus = ver_dir_val[ver_dir.index(i)]
    if ver + plus > n or ver + plus < 1:
      continue
    else:
      ver += plus
print(ver, hor)
'''
'''
n = int(input())
count = 0
for i in range(n + 1):
  for j in range(60):
    for k in range(60):
      if '3' in f'{i}{j}{k}':
        count += 1
print(count)
'''
'''
now = input()
curr_col = ord(now[0])
curr_row = int(now[1])
cols = [ord('a') + i for i in range(8)]
rows = [i + 1 for i in range(8)]
dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0
for i in dirs:
  if curr_col + i[0] in cols and curr_row + i[1] in rows:
    count += 1
print(count)
'''
'''
n, m = map(int, input().split())
a, b, d = map(int, input().split())
field = [list(map(int, input().split())) for i in range(n)]
visited = [[0 for i in range(m)] for j in range(n)]
visited[a][b] = 1
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3
count = 1
turn_time = 0
attempt = 1
while True:
  turn_left()
  turn_time += 1
  na = a + da[d]
  nb = b + db[d]
  if turn_time < 4:
    if visited[na][nb] == 0 and field[na][nb] == 0:
      a = na
      b = nb
      visited[a][b] = 1
      turn_time = 0
      count += 1
      attempt += 1
    else:
      attempt += 1
      continue
  else:
    na = a - da[d]
    nb = b - db[d]
    if field[na][nb] != 1:
      a = na
      b = nb
      turn_time = 0
      attempt += 1
    else:
      break
print(count)
'''