class A():
    def __init__(self):
        self.name = 10
        self.age = 20
        
    def show(self):
        print('heheh A')
class B():
    def show(self):
        print('哈哈哈')
        self.age = 30



class C(A,B):
    pass


c= C()
print(c.name)
print(c.age)
c.show()
c.show1()
print(C.__mro__)
