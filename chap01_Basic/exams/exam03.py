'''
step03 문제 
'''

'''
문) 3개의 단어를 키보드로 입력 받아서 각 단어의 첫자를 추출하여 단어의 약자를 출력하시오.
  조건1) 각 단어 변수(word1, word2, word3) 저장 
  조건2) 입력과 출력 구분선 : 문자열 연산 
  조건3) 각 변수의 첫 단어만 추출하여 변수(abbr) 저장
   
   <<화면출력 결과>>  
 첫번째 단어 : Korea 
 두번째 단어 : Baseball
 세번째 단어 : Orag
 =================
 약자 : KBO
'''
word1="Korea"
word2="Baseball"
word3="Orag"
abbr= word1[0]+word2[0]+word3[0]
print(abbr)
print("첫번째 단어 :", word1)
print("두번째 단어 :", word2)
print("세번째 단어 :", word3)
print('='*17)
print("약자 :", abbr)