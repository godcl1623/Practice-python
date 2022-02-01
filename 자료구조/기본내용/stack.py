# 스택: LIFO 구조로 데이터를 입출력하는 자료구조

# 1. 라이브러리 없이 구현
stk = []

# 1-1. 스택에 데이터 추가
def spush(data):
  stk.append(data)

# 1-2. 스택에서 데이터 추출: 마지막에 들어간 데이터부터 추출
def spop():
  temp = stk[-1]
  del stk[-1]
  return temp
'''
for i in range(10):
  print('add: ', i)
  spush(i) # 0 ~ 9 순서로 추가
print('current size: ', len(stk)) # 10
for _ in range(10):
  print(spop()) # 9 ~ 0 순서로 출력
'''

# 2. 라이브러리 사용
'''
  스택의 경우 큐와 달리 별도의 라이브러리가 존재하지 않음 -> collections 모듈의 deque 이용
  deque: 양방향으로 데이터 입출력 가능 -> 큐 및 스택 모두 구현 가능
    일반적인 리스트는 양 끝 엘리먼트의 삽입/제거에 걸리는 시간이 O(n)
    deque의 경우 O(1)이므로, 큐와 스택은 deque를 이용할 것
'''
from collections import deque
deq = deque()

# 데이터 추가
deq.append('foo') # 자료형의 끝에 데이터 추가
deq.appendleft('bar') # 자료형의 처음에 데이터 추가

# 데이터 제거
deq.popleft() # 자료형 맨 앞의 데이터 제거
deq.pop() # 자료형 맨 끝의 데이터 제거

'''
  append + popleft => 큐처럼 동작
  append + pop => 스택처럼 동작
'''

# 기타 api
deq.remove('foo') # 자료형에서 입력된 데이터를 찾은 후 제거
deq.rotate(1) # deque를 입력된 숫자 만큼 회전 - 양수면 오른쪽, 음수면 왼쪽