'''
set 특징
-순서 없음(index사용 불가 )
-중복 허용 불가
형식) 변수 = {값1, 값2, ...}
-집합 개념
'''

s= {1, 3, 5, 1, 5} #나열 순서 의미 없음
print(len(s)) #중복 데이터 허용 불가

for d in s:
    print(d, end=' ') #1 3 5

#집합 관련 함수
s2= {3, 6}
print(s.union(s2)) #합집합 : {1, 3, 5, 6}
print(s.difference(s2)) #차집합 : {1, 5}
print(s.intersection(s2)) #교집합 : {3}

#list : gender
gender = ['남자', '여자', '남자', '여자'] #중복 허용
sgender= set(gender) #중복 불가
print(sgender) #{'여자', '남자'}
#print(sgender[0]) #TypeError

#set- > list
lgender = list(sgender)
print(lgender[0]) #여자

#원소 추가/삭제
s3 = {1, 3, 5 ,7}
print(s3, type(s3))

s3.add(9)
print(s3)
#{1, 3, 5, 7, 9}

s3.discard(3)
print(s3)
#{1, 5, 7, 9}