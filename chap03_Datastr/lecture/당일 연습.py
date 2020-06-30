#dict

#방법1)
dic=dict(key1=100, key2=200, key3=300)
print(dic, len(dic),type(dic))
#방법2)
dic2={'name':'홍길동','age':'35','addr':'서울시'}
print(dic2, len(dic2), type(dic2))

#key이용한 조작 방법 -수정, 추가, 삭제, 검색
dic2['age'] =45
dic2['name'] = '방'
del dic2['age']
print(dic2)

#key검색 #in으로 확인
print('age'in dic2)
print('name'in dic2)

#3. for 이용
for k in dic2.keys() : #.keys()생략 가능 #키넘김
    print(k, end='->') #key
    print(dic2[k]) #value

'''
또 한 가지 주의해야 할 사항은 Key에 리스트는 쓸 수 없다는 것이다. 
하지만 튜플은 Key로 쓸 수 있다. 
딕셔너리의 Key로 쓸 수 있느냐 없느냐는 Key가 변하는 값인지 변하지 않는 값인지에 달려 있다. 
리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다. 
다음 예처럼 리스트를 Key로 설정하면 리스트를 키 값으로 사용할 수 없다는 오류가 발생한다.
'''

for v in dic2.values():
    print(v)

for k,v in dic2.items() :
    print(k,end='->')
    print(v)

for d in dic2.items() :
 print(d)

 #key-> value
 print(dic2['name'])
 print(dic2.get('name'))

#5. {'key':[value2,value2]} key: 이름, value:급여, 수당
emp={'hong':[250,50], 'lee':[350,80], 'yoo':[200:40]}
print(emp)

#급여가 250이상인 경우 사원명, 수당 합계

#k:이름, v:급여, 수당
for k,v in emp.items():
    print(k, end=' ')
    print(v)

su=0
for k,v in emp.items():
    if v>=250:
        print(k)
        su += v[1]
print("수당합계=",su)


6. 문자 빈도수 구하기
charset=['love','test','love','hello','test','love']
print(len(charset))
wc={}

#방법1)
for word in charset:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1
print('워드 카운트:', wc)
print(max(wc, key=wc.get))

#방법2)
wc2={}
for word in charset:
    wc2[word]=wc2.get(word,0)+1
print(wc2)






