'''
함수의 가변인수
-한 개의 가인수로 여러개의 실인수를 받는 인수
형식)def 함수명(*인수)
'''

#1. tuple형으로 받는 가변인수
def Func1(name,*names):
    print(name)
    print(names)

Func1('홍길동','이순신','유관순')

#import 패키지. 모듈
import scatter.scatter_module #방법1) import 패키지.모듈
#from 패키지. 모듈 import 함수1, 함수 2, 클라스 1
from scatter.scatter_module import Avg, var_std #방법2)

datas=[2,3,5,6,7,8.5]
avg1= scatter.scatter_module.Avg(datas)
avg2= Avg(datas)
print(avg1) #5.25
print(avg2) #5.25

var, std = var_std(datas)
print('var=',var) # var= 5.975
print('std=',std) # std= 2.444381312316063

def statis(func,*data):
    if func == 'sum':
        return sum(data) #함수 실행 종료(exit)
    elif func == 'avg':
        return Avg(data)
    elif func == 'var':
        return var(data)
    elif func == 'std':
        return var_std(data)

    else :
        return '해당함수 없음'

print(statis('sum',1,2,3,4,5)) #15
print(statis('avg',1,2,3,4,5))
var, _= statis('var',1,2,3,4,5)
print('var=',var)
_, std = statis('var',1,2,3,4,5)
print('std=',std )

#2. dict형 가변인수
def person(w,h,**other):
    print('w=',w)
    print('h=',h)
    print(other)

person(65,175,name='홍길동',age=35)

#3.함수를 인수로 바딕
def square(x):
    return x**2

def my_func(func,datas):

    result=[ func(d) for d in datas]
    return result

datas=[1,2,3,4,5]
print(my_func(square,datas)) #(함수, 데이터셋)
#[1, 4, 9, 16, 25]

