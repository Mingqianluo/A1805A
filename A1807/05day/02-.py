class Dog():
    print('哈哈哈哈')
    count = 10#类属性
    __count1 = 20
    def __init__(self,name):
        self.name = name #实例属性
        self.__age = 10#私有属性


    def getAge(self):
        return self.__age
    def getCount1(self):
        return Dog.count

    
    @classmethod
    def getCount(cls):
        print('我是类方法')

    @classmethod
    def getAge()



tom = Dog('Tom')
print(tom.name)
print(tom.getAge())

print(Dog.count)#通过类访问类方法
Dog.getCount()#通过类访问类方法
tom.getCount()#通过对象访问类方法

print(tom.getCount())
