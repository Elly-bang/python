'''
step01 문제 

문) 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오.

 << 출력 결과 >>
단계1 :  [10, 1, 5, 2, 10, 1, 5, 2]
단계2 : [10, 1, 5, 2, 10, 1, 5, 2, 20]
단계3 : [1, 2, 1, 2]
'''

lst = [10, 1, 5, 2] # list 생성
print(lst)
# 단계1 : lst 원소를 2개 생성하여 result 변수에 저장/출력
result=lst*2
print("단계 1:",result)
# 단계2 : lst의 첫번째 원소에 2를 곱하여 result 변수에 추가/출력

y=lst[0]*2
result.extend(y)
print("단계 2:",result)



# 단계3 : result의 홀수 번째 원소만 result2 변수에 추가/출력
result2=result

print(x[:]) #전체 데이터 호출
print(x[::2]) #[::step=2]:홀수형태
print(x[1::2]) #[start::step2]:짝수형태