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
# 2217
'''
# 오답
ropes_num = int(input())
ropes = []
for _ in range(ropes_num):
	ropes.append(int(input()))
if min(ropes) * ropes_num >= max(ropes):
	print(min(ropes) * ropes_num)
else:
	print(max(ropes))
'''
'''
# 오답 2
ropes_num = int(input())
ropes = []
for _ in range(ropes_num):
	ropes.append(int(input()))
count = 1
idx = 0
max_idx = ropes_num
max = max(ropes)
while count <= ropes_num:
	if ropes[idx] * count > max:
		max = ropes[idx] * count
	else:
		if idx != max_idx - 1:
			idx += 1
		else:
			idx = 0
			max_idx -= 1
			count += 1
print(max)
'''
'''
힌트: 가장 작은 무게를 들 수 있는 로프가 들 수 있는 질량 * 병렬 연결 로프 갯수 = 최종 무게
'''
'''
# 정답
ropes_num = int(input())
ropes = []
for _ in range(ropes_num):
	ropes.append(int(input()))
ropes.sort(reverse=True)
max = max(ropes)
for i in range(len(ropes)):
	comp = ropes[i] * (i + 1)
	if comp > max:
		max = comp
print(max)
'''
'''
# 10817(구현)
# 정답
nums = list(map(int, input().split()))
biggest = max(nums)
nums.remove(biggest)
print(max(nums))
'''
