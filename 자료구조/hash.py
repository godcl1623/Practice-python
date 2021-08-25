hash_table = list([0 for i in range(8)])

def make_key(data):
    return hash(data)

def make_address(key):
    return key % 8

'''
case #1 chaining 기법의 경우

def store_data(data, value):
    key = make_key(data)
    hash_address = make_address(key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([key, value])
    else:
        hash_table[hash_address] = [[key, value]]

def read_data(data):
    key = make_key(data)
    hash_address = make_address(key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == key:
                return hash_table[hash_address][index][1]
        print('검색 결과가 존재하지 않습니다')
        return None
    else:
        print('저장된 데이터가 없습니다')
        return None
'''

'''
case #2 linear probing 기법

def store_data(data, value):
    key = make_key(data)
    hash_address = make_address(key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
    else:
        hash_table[hash_address] = [key, value]

def read_data(data):
    key = make_key(data)
    hash_address = make_address(key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index][0] == key:
                return hash_table[index][1]
            else:
                print('검색 결과가 존재하지 않습니다')
                return None
    else:
        print('저장된 데이터가 없습니다')
        return None;
'''

'''
case #3 해쉬 함수 재정의, 해쉬 테이블 확대
hash_table = list([0 for i in range(16)])

def make_address(key):
    return key % 16
'''

'''
case #4 sha256 사용

import hashlib

hash_table = list([0 for i in range(8)])

def make_key(data):
    logic = hashlib.sha256()
    rawdata = logic.update(data.encode())
    rawkey = rawdata.hexdigest()
    return int(rawkey, 16)

def make_address(key):
    return key % 8

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