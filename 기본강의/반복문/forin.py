arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for element in arr:
    print(element + 1)

for elements in range(len(arr)):
    anarr = arr[elements]
    print('카운트 시작: {}'.format(anarr))

for elements in range(5):
    print('우왕ㅋ굳ㅋ')

for i, elem in enumerate(arr):
    print('{}번: {}'.format(i+1, elem))