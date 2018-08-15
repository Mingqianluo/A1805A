import random
class Guess:
    
    
    def guess(self):
        
        
        a = random.randint(0,101)
        while True:
            u = int(input('请输入数字'))
            if u > a:
                print('猜大了')
            elif u < a:
                print('猜小了')
            else:
                print('猜对了')
                break
            

g = Guess()
g.guess()

