'''
# 오답 및 풀이 현황
617. Merge Two Binary Trees X(3/6)
938. Range Sum of BST △(3/6)
897. Increasing Order Search Tree(3/6)
104. Maximum Depth of Binary Tree(3/6)
'''
import time
start_time = time.time()
##################################################
from collections import deque
q = deque((1, 2))
a, b = q.popleft(), q.popleft()
print(type(a))
##################################################
end_time = time.time()
print('time: ', end_time - start_time)