import random
import time
class Digua():
    def __init__(self):
        self.status = '生的'
        self.time = 0


    def __str__(self):
        msg = '我烤的程度%s'%self.status
        return msg
    def cook(self,time):
        self.time += time
        if self.time >= 1 and self.time <= 2:
            self.status = '生的'
        elif self.time >= 3 and self.time <= 5:
            self.statue = '半生不熟'
        elif self.time >= 6 and self.time <= 8:
            self.status = '八分熟'
        elif self.time >= 9 and self.time <= 12:
            self.status = '正好'
        elif self.time > 12:
            self.status = '焦了'

digua = Digua()
for i in range(5):
    digua.cook(random.randint(1,4))
        
    print(digua)

