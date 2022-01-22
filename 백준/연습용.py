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
