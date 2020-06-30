'''
dict특징
-set 구조와 유사함 (순서 없음, index사용 불가)
- R의 list 와 유사함
  key : value 한쌍으로 구성
  key -> value 참조
  key 중복 불가 , value 중복 가능
형식) 변수 = {key : value, key: vlaue}

'''

#1. dict생성

#방법1)
dic= dict(key1 =100, keky2 = 200, key3=300)
print(dic, len(dic), type(dic))
#{'key1': 100, 'keky2': 200, 'key3': 300} 3 <class 'dict'>

#방법2)
dic2={'name':'홍길동','age':35, 'addr':'서울시' }
print(dic2) #{'name': '홍길동', 'age': 35, 'addr': '서울시'}

#2. 수정, 추가, 삭제, 검색 : key 이용
dic2['age'] = 45 #수정
dic2['pay'] = 350 #추가
print(dic2) #{'name': '홍길동', 'age': 45, 'addr': '서울시', 'pay': 350}
del dic2['addr']
print(dic2) #{'name': '홍길동', 'age': 45, 'pay': 350}

#key검색 #in 으로 확인
print('age' in dic2) #TRue

# 3. for 이용
for k in dic2.keys() : #.keys()생략 가능 #키넘김
    print(k, end='->') #key
    print(dic2[k]) #value

for v in dic2.values() : #값 넘김
    print(v)

for k, v in dic2.items(): #key 값 넘김
    print(k,end='->')
    print(v)

for d in dic2.items(): #key 값 넘김
    print(d) #(키, 값)->tuple

# 4. key -> value
print(dic2['name']) #index : 홍길동
print(dic2.get('name')) #get() : 홍길동

# 5. {'key' : [value1, value2]} - {'이름' : [급여, 수당]}

emp= {'hong': [250, 50], 'lee':[350, 80], 'yoo':[200,40]}
print(emp)

#급여가 250이상인 경우 사원명, 수당 합계

for k, v in emp.items() :
  if v[0] >= 250 :
     print(k, end='->')
     print(v)


su = 0
for k, v in emp.items() :
  if v[0] >= 250 :
     print(k)
     su += v[1]
print("수당 합계=",su)

#6.문자 빈도수 구하기
charset = ['love','test','love','hello','test','love']
print(len(charset))
wc={} #'love' : 1

# 방법1)
for word in charset:
    if word in wc:
        wc[word] += 1 # 2 회 이상 발견 : 1씩 증가
    else:
        wc[word] = 1 #최초 발견 : 1를 초기화
print('워드 카운트 :', wc) #워드 카운트 : {'love': 3, 'test': 2, 'hello': 1}

print(max(wc,key=wc.get)) #love

# 방법2)
wc2={} #'love' : 1
for word in charset:
    #key=value
    wc2[word]=wc2.get(word,0) + 1

print(wc2)