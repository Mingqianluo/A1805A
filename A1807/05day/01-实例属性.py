class Dog():
    print('哈哈哈哈')
    count = 10#类属性
    def __init__(self,name):
        self.name = name #实例属性
        self.__age = 10


    def getAge(self):
        return self.__age


tom = Dog('Tom')
print(tom.name)
print(tom.getAge())

print(Dog.count)#通过类访问类方法
