class Car():
    def __init__(self,color):
        self.color = color

    def run(self):
        print('----run----')

class Bmw(Car):
    def __init__(self,color):
        self.count = 6
        super().__init__(color)

    def run(self):
        print('bmw--run')

class BenChi(Car):
    def run(self):
        print('benchi--run')
class CarFactory():
    def create(self,type):
        if type == 1:
            return Bmw('红色')
        elif type == 2:
            return BenChi('黑色')
#bmw = Bmw('红色')
#benchi = BenChi('黑色')

bmw = CarFactory().create(1)
benchi = CarFactory().create(2)
