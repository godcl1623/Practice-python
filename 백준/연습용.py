'''
# 그리디
11399(○), 11047(○), 1541(△)

# 구현
1966(△), 14891
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
