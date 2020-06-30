# 1. 메서드 재정의
# 부모 클래스

class Super:
    data = None #멤버 변수

    #기본 생성자 : 객체만 생성

    #멤버 메서드 : 원형 메서드
    def superFunc(selfself): #인수 없음
        pass


#자식 1
class Sub1(Super):
    #data
    #def superFunc

    def superFunc(self, data):
        self.data=data
        print("자식1:data ={}".format(self.data))

sub1 = Sub1()

sub1.superFunc('20200414') #자식1 :data =20200414

#자식2
class Sub2(super):
    #data
    #def superFunc

    def superFunc(self, data):
        self.data =data
        print("자식2:data={}".format(self.data**2))

class Test:
    def superFunc(self, data): #확장 -> override
        self.data =data
        print("자식3 : data = {}".format(self.data**2))

sub2 = Sub2()
sub2.superFunc(100)
#자식2 : data = 10000


#다형성
sup = super() #부모 객체
