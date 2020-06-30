'''
재귀호출(recursive call)
 - 함수 내에서 자신의 함수를 반복적으로 호출하는 기법
 - 반복적으로 변수의 값을 조정해서 연산 수행
 ex) 1~n (1+2+3+4..n)
 - 반드시 종료조건 필요
'''

# 1. 카운터 : 1~n
def Counter(n) :
    if n == 0 : # 종료조건
        #print('프로그램 종료')
        return 0 # 함수 종료
    else :
        Counter(n-1) # 1. 재귀호출
        '''
        1. stack : [5(first), 4(5-1), 3(4-1), 2(3-1), 1(2-1)] 0[1-1]
        2. stack 역순으로 출력 
        '''
        print(n, end=' ') # 2. 카원트 : 1 2 3 4 5

print(Counter(0)) # 0
Counter(5)

print()

# 2. 누적(1 + 2 + 3 .. +n)
def Adder(n) :
    if n == 1 : #종료 조건
        return 1 # 종료
    else :
        result = n + Adder(n-1) # 1.재귀호출 -> 2. 누적
        '''
        stack : 후입선출(LIFO)
        1. stack [5(first), 4(5-1), 3(4-1), 2(3-1)] 1(2-1)
        2. stack 역순으로 누적 :1+[2+3+4+5] = 15
        '''
        print(result, end=' ') # 3 6 10 15
        return result

print(Adder(1)) # 1
print(Adder(5)) # 15