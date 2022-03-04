import time
'''
# 11399 ATM
# 11047. 동전 0
# 1541. 잃어버린 괄호 - 못풂
'''
start_time = time.time()
#######################################################
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
buy_cases = deque(map(int, input().split()))


#######################################################
end_time = time.time()
print('time: ', end_time - start_time)