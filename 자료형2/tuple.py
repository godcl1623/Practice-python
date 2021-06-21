diction = {'첫번째': 1, '두번째': 2, '세번째': 3, '네번째': 4, '다섯번째': 5}

# 원본 코드
"""for key, value in diction.items():
    print('{} 수는 {}'.format(key, value))"""

# 튜플 사용
for tupleParam in diction.items():
    print('{} 수는 {}'.format(*tupleParam))