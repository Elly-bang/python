'''
정규 표현식

[주요 메타문자]
. : 임의의 한 문자
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc)
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
'''

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
#st2 = 'test1abcABC 123mbc 45test'
#st3 = 'test^홍길동 abc 대한*민국 123$tbc'

#import re #정규 표현식 모듈
from re import findall, match, sub #방법2) from module import function  #from 에서 findall, match, sub를 사용

# re.findall() #방법 1
# findall() #방법 2 주로 이용

# 형식 ) findall(pattern='메타문자 패턴',string='문자열')
#1) 숫자 찾기
print(re.findall('1234',st1)) #['1234'] -list
print(findall('[0-9]{3}',st1)) #0~9까지 3글자 ['123', '555']
print(findall('[0-9]{3,}',st1)) #0~9까지 3글자 이상  ['1234', '555']
print(findall('\\d{3,}',st1)) #['1234', '555']

print(findall('[가-힣]{3,}',st1)) #['홍길동', '이사도시']
print(findall('[a-z]{3}',st1))  #['abc']
print(findall('[a-z|A-Z]{3}',st1))  #['abc', 'ABC']

#공백단위로 토큰
str_list=st1.split(sep=' ') #['1234', 'abc홍길동', 'ABC_555_6', '이사도시']
print(str_list)

names=[] #'빈 list'
for s in str_list:
    tmp=findall('[가-힣]{3,}',s)
    print(tmp)

    ''' [], ['홍길동'],[], [이다도시]'''

    if tmp : #[]-> False, ['홍길동']->True
       names.append(tmp[0]) #['홍길동','이다도시'] -단일
       names.append(tmp) #[['홍길동'],[이다도시]] -중첩

print(names) #['홍길동','이다도시']

#접두어/접미어 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'
print(findall('^test',st2)) #['test']
print(findall('st$',st2)) #['st']

#종료문자 찾기
print(findall('.bc',st2)) #전체 문자가 3자이며, 끝이 bc로 끝나는 것 ['abc', 'mbc']
#시작 문자 찾기
print(findall('t.', st2)) #['te', 't1', 'te']

#4.단어찾기(\\W) : 한글, 영문 숫자 (특수문자 불용어 제외 )
st3 = 'test^홍길동 abc 대한*민국 123$tbc

words= findall('\\w{3,}',st3)
print(words)#3자 이상의 단어 찾기 ['test', '홍길동', 'abc', '123', 'tbc']

#5. 특정 문자열 제외 대괄호 풀면 접두어로 인식
print(findall('[^t]+',st3)) #['es', '^홍길동 abc 대한*민국 123$', 'bc']
print(findall('[^t]',st3)) #['e', 's', '^', '홍', '길', '동', ' ', 'a', 'b', 'c', ' ', '대', '한', '*', '민', '국', ' ', '1', '2', '3', '$', 'b', 'c']

#6.특수문자 제외
print(findall('[^^*$]+',st3)) #['test', '홍길동 abc 대한', '민국 123', 'tbc']

#2. match
#match(pattern='패턴',string='문자열')
#-패턴 일치 여부 반환 (일치 : object 반환, 불일치: NULL 반환 )

jumin="213546-1234567"
result=match("[0-9]{6}-[1-4]\\d{6}",jumin)
print(result) #none ->false
if result:
    print("정상 주민번호")
else:
    print("비정상 주민번호")

#3.sub('pattern','rep','string')
st3 = 'test^홍길동 abc 대한*민국 123$tbc

result=sub('[\^*$]','',st3)    #\:^ 특수기호 X (전처리 용도 많이 쓰임)
# \의미: 메타 문자가 아닌 일반 특수 문자
print(result) #test홍길동 abc 대한민국 123tbc



