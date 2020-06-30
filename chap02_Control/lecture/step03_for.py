'''
반복문(for)

형식)
for 변수 in 열거형객체 :
    실행문
    실행문

열거형객체(iterable) : string, list, tuple, set/dict
제너레이터 식 : 변수 in 열거형객체(원소 순회 -> 변수 넘김)
'''

# 1. string 열거형 객체 이용
string = "나는 홍길동 입니다."
print(len(string)) # 11

for s in string : # 11회
    print(s, end= ' ') # 나 는   홍 길 동   입 니 다 .

for s in string.split() : # split(sep=' ') : 3회
    print(s)
'''
나는
홍길동
입니다.
'''

# 2. list 열거형 객체 이용
help(list) # class
lst = [1, 2, 3, 4, 5] # list object
print(lst) # object 내용 : [1, 2, 3, 4, 5] - vector
print(type(lst)) # object type : <class 'list'>
print(len(lst)) # 5

#print(lst**2) # TypeError

lst2 = [] # 빈 list object
for i in lst :
    print(i, end = ' ') # 1 2 3 4 5
    lst2.append(i**2) # 원소 추가(순서 보장)

print("\nlst2 : ", lst2)

# 1~100 원소를 갖는 list 객체 생성
lst3 = list(range(1, 101)) # range(start, stop-1)
print(lst3)

# 3. range 열거형 객체 이용
'''
range(n) : 0 ~ n-1 정수 
range(start, stop) : start ~ stop-1 정수 
range(start, stop, step) : start ~ stop-1 , step 정수 
'''
num1 = range(10) # 0 ~ 9
num2 = range(1, 10) # 1 ~ 9
num3 = range(1, 10, 2) # 1 3 5 7 9
print(num1) # range(0, 10)
print(num2) # range(1, 10)
print(num3) # range(1, 10, 2)

for i in num1 :
    print(i, end= ' ') # 0 1 2 3 4 5 6 7 8 9
print()
for i in num2 :
    print(i, end= ' ') # 1 2 3 4 5 6 7 8 9
print()
for i in num3 :
    print(i, end= ' ') # 1 3 5 7 9

# 4. list + range 열거형 객체 이용
idx = list(range(5)) # range object -> list object
print(idx) # range(0, 5) -> [0, 1, 2, 3, 4]

for i in idx :
    print(i, end = ' ')
    print(i**2)

'''    
 문) lst1에 1~100까지 100개의 원소를 갖는 vector를 생성하고,
     lst2에 3의 배수만 저장하기 
'''
lst1 = list(range(1, 101)) # 1~100
print(len(lst1)) # 100

lst2 = [] # 빈 list(3의 배수만 저장)
for data in lst1 :
    if data % 3 == 0 :
        lst2.append(data)

print(lst2)
print(len(lst2)) # 33

# index 이용 : 분류정확도
y = [1, 0, 2, 1, 0] # 관측치 : 범주형(0, 1, 2)
y_pred = [1, 0, 2, 0, 0] #  예측치

size = len(y) # 5
acc = 0 # 분류정확도
for i in range(size) : # range(5) : 0 ~ 4
    fit = int(y[i] == y_pred[i]) # int(True/False) -> 1/0
    acc += fit * 20 # 누적변수

print("분류정확도 = ", acc) # 분류정확도 =  80

# 5. 이중 for 문

# 1) 구구단 예
for i in range(2, 10) : # i = 단수
    print("*** {}단 ***".format(i))

    for j in range(1, 10) : # j = 곱수
        print("%d * %d = %d"%(i, j, i*j))

    print() # line skip

para = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

# 2) 문자열 처리
sents = [] # 문장
words = [] # 단어
for sent in para.split('\n') : #  문단 -> 문장
    sents.append(sent) # 문장 저장
    for word in sent.split() : # 문장 -> 단어
        words.append(word) # 단어 저장

print(sents)
print('문장 길이 : ', len(sents))
print(words)
print('단어 길이 : ', len(words))

# 제너레이터 식 : 변수 in 열거형객체
'''
for 변수 in 열거형객체 : 
  -> 객체의 원소 수 만큼 반복 
if 값 in 열거형객체 :
  -> 객체의 원소 중에서 값이 있으면 True, 아니면 False
'''
search = input("검색 단어 입력 : ")

if search in words :
    print("해당 단어 있음") # 해당 단어 있음
else :
    print("해당 단어 없음")






