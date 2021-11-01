'''
코드업 #6096
O(n^2) 이하로 줄일 방법 찾기(현재: O(n^3))
go = []
for i in range(19):
  go.append(list(map(int, input().split())))
cnt = int(input())
co = []
for i in range(cnt):
  co.append(list(map(int, input().split())))
for i in range(len(go)):
  for j in co:
    if go[i][j[1] - 1] == 1:
      go[i][j[1] - 1] -= 1
    elif go[i][j[1] - 1] == 0:
      go[i][j[1] - 1] += 1
    if i == j[0] - 1:
      for k in range(len(go[i])):
        if go[i][k] == 0:
          go[i][k] += 1
        else:
          go[i][k] -= 1
  for l in go[i]:
    print(l, end=' ')
  print()
# 루프를 돌 때 리스트.index(변수)로 변수의 인덱스를 구하려 할 때 변수 값의 구성이 동일하면 인덱스가 정상적으로 캐치되지 않는 것 같음
'''
'''
코드업 #6097
h, w = map(int, input().split())
board = []
for i in range(h):
  board.append([0 for i in range(w)])
stk_num = int(input())
for _ in range(stk_num):
  l, d, x, y = map(int, input().split())
  count = 0
  for i in range(len(board)):
    if d == 0:
      if i == x - 1:
        for j in range(len(board[i])):
          if y-1 <= j and count < l:
            board[i][j] = 1
            count += 1
    else:
      if i >= x - 1:
        for j in range(len(board[i])):
          if j == y - 1 and count < l:
            board[i][j] = 1
            count += 1
for i in range(len(board)):
  for j in range(len(board[i])):
    print(board[i][j], end=' ')
  print()
'''
'''
코드업 #6098
maze = []
for i in range(10):
  maze.append(list(map(int, input().split())))
last = 0
for i in range(len(maze)):
  if i == 0 or i == 9:
    continue
  for j in range(len(maze[i])):
    if j == 0 or j == 9:
      continue
    if last == 0:
      if maze[i][j] == 0:
        maze[i][j] = 9
        last = j
      elif maze[i][j] == 1:
        break
      elif maze[i][j] == 2:
        last = 9
        maze[i][j] = 9
        break
    elif j >= last:
      if maze[i][j] == 0:
        maze[i][j] = 9
        last = j
      elif maze[i][j] == 1:
        break
      elif maze[i][j] == 2:
        last = 9
        maze[i][j] = 9
        break
for i in range(len(maze)):
  for j in range(len(maze[i])):
    print(maze[i][j], end=' ')
  print()
'''