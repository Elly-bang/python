'''
1. json 파일 2가지 형식

1. 중괄호 : {key:value, ...}, {key:value, ...}
   -> json.loads(row)
2. 대괄호 : [{key:value, ...}, {key:value, ...}]
  -> json.load(row)
'''

import json
import pandas as pd

# 1번 형식 : 중괄호 : {key:value, ...}

# 2번 형식 : 대괄호 : [{key:value, ...}, ..]
file = open("../data/labels.json", mode='r', encoding='utf-8')
#print(file.read()) # [{row}, {row}, ...]

rows = json.load(file) # json 문자열 -> python object
print(len(rows)) # 30
print(rows)
print('type =', type(rows)) # type = <class 'list'>

for row in rows[:5] : # [{row}, {row}]
    print(row)
    print(type(row))

file.close()

# list -> DataFrame
rows_df = pd.DataFrame(rows)
print(rows_df.info())
'''
RangeIndex: 30 entries, 0 to 29
Data columns (total 5 columns):
'''
print(rows_df.head())

# 2. pickle
'''
python object(list, dict) -> file(binary) -> python object(list, dict)
'''
import pickle
'''
save : pickle.dump(data, file)
load : pickle.load(file)
'''

# 1) pickle save
'''
file = open("../data/rows_data.pickle", mode='wb') # write binary
pickle.dump(rows, file) # list -> binary
print('pickle file saved')
'''

# file reload

# 2) pickle load
file = open("../data/rows_data.pickle", mode='rb')
rows_data = pickle.load(file)
print(rows_data)
print(type(rows_data))








