
class Car:

    def __init__(self, door, cc, name):
        self.door = door
        self.cc = cc
        self.name= name

    def info(self):
        self.kind = ""
        if self.cc >= 3000:
            self.kind = "대형"

        else:
            self.kind = "소형"

        self.display()

    def display(self):
        print("%s는 %d cc이고(%s), 문짝은 %d개 이다"
              %(self.name, self.cc, self.kind, self.door))


#객체 1생성 : 생성자 -> object
car1 = Car(4, 2000, '소나타')
print('자동차 명 : ', car1.name)
car1.info()

car2 = Car(4,3000,'그랜져')
print('자동차 명 : ', car1.name)
car2.info()


