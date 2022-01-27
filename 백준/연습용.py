'''
# 그리디
11399(○), 11047(○), 1541(△)

# 구현
1966(△), 14891(X)
'''
'''
# 1966: 로직 자체는 맞는데, remove 대신 pop을 써야함 + docs는 필요 없음
cases = int(input())
for _ in range(cases):
	num_of_docs, curr_doc_idx = map(int, input().split())
	docs = [i for i in range(num_of_docs)]
	prios = list(map(int, input().split()))
	curr_prio = prios[curr_doc_idx]
	curr_prio_idx = prios.index(curr_prio)
	order = 1
	while True:
		if prios[0] == max(prios):
			if prios[0] == curr_prio and docs[0] == curr_prio_idx:
				break
			else:
				prios.remove(prios[0])
				docs.remove(docs[0])
				order += 1
		else:
			reorder_docs = docs[0]
			docs.remove(reorder_docs)
			docs.append(reorder_docs)
			reorder_prios = prios[0]
			prios.remove(reorder_prios)
			prios.append(reorder_prios)
	print(order)
	'''
'''
# 14891
잘못 생각한 점
1. 문제 이해 관련
	옆에 톱니와 극성이 다름 -> 계속 루프 돌며 회전하면 됨
	나는 건너뛰어서 회전시키려고 함 -> 잘못 이해한 점
2. for vs while
	for로 루프를 작성할 경우, 메모리에 저장된 내역과 루프를 돌아야 하는 내역이 달라 value error 발생
	ex)
		10101111
		01111101
		11001110
		00000010
		2
		3 -1
		1 1
		위 예제에서 (3, -1) 회전을 진행하면 맨 마지막 톱니가 00000001로 변하는데,
		for 루프를 도는 대상 리스트는 마지막 톱니가 00000010으로 저장된 상태에서 루프를 계속 돌게되기 때문에 불일치가 발생, value error의 원인이 되는 것으로 보임
'''
gears = [list(input()) for _ in range(4)]
turns = int(input())
def rotate(gear_idx, dir):
	if dir == 1:
		temp = gears[gear_idx][-1]
		del gears[gear_idx][-1]
		gears[gear_idx].insert(0, temp)
	else:
		temp = gears[gear_idx][0]
		del gears[gear_idx][0]
		gears[gear_idx].append(temp)
attempt = 1
for _ in range(turns):
	gear_idx, dir = map(int, input().split())
	histdir = dir
	curr_idx = gear_idx  - 1
	while curr_idx < 3:
		if gears[curr_idx + 1][6] != gears[curr_idx][2]:
			histdir *= -1
			rotate(curr_idx + 1, histdir)
			curr_idx += 1
		else:
			break
	curr_idx = gear_idx - 1
	while curr_idx > 0:
		if gears[curr_idx - 1][2] != gears[curr_idx][6]:
			histdir *= -1
			rotate(curr_idx - 1, histdir)
			curr_idx -= 1
		else:
			break
	curr_idx = gear_idx - 1
	rotate(curr_idx, dir)
score = 0
for i in range(len(gears)):
	score += (int(gears[i][0]) * (2 ** i))
print(score)