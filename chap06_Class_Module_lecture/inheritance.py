'''
클래스 상속
상속대상 : 멤버 (o)+ 생성자 (x)
 -> 생성자 상속 대상 아님
형식)
class 자식 클래스
      멤버 (변수 + 메서드)
      생성자

self vs super()
self.member : 현재 크랠스의 멤버 호출
super().member : 부모 클래스의 멤버 호출
'''

class Super:
    name = None
    age = 0

    #생성자 : 객체 생성+ 초기화

    def __init__(self, name, age):
        self.name = name
        self.age = age

    #멤버 메서드 : 데이터 처리

    def display(self):
        print(" 이름 : {}, 나이 : {}".format(self.name, self.age))

#object 생성
sup = Super("부모", 55)
del super

sup.display() #이름: 부모, 나이 : 55

#자식 클래스
class Sub(Super):
    gender = None

    def __init__(self, name, age, gender):
        super().__init__(name, age )

        self.gender = gender

    def display(self):
        print("이름 : {}, 나이:{}, 성별:{}"
              .format(self.name, self.age, self.gender))

#object
sub = Sub('자식', 22, '남자')
sub. display()

class Parent:
    name = job = None

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def display(self):
        print("이름 : {}, 직업 :{}".format(self.name, self.job))


p = Parent('홍길동', '공무원')
p.display()

class Children1(Parent):
    gender = None


    def __init__(self, name, job, gender):
        super().__init__(name,job)
        self.gender= gender


    def display(self):
        print("이름 : {}, 직업:{}, 성별:{}"
              .format(self.name, self.job,self.gender))


ch1 =Children1("이순신","군인","남자")
ch1.display()

class Children2(Parent):
    gender = None

    def __init__(self, name, job, gender):
        super().__init__(name,job)
        self.gender = gender


    def display(self):
        print("이름 :{}, 직업:{}, 성별:{}"
              .format(self.name, self.job, self.gender))

ch2 = Children2("유관순", "독립열사 ", "여자")
ch2.display()

