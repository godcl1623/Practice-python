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
2210(X)
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
# from collections import deque
# import sys
# input = sys.stdin.readline
# r, c = map(int, input().split())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# map = [list(input().rstrip()) for _ in range(r)]
# empty_map = [[0] * c for _ in range(r)]
# sheep = 0
# wolf = 0
# def bfs(x, y):
# 	q = deque()
# 	q.append((x, y))
# 	empty_map[x][y] = 1
# 	wolf_res, sheep_res = 0, 0
# 	while q:
# 		x, y = q.popleft()
# 		if map[x][y] == 'v':
# 			wolf_res += 1
# 		elif map[x][y] == 'k':
# 			sheep_res += 1
# 		for i in range(4):
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 			if 0 <= nx < r and 0 <= ny < c:
# 				if map[nx][ny] != '#' and not empty_map[nx][ny]:
# 					empty_map[nx][ny] = 1
# 					q.append((nx, ny))
# 	if wolf_res >= sheep_res:
# 		sheep_res = 0
# 	else:
# 		wolf_res = 0
# 	return [wolf_res, sheep_res]

# for i in range(r):
# 	for j in range(c):
# 		if map[i][j] != '#' and not empty_map[i][j]:
# 			wolf_res, sheep_res = bfs(i, j)
# 			wolf += wolf_res
# 			sheep += sheep_res
# print(wolf, sheep)
# r, c = map(int, input().split())
# map = [list(input()) for _ in range(r)]
# sheep = []
# wolf = []
# result = []
# def dfs(x, y):
# 	if x <= -1 or x >= r or y <= -1 or y >= c:
# 		return False
# 	if map[x][y] != '#':
# 		result.append(map[x][y])
# 		map[x][y] = '#'
# 		dfs(x + 1, y)
# 		dfs(x - 1, y)
# 		dfs(x, y + 1)
# 		dfs(x, y - 1)
# 		return True
# 	return False
# for i in range(r):
# 	for j in range(c):
# 		if map[i][j] != '#':
# 			dfs(i, j)
# 			if result.count('v') < result.count('k'):
# 				sheep.append(result.count('k'))
# 			else:
# 				wolf.append(result.count('v'))
# 			result = []
# print(sum(sheep), sum(wolf))

# r, c = map(int, input().split())
# map = [list(input()) for _ in range(r)]
# sheep = 0
# wolf = 0
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def dfs(x, y):
# 	if map[x][y] == 'v':
# 		wolf += 1
# 	elif map[x][y] == 'k':
# 		sheep += 1
# 	for i in range(4):
# 		nx = x + dx[i]
# 		ny = y + dy[i]
# 		if 0 <= nx < r and 0 <= ny < c:
# 			dfs(nx, ny)
# for i in range(r):
# 	for j in range(c):
# 		dfs(i, j)
# print(sheep, wolf)
'''
# 2022-03-14 DFS 오답 대상: 백준 2606
# num = int(input())
# case = int(input())
# coms = [[] for _ in range(num + 1)]
# infected = [False for _ in range(num + 1)]
# infected[0] = True
# def dfs(coms, start, infected):
# 	if start > num:
# 		return
# 	if infected[start - 1] == True:
# 		dfs(coms, start + 1, infected)
# 	else:
# 		for i in coms:
# 			if start == i[1]:
# 				if infected[i[0] - 1] == True:
# 					infected[start - 1] = True
# 		dfs(coms, start + 1, infected)
# dfs(coms, 1, infected)
# print(infected.count(True) - 1)
# def dfs(coms, start, visited):
# 	global cnt
# 	visited[start] = True
# 	for i in coms[start]:
# 		if not visited[i]:
# 			cnt += 1
# 			dfs(coms, i, visited)
# cnt = 0

# for i in range(case):
# 	node1, node2 = map(int, input().split())
# 	coms[node1].append(node2)
# 	coms[node2].append(node1)
# 	print(coms)
# dfs(coms, 1, infected)
# print(infected)
# print(cnt)
'''
s = "RLRRLLRLRL"
st = 0
cnt = 0
rs = 0
ls = 0
while len(s) > 0:
		for i in range(len(s)):
				if rs > 0 and ls > 0 and rs == ls:
						break
				if s[i] == 'R':
						rs += 1
				else:
						ls += 1
		st = rs + ls
		s = s[st:]
		rs = 0
		ls = 0
		cnt += 1
print(cnt)