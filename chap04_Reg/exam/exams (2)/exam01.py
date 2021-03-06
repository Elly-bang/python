'''
문1) 다음 emp '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

#for문 이용한 경우
names=[]
for e in emp:
    re=findall('[가-힣]{3},',e)
    names.append(re[0])
print('names=',names)




#list+for이용 :변수=[실행문 for 변수 in 열거형객체]
names=[findall('[가-힣]{3}',e)[0] for e in emp]
print('names=', names)
