# 1. print
print('안녕하세요')

# 2. 변수
var = '안녕하세요'
print(var)

# 3. if
if True:
    print(var)

# 4. ifelse
if True:
    print('nerf this')

elif False:
    print('Terf this')

else:
    print('derf this')

# 5. function
def testFunc(a, b, c):
    return a + b + c

print(testFunc(1, 3, 5))

# 6. 다중 return
def multiFunc(a, b, c):
    return a, b, c

foo, bar, derf = multiFunc(3, 2, 5)
print(foo, bar, derf)

# 7. format
base = 'select {} from {} where id={}'
column = '*'
table = 'formattutorial'
tableid = 785
print(base.format(column, table, tableid))

# 8. 여러줄 문자열
'''
여러줄
문자열과
주석의
차이는
'''

comment = """ 변수 할당 혹은
print로 직접
출력시켰는지
여부의
차이다
"""
print(comment)

# 9. 정수, 실수
original = 100.0
integer = int(original)
realnumber = float(integer)
print(original, integer, realnumber)

# 10. 사용자 입력 받기
input('계속하려면 Enter를 입력하세요 >')

# 11. 리스트
arr = [1, 2, 3, 4, 5]
"""
원소 더하기: arr.append(값) 혹은 arr + [값]
이 때 append의 값 자리로 다른 리스트를 넣으면 그 리스트 자체가 값이 돼버림 -> arr.append([값]) = [1, 2, 3, 4, 5, [값]]
원소 빼기: del arr[인덱스] 혹은 arr.remove(값)
원소 존재여부 확인: 값 in arr
"""
print(arr.append(6))
print(arr + [7])
del arr[3]
print(arr)
print(arr.remove(7))
print(9 in arr)