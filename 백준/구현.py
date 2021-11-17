import time
'''
구현, 시뮬레이션, 브루트 포스 모두 같이 풀기
'''
"""
시뮬레이션
'''
정답
#1966. 프린터 큐
ints = int(input())
for _ in range(ints):
  docus, target_idx = map(int, input().split())
  q_imp = list(map(int, input().split()))
  q_curr_idx = [i+1 for i in range(len(q_imp))]
  init_val = q_imp[target_idx]
  init_idx = q_curr_idx[target_idx]
  count = 0
  while True:
    if q_imp[0] == max(q_imp):
      count += 1
      printed = q_imp.pop(0)
      printed_idx = q_curr_idx.pop(0)
      if printed == init_val and printed_idx == init_idx:
        print(count)
        break
      else:
        continue
    else:
      q_imp.append(q_imp.pop(0))
      q_curr_idx.append(q_curr_idx.pop(0))
      continue
'''
'''
# 14891 톱니바퀴
n, m = map(int, input().split())
r, c, d = map(int, input().split())
curr_map = [list(map(int, input().split())) for i in range(n)]
map_clean = [[0] * m for i in range(n)]
map_clean[r][c] = 1
rPoss = [-1, 0, 1, 0]
cPoss = [0, 1, 0, -1]
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3
cleaned = 1
turn_count = 0
while True:
  turn_left()
  new_r = r + rPoss[d]
  new_c = c + cPoss[d]
  if map_clean[new_r][new_c] == 0 and curr_map[new_r][new_c] == 0:
    map_clean[new_r][new_c] = 1
    r, c = new_r, new_c
    cleaned += 1
    turn_count = 0
    continue
  else:
    turn_count += 1
  if turn_count == 4:
    new_r = r - rPoss[d]
    new_c = c - cPoss[d]
    if curr_map[new_r][new_c] == 0:
      r, c = new_r, new_c
    else:
      break
    turn_count = 0
print(cleaned)
'''
"""
start_time = time.time()
############################################################
# 14891 톱니바퀴 - 못 맞힘

# 맞닿은 톱니의 극이 다르다 -> 한 톱니를 회전시키면 극이 다른 톱니가 반대 방향으로 회전
# 맞닿은 톱니의 극이 같다 -> 한 톱니를 회전시키면 극이 같은 톱니는 그대로 있음
# 1, 4번 톱니: 인덱스 2, 인덱스 6이 맞닿음
# 2, 3번 톱니: 인덱스 2와 6이 맞닿음

from collections import deque
arr = []
for _ in range(4):
    arr.append(deque(list(map(int, input()))))
K = int(input())

def rotate(i, dir):
    #시계방향
    if dir == 1 :
        arr[i].insert(0,arr[i].pop())
    #반시계방향
    elif dir == -1:
        arr[i].append(arr[i].popleft())

for _ in range(K):
    i, dir = map(int,input().split())
    rotate_arr = [[i-1,dir]]

    #오른쪽
    x = i-1
    histdir = dir
    while x + 1 <= 3:
        if arr[x][2] != arr[x+1][6] :
            histdir = -histdir
            rotate_arr.append([x+1, histdir])
        elif arr[x][2] == arr[x+1][6]:
            break
        x += 1

    #왼
    x = i-1
    histdir = dir
    while x - 1 >= 0 :
        if arr[x][6] != arr[x-1][2]:
            histdir = -histdir
            rotate_arr.append([x -1, histdir])
        elif arr[x][6] == arr[x-1][2]:
            break
        x -= 1
    for x, dd in rotate_arr:
        rotate(x,dd)

print(arr[0][0] * 1 + arr[1][0] * 2 + arr[2][0] * 4 + arr[3][0] * 8)

############################################################
end_time = time.time()
print('time: ', end_time - start_time)