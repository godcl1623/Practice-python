import time
'''
# 11399 ATM
people = int(input())
ttw = list(map(int, input().split()))
ttw.sort()
total_time = 0
next = 0
for i in ttw:
  next += i
  total_time += next
print(total_time)
'''
'''
# 11047. 동전 0
n, k = map(int, input().split())
coins = []
for _ in range(n):
  coins.append(int(input()))
coin_num = 0
idx = 0
while k != 0:
  if idx == len(coins):
    break
  if k - coins[::-1][idx] < 0:
    idx += 1
    continue
  k -= coins[::-1][idx]
  coin_num += 1
print(coin_num)
'''
'''
# 1541. 잃어버린 괄호 - 못풂
'''
start_time = time.time()
#######################################################

#######################################################
end_time = time.time()
print('time: ', end_time - start_time)