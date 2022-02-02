# 0. 해쉬 테이블
'''
    - 해쉬: 임의 값을 고정 길이로 변환
    - 해쉬 테이블: 키 값 연산에 의해 직접 접근이 가능한 데이터 구조
    - 해싱 함수: 키에 대한 산술 연산을 이용해 데이터 위치를 찾는 함수
    - 해쉬 값(= 해쉬 주소): key를 해싱 함수로 연산한 결과
        - 해쉬 테이블에서 해당 key 값의 위치 일관성 있게 찾을 수 있음
    - 슬롯: 한 개의 데이터를 저장할 수 있는 공간
'''

# 1. 해쉬 테이블 기본 형태
'''
    해쉬 테이블: 슬롯 + 슬롯 지칭할 해쉬 값 필요
    리스트 원소 자리 하나가 데이터가 저장되는 슬롯의 역할
    리스트 인덱스 = 슬롯을 호출하는 해쉬 값
'''
from audioop import add


hash_table_example = list([0 for i in range(10)])

# 2. 해쉬 함수
'''
    - 가장 간단한 방식은 Division 법: 나눗셈 후의 나머지를 사용하는 기법
        -> key 값이 무엇이 됐던 특정 숫자로 나눈 나머지 반환 => 일정한 길이의 해쉬값 도출
    - 아래 hash() 함수는 파이썬 내부적으로 제공하는 해싱 함수지만, 실행할 때마다 값이 달라질 수 있음
    - make_address()의 경우 입력된 key를 8로 나눈 나머지를 해쉬 값으로 사용하게 만드는 해싱 함수임
'''
def make_key_example(data):
    return hash(data)

def make_address_example(key):
    return key % 8

# 3. 해쉬 테이블에 데이터 저장 예시
# 3-1. 저장될 데이터에 대한 Key 생성 방법 정의
'''
    - 해쉬 테이블에 저장할 데이터는 영문 문자열로 한정하며, 첫 글자의 ASCII 코드를 Key로 사용한다.
    - 변수명 rawKey의 경우 강의안에서는 data로 작성됐지만, 실제 수행하는 역할과 변수명이 일반적으로 뜻하는 의미가 맞지 않다고 생각해 rawKey로 작성함.
'''
rawKey1 = 'Andy' # ord(A) = 65
rawKey2 = 'Dave' # ord(D) = 68
rawKey3 = 'Trump' # ord(T) = 84

# 3-2. 주어진 데이터, 키를 사용해 해쉬 테이블에 값 저장
def storage_example(rawKey, value):
    key = ord(rawKey[0])
    address = make_address_example(key)
    hash_table_example[address] = value

storage_example(rawKey1, 'foo')
print(hash_table_example) # [0, 'foo', 0, 0, 0, 0, 0, 0, 0, 0]

# 3-3. 해쉬 테이블에서 특정 주소의 데이터 불러오기
'''

'''
def get_example(rawKey):
    key = ord(rawKey[0])
    address = make_address_example(key)
    return hash_table_example[address]

print(get_example(rawKey1)) # foo

# 4. 충돌 해결 알고리즘
'''
    - (해쉬)충돌: 해쉬 테이블의 가장 큰 문제 - 어떠한 값을 동일한 주소에 저장하려는 경우 발생
    - 해결 방법
        1. Chaining 기법: 충돌 발생 시 해당 주소에서 링크드 리스트를 사용해 데이터를 추가로 뒤에 연결시켜 저장
            => 저장공간 외의 공간을 활용(= 개방 해싱)
        2. Linear Probing 기법: 충돌이 발생한 address의 바로 다음 address부터 맨 처음 나오는 빈 공간에 저장하는 기법
            => 저장공간 안에서 충돌 문제를 해결(= 폐쇄 해싱)
        3. 해쉬 함수 재정의 및 해쉬 테이블 저장공간 확대
'''

'''
case #1 chaining 기법의 경우

# 1. 데이터 저장 함수
def store_data(data, value):
    # (1) key, address를 생성한다
    key = make_key(data)
    hash_address = make_address(key)
    # (2) (1)에서 도출된 주소에 값이 저장된 상태인지 체크한다. 만약 이미 값이 존재하는 경우(= 주소 충돌이 발생한 경우):
    if hash_table[hash_address] != 0:
        # (3) 해당 주소에 존재하는 리스트 내 원소를 모두 체크한다. 
        for index in range(len(hash_table[hash_address])):
            # (4) 현재 루프에서 체크하는 리스트 내 데이터의 key가 새롭게 입력된 key와 동일한 경우(= 이미 존재하는 key가 입력된 경우 - 주소 충돌과 별개)
            if hash_table[hash_address][index][0] == key:
                # (5) 일치하는 key의 value를 새로 입력된 value로 업데이트한다.
                hash_table[hash_address][index][1] = value
                return
        # (6) 입력된 key가 리스트에 존재하지 않을 경우, 리스트에 새로운 key, value 쌍을 추가한다.
        hash_table[hash_address].append([key, value])
    # (7) 입력된 주소에 값이 저장되지 않았을 경우, key, value 쌍을 저장하는 이차원 리스트를 해당 주소에 할당한다.
    else:
        hash_table[hash_address] = [[key, value]]

# 2. 데이터 열람 함수
def read_data(data):
    # (1) 입력된 data(혹은 rawKey)를 key, address로 변환
    key = make_key(data)
    hash_address = make_address(key)
    # (2) 입력된 address에 값이 저장된 경우:
    if hash_table[hash_address] != 0:
        # (3) 해당 address에 저장된 리스트 원소를 체크한다:
        for index in range(len(hash_table[hash_address])):
            # (4) 만약 저장된 데이터 중 입력된 key와 일치하는 데이터가 있는 경우(= 찾으려는 데이터가 존재하는 경우)
            if hash_table[hash_address][index][0] == key:
                # (5) 해당 주소에 저장된 데이터를 반환한다.
                return hash_table[hash_address][index][1]
        # (6) 입력된 data를 기반으로 하는 key가 존재하지 않는 경우(= 찾으려는 데이터가 존재하지 않음), 아무것도 반환하지 않는다.
        print('검색 결과가 존재하지 않습니다')
        return None
    # (7) 입력된 address에 저장된 값이 없는 경우, 해당 내용을 반환한다.
    else:
        print('저장된 데이터가 없습니다')
        return None
'''

