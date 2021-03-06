'''
클래스(class)
-함수의 모임
-역할: 다수의 함수와 공유 자료를 묶어서 객체(object) 생성
-유형 : 사용자 정의 클래스, 라이브러리 클래스 (python)
-구성 요소: 멤버(member)+생성자
-멤버(member): 변수(자료 저장) + 메서드(자료 처리)
-생성자 : 객체 생성
#####################
형식)
class 클래스명 :
     멤버변수 = 자료
     def 멤버메서드() :
        자료 처리
     생성자 : 객체 생성
#####################
'''

#1.중첩함수
def calc_func(a,b): #outer : 자료 저장
    #자료 저장
    x = a
    y = b

    #inner :자료 처리(조작)
    def plus():
        return x+y
    def minus():
        return x-y

    return plus, minus
p, m = calc_func(10, 20) #일급함수 : +는 p로, -는 m으로 저장
print('plus=',p()) #plus= 30
print('minus=',m()) #minus= -10

#2. 클래스 정의
class calc_class:
    #member변수(전역 변수): 자료 저장
    x = y = 0

    #생성자 : 객체 생성 + 멤버 변수 값 초기화
    def __init__(self, a, b):
        #멤버 변수 초기화
        #self.멤버변수=지역변수
        self.x = a
        self.y = b #비활성화 y회색은 지역변수 뜻함/ self 사용해야 전역 변수

    #멤버 메서드 : 클래스에서 정의한 함수 x = y = 0에서 +,-메서드 2가지 만듦(self이용)
    def plus(self): #바깥 함수로 접근시 self가 작용
       return self.x + self.y

    def minus(self):
        return self.x - self.y

#클래스(1) vs 객체(n)
    #생성자 -> 객체 (object)
    obj1 = calc_class(10, 20) #클래스명(): 생성자 -> 객체 생성
    #object.member() :멤버 메서드 호출

    #obj1.plus()
    #obj1.minus()

    print('plus=', obj1.plus()) #plus=30
    print('minus=', obj1.minus()) #minus=-10
    # object.member() :멤버 변수 호출
    print('x=', obj1.x) #x=10
    print('y=', obj1.y) #y=20

    #생성자-> 객체2
    obj2= calc_class(100, 200)
    print('plus=', obj2.plus())  #  plus = 300
    print('minus=', obj2.minus()) #  minus = -100
    print('x=', obj2.x)  # x= 100
    print('y=', obj2.y)  # y= 200
    #객체 주소 확인 => class는 하나이며, n개의 객체를 만들기 위한 지도 역할 . 각각 저장됨을 확인.
    print(id(obj1),id(obj2)) # 2393244617544 2393244621960

#3. 라이브러리 클래스
from datetime import date #from 모듈 import 클래스
today = date(2020, 4, 13) #생성자 -> 객체

#object.member
print('year :',today.year)
print('month :',today.month)
print('day :',today.day)

#object.member():method
week = today.weekday()
print('week :', week) #week : 0 -> 월요일 : 0~6까지
