class Dog:

    def eat(self,food):
        print("%s吃%s"%(self.name,food))

    def introduce(self):
        print("我的名字是%s 我%s叫"%(self.name,self.jiao))


hsq = Dog()
hsq.jiao = "汪汪"
hsq.name = "哈士奇"
hsq.eat("狗粮")
hsq.introduce()

xtq = Dog()
xtq.jiao = '狂'
xtq.name = "啸天犬"
xtq.eat("二氧化碳")
xtq.introduce()
