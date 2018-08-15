class Animal():
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

jiafei = Cat('加菲猫','橘色')
print(jiafei.name)
print(jiafei.color)

jierui = Mouse('杰瑞','灰色')
print(jierui.name)
print(jierui.color)
