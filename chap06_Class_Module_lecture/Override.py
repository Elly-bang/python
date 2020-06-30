class Super:
    data = None

    def superFunc(self):
        pass

class Sub1(Super):

    def superFunc(self, data):
        self.data = data
        print("자식1 : data={}".format(self.data))

sub1 = Sub1()
sub1.superFunc('2020414')

class Sub2(Super):

    def superFunc(self, data):
        self.data = data
        print("자식2 : data = {}".format(self.data**2))

class Test:
    def superFunc(self, data):
        self.data =data
        print("자식 3 : data = {}". format(self.data**2))

sub2 = Sub2()
sub2.superFunc(100)

sup = Super()
sub1 = Sub1()
sub2 = Sub2()

sup = sub1
sup.superFunc(100)
sup = sub2
sup.superFunc(100)

