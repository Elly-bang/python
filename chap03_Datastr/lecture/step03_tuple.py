'''tuple
-순서가 존재한다.
-index사용 순서 존재
-수정 불가,처리 속도 빠름
-1차원 배열 구조
-제공 함수 x
-형식) 변수 =(원 1, 원2 ....)
'''

tp=10 #scala
tp1= (10)  #scala
print(tp1, tp)

tp2=(10, )
print(tp2,type(tp2))

tp3 = (10, 58, 4, 96, 55, 2)
print(tp3[:4])
print(tp3[-3:])
##수정 불가
#tp3[0] =100 #TypeError:

#max/min

vmax=vmin =tp3[0] #첫번재 원소 ->초기화
for t in tp3 :
    if vmax < t :
        vmax = t
    if vmin > t :
        vmin = t

print('최댓값=',vmax)
print('최솟값=',vmin)

#list -> tuple

lst=list(range(10000))
print(len(lst))

tlst=tuple(lst)
print(type(tlst))