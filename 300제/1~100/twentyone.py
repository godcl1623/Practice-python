# 28 다시 풀기
'''
오답현황(~210730) - 3번씩 풀이
22~24, 27, 29: 1번
28: 2번
'''
# 21. 문자열 인덱싱: letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
'''
>> letters = 'python'

실행 예:
p t
'''
letters = 'python'
print(letters[0], letters[2])

# 22. 문자열 슬라이싱: 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요. (추가 조건: 단, 숫자 4는 사용하지 말것)
'''
>> license_plate = "24가 2210"
실행 예: 2210
'''
license_plate = "24가 2210"
print(license_plate[-4:]);

# 23. 023 문자열 인덱싱: 아래의 문자열에서 '홀' 만 출력하세요. (추가 조건: 조건문 쓰지 말것)(힌트: 슬라이스랑 비슷)
'''
>> string = "홀짝홀짝홀짝"
실행 예:
홀홀홀
'''
string = "홀짝홀짝홀짝"
print(string[::2]);

# 24. 024 문자열 슬라이싱: 문자열을 거꾸로 뒤집어 출력하세요. (추가 조건: 조건문 쓰지 말것)(힌트: 23번이랑 비슷)
'''
>> string = "PYTHON"
실행 예:
NOHTYP
'''
string = "PYTHON"
print(string[::-1])

# 25. 문자열 치환: 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
'''
>> phone_number = "010-1111-2222"
실행 예
010 1111 2222
'''
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))

# 26. 문자열 다루기: 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
'''
실행 예
01011112222
'''
print(phone_number.replace('-', ''))

# 27. 문자열 다루기: url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요. (힌트: 구분자를 기준으로 '나눈다')
'''
>> url = "http://sharebook.kr"
실행 예:
kr
'''
url = "http://sharebook.kr"
print(url.split('.')[1]);

# 28. 문자열은 immutable: 아래 코드의 실행 결과를 예상해보세요. (힌트: 한 번 더 생각해 볼 것, 틀린 이유와 함께 답이 떠오른게 아니면 무조건 틀렸음)
'''
>> lang = 'python'
>> lang[0] = 'P'
>> print(lang)
'''
# 오류 발생: 문자열은 이 방법으로 변경할 수 없음

# 29. replace 메서드: 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요. (추가 조건: 단, 조건문 사용하지 말 것)
'''
>> string = 'abcdfe2a354a32a'
실행 예:
Abcdfe2A354A32A
'''
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'));

# 30. replace 메서드: 아래 코드의 실행 결과를 예상해보세요.
'''
>> string = 'abcd'
>> string.replace('b', 'B')
>> print(string)
'''
# abcd(변하지 않는다)