'''
# 그리디
1789(△), 10162(O), 1339(X) - https://hongcoding.tistory.com/76

# 구현
10872(O), 1924(△)

자료구조, 알고리즘별 문제 출제 방식 체크용 예제 1~2개 풀어보기
# 배열
# 큐
10845(O)
# 스택
3986(O)
# 링크드 리스트(= 연결 리스트)
2605(△) - 참조: https://heewon9809.tistory.com/264
# 해쉬
# 트리
# 힙
'''
'''
# 10845
import sys
cmds_num = int(sys.stdin.readline())
q = []
for i in range(cmds_num):
	cmd_input = sys.stdin.readline().split()
	if cmd_input[0] == 'push':
		q.append(int(cmd_input[1]))
	elif cmd_input[0] == 'pop':
		if len(q) == 0:
			print(-1)
		else:
			temp = q[0]
			del q[0]
			print(temp)
	elif cmd_input[0] == 'size':
		print(len(q))
	elif cmd_input[0] == 'empty':
		if len(q) == 0:
			print(1)
		else:
			print(0)
	elif cmd_input[0] == 'front':
		if len(q) == 0:
			print(-1)
		else:
			print(q[0])
	elif cmd_input[0] == 'back':
		if len(q) == 0:
			print(-1)
		else:
			print(q[-1])
'''
'''
# 3986
import sys
words_num = int(sys.stdin.readline())
count = 0
for _ in range(words_num):
	word = sys.stdin.readline().rstrip()
	stk = []
	for i in word:
		if len(stk) == 0:
			stk.append(i)
		else:
			if stk[-1] == i:
				del stk[-1]
			else:
				stk.append(i)
	if len(stk) == 0:
		count += 1
print(count)
'''
n = int(input())
cards = list(map(int, input().split()))
students = [i + 1 for i in range(n)]
order = {}
curr_idx = 0
while len(order.keys()) != len(students):
	order[curr_idx] = [curr_idx - cards[curr_idx], students[curr_idx]]
	curr_idx += 1
new_list = []
for i in order.values():
	new_list.insert(i[0], i[1])
for i in new_list:
	print(i, end=' ')
