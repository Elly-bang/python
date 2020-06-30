'''
반복문(while)

while 조건식 :
    실행문
    실행문
'''

# 카운터, 누적 변수
cnt = tot = 0 # 변수 초기화

while cnt < 5 : # True -> loop(명령문 집합) 실행
    cnt += 1 # 카운터 변수
    tot += cnt # 누적변수
    print(cnt, tot)

# 문1) 1~100까지 합 출력하기
cnt = tot = 0
data = [] # 빈 list(짝수 저장)

while cnt < 100 :
    cnt += 1
    tot += cnt
    if cnt % 2 == 0: # 2의 배수(짝수)
        data.append(cnt) # 짝수 값 추가

print("1~100까지 합 : %d"%(tot))
print("짝수 값 : ", data)

# 문2) 1~100 사이에서 5의배수이면서 3의 배수가 아닌 값만 append 하기
cnt = 0
data = [] # 5의 배수이면서(and) 3의 배수가 아닌 값 저장

while cnt < 100 :
    cnt += 1
    if cnt % 5 == 0 and cnt % 3 != 0 : # not(cnt % 3 == 0)
        data.append(cnt)

print("5의 배수이면서(and) 3의 배수가 아닌 값")
print(data)

# 무한 loop -> 종료 조건(0)
while True :
    num = int(input("숫자 입력 : "))
    if num == 0 :
        print("프로그램 종료")
        break # 탈출(exit) : 종료 조건
    print("num =", num)

# random : 난수 생성
import random # 난수 생성 모듈
help(random.random) # 0~1 난수 실수
help(random.choice)
help(random.randint) # 난수 정수

r = random.random() # 모듈.함수(0~1 난수)
print('r=', r) # r= 0.39981229676019947

# 문3) 난수 0.01 미만이면 종료, 아니면 난수 개수 출력
# 종료 조건 : 0.01 미만

cnt = 0
while True :
    r = random.random()
    if r < 0.01 :
        break # exit
    else :
        cnt += 1

print('난수 개수 =', cnt)

r = random.randint(1,5) # 1 ~ 5 난수 정수
print(r)

print(">>> 숫자 맞추기 게임 <<<")
'''
숫자 범위 : 1 ~ 10
myInput == computer : 성공(exit) -> 종료 조건 
myInput > computer : '더 작은 수 입력'
myInput < computer : '더 큰 수 입력'
'''
computer = random.randint(1, 10)
while True :
    myInput = int(input("예상 숫자 입력 : ")) # 사용자 입력
    if myInput == computer :
        print('~~성공~~')
        break # exit
    elif myInput > computer :
        print('~~ 더 작은 수 입력 ~~')
    elif myInput < computer:
        print('~~ 더 큰 수 입력 ~~')

'''
continue vs break
 - 반복문에서 사용되는 명령어 
 - continue : 반복을 지속, 다음 문장 skip 
 - break : 반복 멈춤 
'''

i = 0
while i < 10 :
    i += 1

    if i == 3 :
        continue # 다음 문장 skip
    if i == 6 :
        break
    print(i, end='  ') # 1  2  4  5














