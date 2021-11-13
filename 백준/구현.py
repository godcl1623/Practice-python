import time
'''
구현, 시뮬레이션, 브루트 포스 모두 같이 풀기
'''
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
start_time = time.time()
############################################################
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for i in range(n)]
clean_count = 0
turn_count = 0
def turn_left():
  global d, turn_count
  turn_count += 1
  if d == 0:
    d = 3
  else:
    d -= 1
while True:
  print('(r, c): ', (r, c))
  print('clean stat: ', room[r][c])
  print('d: ', d)
  print('turn_count: ', turn_count)
  # 사방 탐색이 진행중인 경우
  if turn_count < 4:
    # 현재 위치가 청소가 안 된 상태인 경우
    if room[r][c] == 0:
      room[r][c] = 1
      clean_count += 1
      print('##### cleaned #####')
      for i in range(len(room)):
        for j in range(len(room[i])):
          if i == r and j == c:
            print(room[i][j]+1, end=' ')
          else:
            print(room[i][j], end=' ')
        print()
    # 현재 위치가 청소가 된 상태인 경우 -> 탐색 실행
    else:
      # 현재 위치 왼쪽이 청소가 안 된 공간인 경우 -> 좌회전 후 이동
      if d == 0:
        print('current: north')
        if room[r][c-1] == 0:
          print('turn and go to west')
          turn_left()
          turn_count = 0
          c -= 1
          continue
        else:
          print('turn to west')
          turn_left()
          continue
      elif d == 1:
        print('current: east')
        if room[r-1][c] == 0:
          print('turn and go to north')
          turn_left()
          turn_count = 0
          r -= 1
          continue
        else:
          print('turn to north')
          turn_left()
          continue
      elif d == 2:
        print('current: south')
        if room[r][c+1] == 0:
          print('turn and go to east')
          turn_left()
          turn_count = 0
          c += 1
          continue
        else:
          print('turn to east')
          turn_left()
          continue
      else:
        print('current: west')
        if room[r+1][c] == 0:
          print('turn and go to south')
          turn_left()
          turn_count = 0
          r += 1
          continue
        else:
          print('turn to south')
          turn_left()
          continue
  # 사방 탐색을 진행한 결과 네 방향 모두가 청소가 이미 끝났거나 벽인 경우
  else:
    if d == 0:
      r += 1
      turn_count = 0
      continue
    elif d == 1:
      c -= 1
      turn_count = 0
      continue
    elif d == 2:
      r -= 1
      turn_count = 0
      continue
    else:
      c += 1
      turn_count = 0
      continue
############################################################
end_time = time.time()
print('time: ', end_time - start_time)