'''
문자열 처리
-문자열(string) 문자들의 순서 (index)집합
-indexing/slicing 가능
-문자열=상수 : 수정불가
'''

#1. 문자열 처리
#1) 문자열 유형
lineStr="this is one ling string" #한 줄 문자열
print(lineStr)

#여러줄의 문자열
multiStr='''this 
is multi line
string'''
print(multiStr)

multiStr2='this\nis multi line\n string' #\n
print(multiStr2)

#sql문 : 부서번호
deptno =int(input('부서번호 입력:'))
query = f"""select*from emp
where deptno={deptno}
order by sel decs"""
print(query)

query.
#2)문자열 연산(+,*)
print('python'+' program') #결합연산자 python program
print('python'+37)  #TypeError: can only concatenate str (not "int") to str
print('python'+str(37)) #python37
print('-'*30) #30번 반복

'''
object.member or object.member()
int.member 
str.member
'''

#3)문자열 처리 함수
lineStr = "this is one line string"
print(lineStr, type(lineStr)) # 내용, 자료형 출력
# this is one line string <class 'str'>
print('문자열 길이 : ', len(lineStr)) # 문자열 길이 :  23
print('t의 글자수 :', lineStr.count('t')) # t의 글자수 : 2

# 접두어 : 시작문자열
print(lineStr.startswith('this')) # True
print(lineStr.startswith('that')) # False

# 분리split : 토큰 생성
words = lineStr.split(sep=' ') # 문장 -> 단어
print(words) # ['this', 'is', 'one', 'line', 'string']
print('단어 길이 : ', len(words)) # 단어 길이 :  5

# 문단 -> 문장
multiStr = '''this
is multi line
string'''

sentences = multiStr.split(sep='\n')
print(sentences) # ['this', 'is multi line', 'string']
print('문장 길이 :', len(sentences)) # 문장 길이 : 3

#결합 (join):'구분자'
sentence=' '.join(words) #단어-> 문장
print(sentence) #this is one line string

para=','.join(sentences) #문장-> 문단
print(para) #this,is multi line,string

para=','.join(sentence) #문장-> 문단
print(para)  #t,h,i,s, ,i,s, ,o,n,e, ,l,i,n,e, ,s,t,r,i,n,g

#2)문단,문장
multiStr='''this
is multi line
string'''

sentenses=multiStr.split(sep='\n')
print(sentenses) #['this #enter ㅏ됴', 'is multi line', 'string']
print('문장 길이:',len(sentenses)) #문장 길이: 3

print(multiStr.upper()) #소문자-> 대문자
#THIS
#IS MULTI LINE
#STRING

#4)indexing/slicing
print(lineStr[0]) # t첫번째 문자
print(lineStr[-1]) #g 마지막 문자

print(lineStr[0:4]) #[start:end-1] this
print(lineStr[-6:]) #오른쪽 끝 6개  string

#2. escape문자 처리
'''
escape문자 :명령어 이외의 특수문자 (',",\n,\t,\b)
'''

print("\nescape 문자")  #escape 문자
print("\\nescape 문자") #\nescape 문자
print(r"\nescape 문자") #\nescape 문자

#c:\python\work\test
print('c:\python\work\test') #c:\python\work	est
print('c:\\python\\work\\test') #c:\python\work\test
print(r'c:\python\work\test') #c:\python\work\test