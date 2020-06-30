'''
문2-2) 다음 벡터(emp)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 다음과 같은 출력결과가 나타나도록 함수를 정의하시오. 

# <출력 결과>
 전체 사원 급여 평균 : 260
'''

from re import findall
from statistics import mean

# <Vector 준비>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
'''
def name_pro(emp):
     names = []
     for e in emp: 
         tmp= findall('[가-힣]{3}', e)
         if tmp :
             names.append(tmp[0])
   return names
'''

# list 내포 : 변수 =[실행문 for 변수 in 열거형 객체}
names= [findall('[가-힣]{3}',e) [0] for e in emp]
return names

# 함수 호출
# names= name_pro(emp)
print('전체 사원의 급여 평균 :', pays_mean)





