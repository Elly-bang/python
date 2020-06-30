'''
제어문: 조건문(if),반복문(while,for)
Python 블럭: 콜론과 들여쓰기

형식1)
if 조건식 :
   실행문
   실행문
'''

var=10
if var >= 10 :
    print('var=',var)
    print('var는 10보다 크거나 같다')

print('항상 실행 되는 영역')

#var= 10
#var는 10보다 크거나 같다
#항상 실행 되는 영역

var=10
if var >= 15 :
    print('var=',var)
    print('var는 10보다 크거나 같다')

print('항상 실행 되는 영역') #항상 실행 되는 영역만 나오는것은 거짓


'''
형식2)
if 조건식:
    실행문1
else :
    실행문2
'''
var=2
if var >=5 :
    print("var는 5보다 크거나 같다.")
else :
    print("var는 5보다 작다.")

    #var는 5보다 작다.

#키보드 점수 입력-> 60점 이상 : 합격, 미만 : 불합격

score=int(input("점수입력 :"))
if score >= 60 :
    print("합격")
else :
    print("불합격")

# 기존 라이브러리 사용  import
import datetime #mopdule import
today=datetime.datetime.now() #module.class.method()
print(today) #2020-04-07 11:09:59.480495

#요일 반환
week=today.weekday()
print(week) #0~4:평일, 5~6:휴일  #1

if week >=5 :
    print("오늘은 휴일")
else :
    print("오늘은 평일")

'''
형식3)
if 조건식1 :
   실행문1
elif 조건식2 :
   실행문2
else :
   실행문3
'''

#문2)키보드 score입력 :A(100~90),B(80),C(70),D(60),F(59미만)

score=int(input("점수 입력: "))
if score >=90 :
    print("A")
elif score <90 and >=80 :
    print("B")
elif score < 80 and >= 70 :
    print("C")
elif score < 70 and >= 60 :
    print("D")
else score <=59 :
    print("F")

score=int(input("점수 입력(0~100): "))
#전역 변수 :score grade
grade =''
if score >=90 :
    grade="A학점"
elif score >=80 :
    grade = "B학점"
elif score >= 70 :
    grade = "C학점"

elif score >= 60 :
    grade = "D학점"
else :
    grade = "F학점"

 print("당신의 점수는 %d이고, 등급은 %s이다"%(score,grade))

#블럭 if vs 라인 if

num =9
if num >=5 :
    result=num*2
else:
    result=num+2

print(result) #18

# 라인 if
# 형식) 변수 = 참 if 조건문  else 거짓
result = num * 2 if num >= 5 else num + 2
print(result) # 18