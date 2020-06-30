'''
리스트 내포
-list에서 for문 사용
형식1) 변수=[실행문 for 변수 in 열거행 객체 ]
실행순서 : 1. for > 2. 실행문 > 3. 변수 저장
형식2) 변수=[실행문 for 변수 in 열거행 객체 if 조건식 ]
실행순서 : 1. for > 2. if문 > [3.실행문 > 4.변수 저장 (생략 가능)] ===>??????순서
'''

#형식1) 변수 = [실행문 for 변수 in 열거행 객체 ]

#x 각 변량에 제곱
x=[2,4,1,3,7]
#x**2
data=[]
for i in x:
    print(i**2)
    data.append(i**2)
print(data) #[4, 16, 1, 9, 49]

data2=[실행문 for i in x]
print(data2) #[4, 16, 1, 9, 49]

#형식2)변수=[실행문 for 변수 in 열거행 객체 if 조건식 ]
#1~100 3의 배수

num=list(range(1,101))
print(num) #[1, 2, 3, 4

data3=[ i for i in num if i % 3 == 0 ]
print(data3) #[3, 6, 9, 12

#내장 함수 리스트 내포
print('sum=', sum(x))

data4=[[1,3,5],[4,5],[7,8,9]] #중첩 list

for d in data4:
result = [sum(d) for d in data4]
print(result)

