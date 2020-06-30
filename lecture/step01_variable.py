'''
변수(Variable)
-형식)변수명=값 or 수식 or 변수명
-자료를 저장하는 메모리 이름
-type 선언 없음(R과 동일)
'''

#1.변수와 자료
var1="Hello python"
var2='Hello python'

print(var1) #line skip
print(var2)
print(type(var1)) #<class 'str'>
print(type(var1),type(var2)) #<class 'str'> <class 'str'>

var1=100
print(var1,type(var1)) #100 <class 'int'>
var3=150.25
print(var3,type(var3)) #150.25 <class 'float'>

var4=True
print(var4,type(var4)) #True <class 'bool'>

var4=False
print(var4,type(var4)) #False <class 'bool'>

#2. 변수명 작성규칙(P.11) .은 변수명 사용 안됨

_num10=10
_NUM10=20
print(_num10,_NUM10) #10 20
print(id(_num10),id(_NUM10)) #140704861748576 140704861748896


#키워드 확인 (변수명 사용 안됨)
import keyword #모듈 임포트 #C:\Python37\Lib 위치  keyword
py_keyword=keyword.kwlist #키워드 반환
print("파이선 키워드:",py_keyword) #파이선 키워드: ['False', 'None', 'True', 'and' 등등은 변수명으로 사용하면 안됩니다.!!
print("len=",len(py_keyword)) #len= 35

#낙타체
korScore =90 #변수=상수
matScore=85
engScore=75
tot=korScore+matScore+engScore #변수 = 수식
print("tot=",tot) #tot= 250

#3. 참조변수: 메모리 객체(value)를 참조하는 주소 저장 변수
x=150 #150객체의 주소
y=45.23
y2=y #변수 복제(주소 복제)
x2=150 #기존 객체 있으면, 주소 반환
#변수 내용 출력
print(x,y,y2,x2) #150 45.23 45.23 150
#변수 주소 출력
print(id(x),id(y),id(y2),id(x2)) #140704861753056 1981540447984 1981540447984 140704861753056

