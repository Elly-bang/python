'''
 문) 동적 멤버 변수 생성으로 다음과 같은 산포도를 구하는 클래스를 정의하시오.
 
class Scattering :         
        
        생성자 : 객체 + 동적멤버 생성
        
        분산 함수(var_func) var= sum((x변량-평균)**2) / (n-1)

        표준편차 함수(std_func)  std= sqrt(분산)
        
        
   << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]

print(mean(x))

'''
분산 = sum((x변량-평균)**2) / (n-1)
표준편차 = sqrt(분산)
'''

def var_std(dx) :
    avg = mean(x) # 산술평균
    # list + for

    diff = [(x-avg)**2 for x in x]  # (x변량-평균)**2
    diff_sum = sum(diff)

    var = diff_sum / (len(x) - 1) # 분산
    std = sqrt(var) # 표준편차
    return var, std

# 함수 호출
var, std = var_std(x)
print('분산 = ', var) #분산 =  7.466666666666666
print('표준편차 =', std) #표준편차 = 2.7325202042558927



 
        
    
    



