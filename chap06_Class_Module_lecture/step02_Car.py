'''
동적 멤버 변수 생성
-필요한 경우 특정 함수 또는 생성자에 변수 생성
self : 자신의 멤버, 클래스의 멤버를 호출하는 역할
self.멤버 변수
self.멤버 메서드()
'''

class Car :
    #멤버 변수
    #door = cc = 0
    #name = None #null

    #생성자 : 객체 + 변수 초기화
    def __init__(self, door, cc, name) :
        #self.멤버 변수 = 매개 변수
        self.door = door #동적멤버 변수 생성 1
        self.cc = cc #동적멤버 변수 생성 2
        self.name = name #동적멤버 변수 생성 3

    #멤버 메서드 : 자료 처리
    def info(self):
        self.kind = "" #동적 멤버 변수 4
        if self.cc >= 3000 :  #참조 self뒤에 멤버.변수명 하면, 변수 생성
            self.kind = "대형"
        else :
            self.kind = "소형"
        self.display()

    def display(self):
        print("%s는 %d cc이고(%s), 문짝은 %d개 이다"
              %(self.name, self.cc, self.kind, self.door))

#객체 1생성 : 생성자() -> object
car1=Car(4, 2000, '소나타')
#car1.member or car1.member()
print('자동차 명 :', car1.name)
car1.info()

# 객체 2생성
car2 = Car(4, 3000, '그랜저')
print('자동차 명 :', car2.name)
car2.info()


