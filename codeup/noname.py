'''
1번 통과한 목록(코드업 파이썬 100제) ※이하 통과 = 모범 답안과 유사한 방법으로 풀이
88, 91, 94, 95, 96
'''
'''
2번 통과한 목록(코드업 파이썬 100제)
'''
'''
3번 통과한 목록(코드업 파이썬 100제)
'''
'''
힌트 목록
97: O(n^2) 이내로 작성
'''
m = []
for _ in range(10):
  m.append(list(map(int, input().split())))
br = 1
for i in range(len(m)):
  if i == 0 or i == 9:
    continue
  for j in range(br, len(m[i])):
    if m[i][j] == 0:
      m[i][j] = 9
    elif m[i][j] == 1:
      if br != 9:
        br = j - 1
        break
    else:
      m[i][j] = 9
      br = 9
      break
for i in range(len(m)):
  for j in m[i]:
    print(j, end=' ')
  print()