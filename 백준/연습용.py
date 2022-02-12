'''
# 그리디
1789(△), 10162(O), 1339(X) - https://hongcoding.tistory.com/76

# 구현
10872(O), 1924(△)

자료구조, 알고리즘별 문제 출제 방식 체크용 예제 1~2개 풀어보기
'''
'''
# 1339 정답
import sys
word_nums = int(sys.stdin.readline())
words_list = []
for _ in range(word_nums):
	words_list.append(sys.stdin.readline().rstrip())
words_vals = {}
for i in range(word_nums):
	for j in range(len(words_list[i])):
		if words_list[i][j] in words_vals:
			words_vals[words_list[i][j]] += 10 ** (len(words_list[i]) - 1 - j)
		else:
			words_vals[words_list[i][j]] = 10 ** (len(words_list[i]) - 1 - j)
numsList = []
for value in words_vals.values():
	numsList.append(value)
numsList.sort(reverse=True)
sum = 0
curr_num = 9
for num in numsList:
	sum += num * curr_num
	curr_num -= 1
print(sum)
'''
# 2007
import sys
m, d = map(int, sys.stdin.readline().split())
last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
init_date_idx = d % 7
if m == 1:
	print(date[init_date_idx])
elif m > 1 and m <= 3:
	init_date_idx += 3
	print(date[init_date_idx % 7])
else:
	init_date_idx += 3
	new_last_day = last_day[2:m - 1]
	thirty_ones = new_last_day.count(31)
	thirties = new_last_day.count(30)
	init_date_idx += (3 * thirty_ones) + (2 * thirties)
	print(date[init_date_idx % 7])