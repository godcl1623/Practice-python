##### 큐, 덱 #####
###큐###
"""
# 18258 큐 2 - 다시풀기: 시간초과 발생
'''
push: 정수를 큐에 추가
pop: 맨 앞의 정수를 빼고 그 수를 출력(수가 없으면 -1 출력)
size: 큐에 들어있는 정수 갯수 출력
empty: 큐가 비어있으면 1, 아니면 0
front: 큐의 가장 앞에 있는 정수 출력(없으면 -1)
back: 큐의 가장 뒤에 있는 정수 출력(없으면 -1)
'''
"""
"""
# 2164 카드2
'''
N장의 카드(1~N 표기, 1이 가장 위)
카드 한 장 남을 때까지 반복:
  (1) 제일 위 카드 버림
  (2) (1)을 제외한 후 가장 위에 있는 카드를 마지막으로 옮김
N이 주어졌을 때 가장 마지막에 남는 카드는?
'''
import sys;
from collections import deque;

cards = int(sys.stdin.readline());
queue = deque([]);

for i in range(1, cards + 1):
  queue.append(i);

while len(queue) != 1:
  queue.popleft();
  second = queue.popleft();
  queue.append(second);
print(queue[0]);
"""
"""
# 11866 요세푸스 문제 0 - 다시풀기: deque rotate 조사 요망
'''
N 명의 사람이 원을 이뤄 앉음
양의 정수 K 주어지면 K번째 사람을 제거하는걸 N명 모두 제거될 때까지 반복
원에서 사람들이 제거되는 순서를 (N, K) -> 요세푸스 순열
예를 들어 (7, 3) 요세푸스 순열은 3, 6, 2, 7, 5, 1, 4
1234567
124567 -> 456712
12457 -> 71245
1457 -> 4571
145
14
4
'''
import sys;
from collections import deque;

yo = sys.stdin.readline().split();
queue = deque([]);

for i in range(1, int(yo[0]) + 1):
  queue.append(i);

result = [];
crit = queue.index(int(yo[1]));
while len(queue) != 0:
  queue.rotate(-crit);
  popped = queue.popleft();
  result.append(str(popped));
print(f"<{', '.join(result)}>");
"""
# 1966번 프린터 큐 - 다시풀기: 오답
'''
프린터는 기본적으로 FIFO
새로운 소프트웨어 만듦
  1. 큐 중요도 확인 -> 우선순위 큐
  2. 큐 첫 번째 원소보다 우선순위 높은 원소 뒤에 존재 -> 첫 번째 원소 맨 뒤로 재배치
  3. 큐 첫 번째 원소가 우선순위 가장 높음 -> 인쇄
'''
'''
# 잘못된 풀이
import sys;
from collections import deque;

casenum = int(sys.stdin.readline());
cases = [];
queue = deque([]);
for i in range(casenum):
  docus, target = map(int, sys.stdin.readline().split());
  prios = list(map(int, sys.stdin.readline().rsplit()));
  cases.append([docus, target, prios]);

for i in cases:
  for j in range(i[0]):
    queue.append(i[2][j]);
  initVal = queue[i[1]];
  count = queue.count(initVal);
  rotated = 0;
  temp = [];
  maxPrio = max(queue);
  while len(queue) != 0:
    maxPrio = max(queue);
    if queue[0] == maxPrio:
      printed = queue.popleft();
      temp.append(printed);
    else:
      queue.rotate(-1);
      if count != 1:
        rotated += 1;
  if rotated == 0:
    print(temp.index(initVal) + 1);
  else:
    print(len(temp) - rotated + 1);
'''
'''
# 정답
test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split( )))
    imp = list(map(int, input().split( )))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0
    
    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if imp[0]==max(imp):
            order += 1
                        
            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0]=='target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0)) 
'''
