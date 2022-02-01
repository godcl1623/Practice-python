# 1. 라이브러리를 사용하지 않은 경우
'''
  큐는 FIFO 기법으로 데이터를 추가/삭제한다
'''

# 1-1. FIFO 큐
q = []

# 큐에 데이터를 추가한다 = enqueue
def enq(data):
  q.append(data)

# 큐에서 데이터를 FIFO 순서로 제거(= dequeue)한 후 반환
def fiDeq():
  temp = q[0]
  del q[0]
  return temp

# 현재 큐에 추가된 데이터의 갯수를 반환
def qSize():
  return len(q)

'''
for i in range(10):
  enq(i)
print(qSize()) # 10
print(fiDeq()) # 0
print(fiDeq()) # 1
print(fiDeq()) # 2
print(qSize()) # 7
'''

# 1-2. LIFO 큐 - 공통되는 부분은 FIFO 큐 api 사용
def liDeq():
  temp = q[-1]
  del q[-1]
  return temp

'''
print(qSize()) # 10
print(liDeq()) # 9
print(liDeq()) # 8
print(liDeq()) # 7
print(qSize()) # 7
'''

# 1-3. Priority 큐 - 큐가 데이터 이외에 우선순위를 함께 저장함 -> 우선순위가 높은 순으로 dequeue

def penq(priority, data):
  q.append((priority, data))

def pdeq():
  tempLst = []
  for i in q:
    tempLst.append(i[0])
  maxIdx = max(tempLst)
  temp = q[tempLst.index(maxIdx)]
  del q[tempLst.index(maxIdx)]
  return temp

'''
prios = [3, 7, 1, 4, 6, 2, 5, 9, 8, 0]
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for i in range(10):
  penq(prios[i], data[i])
print(q)
for _ in range(10):
  print(pdeq())
'''

# 2. 라이브러리를 사용하는 경우
import queue

# 2-1. FIFO 큐
fq = queue.Queue()

# enque: put(데이터)
fq.put('data')

# deque: get()
print(fq.get()) # data

# 규모 체크: qsize()
print(fq.qsize()) # 0

# 2-2. LIFO 큐
lq = queue.LifoQueue()

# LIFO 큐는 기본적인 api는 FIFO 큐와 동일하지만, get()의 동작이 FIFO와 다르다

# 2-3. Priority 큐
pq = queue.PriorityQueue()

# Priority 큐 또한 api는 FIFO 큐와 동일하지만, 이번에는 put()의 동작이 FIFO와 다르다
pq.put((5, 'data')) # 우선순위, 데이터 쌍의 튜플을 인수로 전달해야 함

# 2-4. 기타 api
'''
  *Queue().empty(): 큐가 비어있는지 여부를 boolean 값으로 반환
  *Queue().full(): 큐가 가득 찼는지 여부를 boolean 값으로 반환
'''