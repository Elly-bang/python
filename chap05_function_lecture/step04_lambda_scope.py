'''
1.축약함수(lambda)
-한 줄 함수
형식) 변수 = lambda 인수 : 리턴값
ex) lambda x,y : x+y

2. scope
-전역변수, 지역변수 (함수)

'''

#1. lambda
def adder(x,y):
    add = x + y
    return add

add=lambda x, y :x + y
#[lambda x,y : x+y for 변수 in 열거형 객체]

re=add(10, 20)
print(re) #30

#2. scope
'''
전역 변수 : 전지역에서 사용되는 변수 
지역 변수 : 특정지역(함수)에서만 사용되는 변수 
'''
x = 50 #전역변수

def local_func(x):
    x+= 50  #x=100 지역변수 (전역 변수 출력시 출력되지 않음)
    #해당 함수가 종료되면 자동으로 소멸
local_func(x)
print('x=',x) #x= 50  100이 아닌 50이 출력되는 이유는 전역 변수이기 때문

########################################################################
def global_func():
    global  x #global 키워드 : 전역변수로 해석해라
    x += 50 #x=100

global_func()
print('x=',x) #x= 100

print('x',)