'''
case #2 linear probing 기법

# 1. 데이터 저장 함수
def store_data(data, value):
    # (1) 주어진 data를 활용해 key, address 생성
    key = make_key(data)
    hash_address = make_address(key)
    # (2) 입력된 address에 이미 데이터가 저장된 경우:
    if hash_table[hash_address] != 0:
        # (3) 해당 주소부터 해쉬 테이블 내 남은 원소들에 대해 빈 주소가 있는지 탐색한다:
        for index in range(hash_address, len(hash_table)):
            # (4) 이번 루프에 해당되는 주소에 아무런 값도 저장되지 않은 경우
            if hash_table[index] == 0:
                # (5) 해당 주소에 key, value 쌍을 저장한다
                hash_table[index] = [key, value]
            # (6) 이번 루프에 해당되는 주소에 저장된 값의 key가 새로 입력된 key와 동일한 경우
            elif hash_table[index][0] == key:
                # (7) 저장된 value를 새로 입력된 value로 수정한다
                hash_table[index][1] = value
    # (8) 입력된 address에 데이터가 저장되지 않은 경우, key, value 쌍을 새로 저장한다.
    else:
        hash_table[hash_address] = [key, value]

# 2. 데이터 열람 함수
def read_data(data):
    # (1) 주어진 데이터로 key, adress 변환
    key = make_key(data)
    hash_address = make_address(key)
    # (2) 입력된 address에 데이터가 저장된 경우
    if hash_table[hash_address] != 0:
        # (3) 해당 주소부터 해쉬 테이블의 남은 원소들에 대해 탐색을 진행한다
        # 데이터 저장 시점에 충돌이 발생했기 때문에, address만으로는 어느 위치에 저장됐는지 알 수 없기 때문
        for index in range(hash_address, len(hash_table)):
            # (4) 입력된 key를 발견한 경우
            if hash_table[index][0] == key:
                # (5) 해당 key에 저장된 value를 반환한다
                return hash_table[index][1]
            # (6) 입력된 key를 찾을 수 없는 경우, 관련 메세지를 반환한다.
            else:
                print('검색 결과가 존재하지 않습니다')
                return None
    # (7) 입력된 address에 데이터가 저장되지 않은 경우, 관련 메세지를 반환한다.
    else:
        print('저장된 데이터가 없습니다')
        return None;
'''

'''
case #3 해쉬 함수 재정의, 해쉬 테이블 확대 = 공간과 탐색 시간의 교환

# 해쉬 테이블의 사이즈 자체를 늘림(range(10) -> range(16))
hash_table = list([0 for i in range(16)])

# 늘어난 사이즈 만큼 주소를 만들 때 나눠주는 숫자도 늘림(8 -> 16)
def make_address(key):
    return key % 16
'''

'''
case #4 sha256(해시 알고리즘) 사용 방법

# 1. 해싱 함수 관련 모듈 import
import hashlib

# 2. 해쉬 테이블 생성
hash_table = list([0 for i in range(8)])

# 3. key 함수에 알고리즘 적용
def make_key(data):
    # (1) 불러올 알고리즘을 할당한다.
    logic = hashlib.sha256()
    # (2) sha256 내 update() 메서드로 주어진 문자열을 해싱한다.
    # 문자열.encode()는 주어진 문자열을 UTF-8 등의 포맷으로 인코딩하는 메서드이다.
    rawdata = logic.update(data.encode())
    # hexdigest()는 위에서 update()로 해싱된 바이트 문자열을 16진수로 변환한 결과를 반환한다.
    rawkey = rawdata.hexdigest()
    # 16진수 문자열을 10진수로 변환해 반환한다.
    return int(rawkey, 16)

# 위 make_key로 생성된 key를 통해 address를 생성한다.
def make_address(key):
    return key % 8

# chaining 기법에서의 저장 함수
def store_data(data, value):
    key = make_key(data)
    hash_address = make_address(key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][0] == key:
                hash_table[hash_address][1] = value
            else:
                hash_table[hash_address].append([key, value])
    else:
        hash_table[hash_address] = [[key, value]]

# chaining 기법에서의 열람 함수
def read_data(data, value):
    key = make_key(data)
    hash_address = make_address(key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][0] == key:
                return hash_table[hash_address][1]
            else:
                return None
    else:
        return None
'''