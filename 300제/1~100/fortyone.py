# 45번 다시 풀기(210628)
'''
오답 현황(~210628)
45번 - 2번
47번 - 1번
'''
# 41. upper 메서드
'''
다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.

ticker = "btc_krw"
'''
ticker = "btc_krw"
print(ticker.upper())

# 42. lower 메서드
'''
다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.

ticker = "BTC_KRW"
'''
ticker = "BTC_KRW"
print(ticker.lower())

# 43. capitalize 메서드: 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
hello = 'hello'
print(hello.capitalize())

# 44. endswith 메서드
'''
파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.

file_name = "보고서.xlsx"
'''
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

# 45. endswith 메서드
'''
파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.

file_name = "보고서.xlsx"
'''
file_name = "보고서.xlsx"


# 46. startswith 메서드
'''
파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.

file_name = "2020_보고서.xlsx"
'''
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

# 47. split 메서드
'''
다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.(단, ' '는 사용하지 말 것)

a = "hello world"
'''
a = "hello world"


# 48. split 메서드
'''
다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.

ticker = "btc_krw"
'''
ticker = "btc_krw"
print(ticker.split('_'))

# 49. split 메서드
'''
다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.

date = "2020-05-01"
'''
date = "2020-05-01"
splitdate = date.split('-')
for target in splitdate:
    year, month, day = splitdate
print(f'년도: {year}, 월: {month}, 일: {day}')

# 50. rstrip 메서드
'''
문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.

data = "039490     "
'''
data = "039490     "
print(data.rstrip())