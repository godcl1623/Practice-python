# 15부터 다시 풀기
# 11. 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
print(10 * 삼성전자)

# 12. 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.(https://wikidocs.net/7021) - 단, 문자열 없음
시가총액 = '298조'
현재가 = 50000
PER = 15.79

# 13. 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.(s = "hello"; t = "python") 두 변수를 이용하여 아래와 같이 출력해보세요.(hello! python)
s = 'hello'
t = 'python'
print('{}! {}'.format(s, t))

# 14. 아래 코드의 실행 결과를 예상해보세요.
print(2 + 2 * 3 )
# 8

# 15. type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
'''
>> a = 128
>> print (type(a))
<class 'int'>
'''
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
a = "132"
print(type(a))

# 16. 문자열 '720'를 정수형으로 변환해보세요.
target = '720'
result = int(target)
print(result, type(result))

# 17. 정수 100을 문자열 '100'으로 변환해보세요.
target = 100
result = str(target)
print(result, type(result))

# 18. 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
target = '15.79'
result = float(target)
print(result, type(result))

# 19. year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = '2021'
result = int(year)
print(result - 2, result - 1, result)

# 20. 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
월납부액 = 48584
개월 = 36
총금액 = 월납부액 * 개월
print(총금액)