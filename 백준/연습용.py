'''
# 그리디
1789(△), 10162(O), 1339(X) - https://hongcoding.tistory.com/76

# 구현
10872(O), 1924(△)

자료구조, 알고리즘별 문제 출제 방식 체크용 예제 1~2개 풀어보기
## 자료구조
# 배열
# 큐
10845(O)
# 스택
3986(O)
# 링크드 리스트(= 연결 리스트)
2605(△)
# 해쉬
9375(X) - 참조: https://hongcoding.tistory.com/60
# 트리
14425(X) - 참조: https://jinho-study.tistory.com/980
# 힙
## 알고리즘
# DFS
2210
# BFS
16948
'''
'''
# 9375(답안)
t = int(input())

for i in range(t):
	n = int(input())
	weardict = {}
	for j in range(n):
		wear = list(input().split())
		if wear[1] in weardict:
			weardict[wear[1]].append(wear[0])
		else:
			weardict[wear[1]] = [wear[0]]
	print(weardict)

	cnt = 1 # 각 종류마다 항목의 개수

	for k in weardict:
		cnt *= (len(weardict[k])+1)
	print(cnt-1)
'''
'''
# 14425(오답)
n, m = map(int, input().split())
count = 0

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self, head):
		self.head = head

	def save(self, value):
		self.current = self.head
		while True:
			if len(value) < len(self.current.value):
				if self.current.left != None:
					self.current = self.current.left
				else:
					self.current.left = Node(value)
					return
			elif len(value) > len(self.current.value):
				if self.current.right != None:
					self.current = self.current.right
				else:
					self.current.right = Node(value)
					return
			else:
				idx = 0
				while True:
					if ord(value[idx]) == ord(self.current.value[idx]):
						idx += 1
					elif ord(value[idx]) < ord(self.current.value[idx]):
						idx = 0
						if self.current.left != None:
							self.current = self.current.left
						else:
							self.current.left = Node(value)
							return
					else:
						idx = 0
						if self.current.right != None:
							self.current = self.current.right
						else:
							self.current.right = Node(value)
							return

	def search(self, value):
		global count
		self.current = self.head
		while self.current:
			if value == self.current.value:
				count += 1
				return True
			else:
				if len(value) < len(self.current.value):
					self.current = self.current.left
				elif len(value) > len(self.current.value):
					self.current = self.current.right
				else:
					idx = 0
					while self.current:
						if value == self.current.value:
							count += 1
							return True
						if ord(value[idx]) == ord(self.current.value[idx]):
							idx += 1
						elif ord(value[idx]) < ord(self.current.value[idx]):
							idx = 0
							self.current = self.current.left
						else:
							idx = 0
							self.current = self.current.right
		return False

root_node = Node(input())
tree = Tree(root_node)

for _ in range(n - 1):
	tree.save(input())

for _ in range(m):
	tree.search(input())

print(count)
'''
'''
# 14425
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = set([input().rstrip() for _ in range(n)])
cnt = 0
for _ in range(m):
	t = input().rstrip()
	if t in s:
		cnt += 1
print(cnt)
'''
