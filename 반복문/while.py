"""
patterns = [1, 2, 3, 4, 5]

#for i in patterns:
    #print(i)

i = 0
while i < len(patterns):
    print(patterns[i])
    i += 1
"""

selected = '손'
while selected not in ['가위', '바위', '보']:
    selected = input('''가위, 바위, 보 중 하나를 입력하세요
> ''')

print("선택된 항목은 '{}'".format(selected))