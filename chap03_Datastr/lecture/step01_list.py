'''
List특징
-1차원 배열구조
 형식)변수 =[값1, 값2,...]
-다양한 자료형 저장 가능
-index 사용, 순서 존재
 형식)변수[index],index=0
-값 수정 (추가 , 삽입, 수정, 삭제)
'''

#1. 단일 list
lst = [1, 2, 3, 4, 5]
print(lst, type(lst),len(lst))

for i in lst:
  #  print(i,end=' ') 1 2 3 4 5
     print(lst[i-1: ]) #변수 [start: stop]
'''
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]
'''

for i in lst:
    #  print(i,end=' ') 1 2 3 4 5
    print(lst[ : i])  # 변수 [stop-1]
'''
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
'''

'''
처음/마지막 데이터 추출
'''

x=list(range(1,101)) #1~100
print(x)
print(x[:5]) #앞부분 5개 원소 : [1, 2, 3, 4, 5]
print(x[-5:]) #마지막 5개 원소 :[96, 97, 98, 99, 100]

'''
indx형식 
변수[start:stop-1:step]
'''

print(x[:]) #전체 데이터 호출
print(x[::2]) #[::step=2]:홀수형태
print(x[1::2]) #[start::step2]:짝수형태

# 2. 중첩list : [[],[]] ->1차원
a= ['a','b','c']
b= a #서로 다른 타입 저장 가능
b= [10,20,5,'a',True,"hong"]
b= [10,20,5,['a','b','c'],True,"hong"]
print(b[3]) #a
print(b[3][2]) #c
print(b[3][1:]) #['b', 'c']

print(type(a),type(b)) #<class 'list'> <class 'list'>
print(id(a),id(b)) #1409324068680 1409324062856

#3. 값 수정(추가, 삽입, 수정, 삭제)
num =['one','two','three','four']
print(len(num)) #['one', 'two', 'three', 'four']
num.append('five') #원소 추가
print(num) #['one', 'two', 'three', 'four', 'five']
num.remove('five')
print(num) #['one', 'two', 'three', 'four']
num.insert(0,'zero')
print(num) #['zero', 'one', 'two', 'three', 'four']
num[0] =0
print(num) #[0, 'one', 'two', 'three', 'four']

#4.list 연산 (+,*)

#1)list결합
x = [1,2,3,4]
y = [1.2,2.5]
z = x + y #new object
print(z,type(z)) #[1, 2, 3, 4, 1.2, 2.5] <class 'list'>

#2)list확장
x.extend(y) #기존 object
print(x) #[1, 2, 3, 4, 1.2, 2.5] 단일list

#3) list 추가
x.append(y) #[1, 1.2, 2, 2.5, 3, 4, [1.2, 2.5]] 중첩 list
print(x)

#extend/append 기존 객체 사용하면서 모양이 다르다.

#4)list곱셉

lst=[1, 2, 3, 4]
result=lst*2 #2번 반복
print(result) #[1, 2, 3, 4, 1, 2, 3, 4]

#5.list정렬
result.sort() #오름차순
print(result.sort())
print(result) #[1, 1, 2, 2, 3, 3, 4, 4]

result.sort(reverse=True) #내림차순
print(result) #[4, 4, 3, 3, 2, 2, 1, 1]

# 6. scala vector 변수
'''
scala 변수 : 한 개의 상수(값)를 갖는 변수 (크기)
vector 변수: 다수의 값을 갖는 변수(크기, 방향)
'''

dataset=[] #빈list vector 변수
size=int(input("vector size:")) #scala 변수

for i in range(size): #range(5) :0~4
    dataset.append(i+1) #vector변수

print(dataset) #[1, 2, 3, 4, 5]

ataset=[] #빈list vector 변수
size=int(input("vector size:")) #scala 변수

for i in range(size): #range(10) :0~9
    dataset.append(i+1) #vector변수

print(dataset) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#7. list에서 원소 찾기

'''
if 값 in list:
    참 실행문 
else :
     거짓 실행문

'''

if 5 in dataset:
    print("5가 있음")
else:
    print("5가 없음")