'''
기본(default) 생성자
-생성자를 생략하면 기본 생성자가 만들어진다.
-묵시적 생성자
'''
class default_cost:
    #생성자 생략
    '''
    def __init__(self): #기본 생성자
        pass
    '''

    def data(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        re =self.x * self.y
        return re

obj = default_cost() #빈 괄호 기본 생성자
obj.data(10, 20) #data생성
print('mul=',obj.mul()) #연산 mul=200

#TV class 정의
class TV: #class = 변수(명사,자료) + 메서드(동사, 자료 처리 기능)
    #멤버 변수 : 자료 저장
    channel = volume = 0
    power = False #off(False) -> on (True)
    color = None #Null

    #기본 생성자
    '''def __init__(self): #기본 생성자 생략
        pass
'''

    #멤버 메서드 : 리모컨 역할
    def volumeUp(self):
        self.volume += 1
    def volumeDown(self):
        self.volume += 1
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel += 1
    def channelPower(self):
        self.power= not (self.power) #반전 (T<->F)

#멤버 변수 초기화 메서드
    def data(self, channel, volume, color ):
        self.chnnel =channel0
        self.volume = volume
        self.color = color

# TV 정보 출력 메서드
     def display(self):
         print("전원 :{}, 채널:{}, 볼륨: {}, 색상: {}"
               .format(self.power, self.channel, self.volume, self.color))

#객체 생성
tv1 = TV() #기본 생성자 -> 객체
#tv1.display()
#전원 :False, 채널:0, 볼륨: 0, 색상: None
tv1.data(5, 10, '검정색')
tv1.display()
#전원 :False, 채널:0, 볼륨: 10, 색상: 검정색
tv1.changePower()
tv1.channelUp()
tv1.volumeUp()
tv1.display()

'''
문) tv2 객체를 다음과 같이 생ㅅ어하시오.
단계1 )전원 : False, 채널 : 1, 볼륨:1, 색상 : 파랑색
단계2 )전원 : True, 채널 : 10, 볼륨:15, 
단계3 ) tv2 객체 정보 출력 
'''

tv2 = TV()
tv2.data(1, 1, '파랑색')

