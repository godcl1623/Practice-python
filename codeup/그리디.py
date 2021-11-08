'''
2001. 최소 대금(O)
pastas = []
for i in range(3):
  pastas.append(int(input()))
juices = []
for i in range(2):
  juices.append(int(input()))
set_price = min(pastas) + min(juices)
print(f'{set_price * 1.1:.1f}')
'''
'''
3301. 거스름돈(O)
lefts = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
lefts.sort()
target = int(input())
count = 0
for i in lefts[::-1]:
  whole = target // i
  if whole > 0:
    target -= whole * i
    count += whole
  if target == 0:
    break
print(count)
'''
'''
3321. 최고의 피자(△): 풀긴 풀었는데 너무 오래 걸림, 오답 발생(2번?) - 문제 이해 못함
n = int(input()) # 토핑
a, b = map(int, input().split()) # 도우 가격, 토핑 가격
c = int(input()) # 도우 칼로리, 이 아래는 토핑 각각 칼로리
tops = [] # 토핑 칼로리 모음
for _ in range(n):
  tops.append(int(input()))
tops.sort()
# 최고의 피자 = 달러 당 열량이 최대
# 같은 토핑은 최대 2개까지
max_cal = 0
start = 0
end = start + 1
while True:
  if start == len(tops):
    break
  pizza_price = a + b * (end - start)
  pizza_cal = c + sum(tops[start:end])
  cal_per_price = int(pizza_cal / pizza_price)
  if max_cal <= cal_per_price:
    max_cal = cal_per_price
  end += 1
  if end > len(tops):
    start += 1
    end = start + 1
print(max_cal)
'''
'''
3120. 리모컨(△): 풀긴 풀었는데 너무 오래 걸림, 오답 발생
current, target = map(int, input().split())
count = 0
while current != target:
  print('count: ', count)
  print('current: ', current)
  count += 1
  if 1 <= abs(abs(target - current) - 10) < 3:
    if current <= target:
      current += 10
    else:
      current -= 10
  elif 1 <= abs(abs(target - current) - 5) < 3:
    if current <= target:
      current += 5
    else:
      current -= 5
  elif 1 <= abs(abs(target - current) - 1) < 3:
    if current <= target:
      current += 1
    else:
      current -= 1
  else:
    if abs(target - current) >= 10:
      if current <= target:
        current += 10
      else:
        current -= 10
    elif abs(target - current) >= 5:
      if current <= target:
        current += 5
      else:
        current -= 5 
    else:
      if current <= target:
        current += 1
      else:
        current -= 1 
print(count)
'''
'''
4763. 원숭이: 못풂
'''
import time
start_time = time.time()
##############################################

##############################################
end_time = time.time()
print('time: ', end_time - start_time)