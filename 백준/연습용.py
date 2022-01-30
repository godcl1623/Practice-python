'''
# 그리디
1789(△), 10162(O)

# 구현
10872(O)
'''
'''
# 10162
t = int(input())
a, b, c = 300, 60, 10
cnt_a, cnt_b, cnt_c = 0, 0, 0
if t % c != 0:
	print(-1)
else:
	while t != 0:
		if t >= a:
			t -= a
			cnt_a += 1
		elif t >= b:
			t -= b
			cnt_b += 1
		else:
			t -= c
			cnt_c += 1
	print(cnt_a, cnt_b, cnt_c)
'''
'''
# 10872
n = int(input())
elmts = [i for i in range(1, n + 1)]
result = 1
for i in elmts:
	result *= i
print(result)
'''