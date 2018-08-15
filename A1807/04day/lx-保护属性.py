class people:
    def __init__(self,name):
        self.__name = name
        self.age = 18
    def getName(self):
        return self.__name
    def setName(self,newName):
        if len(newName) >= 5:
            self.__name = newName
        else:print('错误')

xm = people('adsfs')
print(xm.getName())
print(xm.age)
