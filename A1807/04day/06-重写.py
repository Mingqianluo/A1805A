class Dog():

    def wark(self):
        print('汪汪汪')

class hsq(Dog):
    def wark(self):
        print('嗷嗷嗷')

class xtq(Dog):
    def wark(self):
        print('狂叫')
        Dog.wark(self)
hsq1 = hsq() 
hsq.wark()

xtq1=xtq()
xtq.wark()
