'''
1번 통과한 목록(코드업 파이썬 100제) ※이하 통과 = 모범 답안과 유사한 방법으로 풀이
8, 18, 24, 42, 46, 47, 52, 53, 58, 60, 61, 62, 64, 74, 79, 81, 84, 87, 91, 94, 97, 98
'''
'''
2번 통과한 목록(코드업 파이썬 100제)
6, 7, 17, 20, 25, 26, 27, 28, 29, 30, 31, 33, 38, 48, 54, 70, 75, 76, 78, 82, 85, 88, 95, 96
'''
'''
3번 통과한 목록(코드업 파이썬 100제)
'''
'''
힌트 목록
18: f-string 사용하지 말고 풀어보기
24: f-string, sep 제외
42, 44: :.*f 제외
52, 53: 부등호 제외
63: 두 수 중 후자가 큰 경우를 제외하면 모두 전자가 표시되도록 작성
81: 3줄로 작성
87: 꼭 print를 사용할 필요는 없음
94: 모든 input을 활용할 것
97: O(n^2) 이내로 작성
'''
'''
22.01.10 오답
27, 29, 42~43, 46, 52~53, 56~57, 59~63, 78~79, 82, 84~90
'''
# a, b = map(int, input().split())
# a = int(input())
# a = input()
# a, b, c = map(int, input().split())
# a = list(map(int, input().split()))
# a, b, c, d = map(int, input().split())
# print(min(numsList))
field = [list(map(int, input().split())) for i in range(10)]
x, y = 1, 1
for i in range(1, len(field)):
  for j in range(x, len(field[i])):
    if field[i][j] == 0:
      field[i][j] = 9
    elif field[i][j] == 1:
      x = j - 1
      break
    elif field[i][j] == 2:
      field[i][j] = 9
      x = len(field[i])
      break
for i in range(len(field)):
  for j in range(len(field)):
    print(field[i][j], end=' ')
  print()