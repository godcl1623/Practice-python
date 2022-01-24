'''
# 그리디
11399(○), 11047(○), 1541(△)

# 구현
1966, 14891
'''
original_formula = input().split('-')
result = 0
for i in original_formula[0].split('+'):
	result += int(i)
for i in original_formula[1:]:
	for j in i.split('+'):
		result -= int(j)
print(result)