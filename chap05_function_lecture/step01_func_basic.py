'''
함수 (function)
-중복 코드 제거
-재사용 가능
-특정 기능 1개 포함
-유형)사용자 정의 함수, 라이브러리 함수
'''

# 1. 사용자 정의 함수
'''
형식)
def 함수명([매개 변수]):
    실행문
    실행문
    [return 값1, 값2,....]
'''
#1)인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1() #함수 호출

#2)인수가 있는 함수
def userFunc2(x,y):
    adder=x+y
    print('adder=', adder) #adder= 30

userFunc2(10,20) #adder= 30

#3)리턴 함수
def userFunc3(x,y):
    add=x+y
    sub=x+y
    mul=x*y
    div=x/y
    return  add, sub, mul, div

a,s,m,d = userFunc3(100,20)
print('add=',a)
print('sub=',s)
print('mul=',m)
print('div=',d)

#2. 라이브러리 함수
'''
#1) bulit-in :기본 함수
dataset = lsit(range(1,6))
print(dataset)

print('sum=',sum(dataset)]
print('max=',max(dataset)]
print('sum=',min(dataset)]
print('sum=',sum(dataset)]

#2)import :모듈.함수()
'''
import statistics #통제 관련 함수 제공
'''
ctrl +클릭 :module of function source 보기 
'''
from statistics import mean #방법2)주로 사용

print(dir(statistics))# 해당 모듈의 정보

avg1=statistics.mean(dataset)
avg2=mean(dataset)
print('평균=',avg1)
print('평균=',avg2)






