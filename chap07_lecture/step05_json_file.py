'''
JSON 파일
 - 네트워크에서 표준으로 사용되는 파일 형식
 - 파일 형식 : {key:value, key:value}, {key:value, key:value}
 - 활용 예 : 서로 다른 플랫폼(java, python)에서 파일 공유

 - json 모듈
  1. encoding : file save : python object(list, dict) -> json file
  2. decoding : file read : json file -> python object
'''

import json

# 1. encoding : object -> 문자열
'''
python object -> json 문자열 -> file save
형식) json.dumps(object)
'''
user = {'id' : 1234, 'name':'홍길동'} # dict
print(type(user)) # <class 'dict'>

json_str = json.dumps(user, ensure_ascii=False) # unicode -> ascii 인코딩 안함
print(json_str) #{"id": 1234, "name": "홍길동"}
print(type(json_str)) # <class 'str'>

# 2. decoding : 문자열 -> object
'''
json 문자열 -> python object
형식) json.loads(json 문자열)
'''
py_obj = json.loads(json_str)
print(py_obj) # {'id': 1234, 'name': '홍길동'}
print(type(py_obj)) # <class 'dict'>

# 3. json file read/write

# 1) json file read : decoding
import os
print(os.getcwd())
file = open("../data/usagov_bitly.txt", mode='r', encoding='utf-8')
data = file.readlines() # 전체 내용 -> 줄단위 읽기(list)
file.close()
print(data)

# decoding : json 문자열 -> python object
rows = [ json.loads(row) for  row in data] # row = {'key':value, ....}
print(len(rows)) # 3560

for row in rows[:10] :
    print(row) # {'a': 'Mozilla/5.0 (Windows NT 6.1; WOW64)
    print(type(row)) # <class 'dict'> -> python object

# json object -> DataFrame
import pandas as pd
rows_df = pd.DataFrame(rows) # 행렬 자료구조
print(rows_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3560 entries, 0 to 3559
Data columns (total 18 columns):
'''
print(rows_df.head())
print(rows_df.tail())

# 2) json file write : json encoding
file = open("../data/json_text.txt", mode='w', encoding='utf-8')
print(type(rows)) # python object : <class 'list'>

for row in rows[:100] : # row = {key:value, ....} : dict
    json_str = json.dumps(row) # dict -> json 문자열
    file.write(json_str) # file save
    file.write('\n') # 줄바굼

print('file 저장 완료 ~~~')

# 3) json file read : json decoding
file = open("../data/json_text.txt", mode='r', encoding='utf-8')
data = file.readlines()
print(len(data))

# json decoding
rows = [json.loads(row) for row in data] # json 문자열 -> python object

rows_df = pd.DataFrame(rows)
print(rows_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 18 columns):
'''