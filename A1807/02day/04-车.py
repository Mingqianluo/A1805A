class Car():
    def __init__(self,model,color):
        
        self.model = model
        self.color = color
    def __str__(self):

        msg = '我是%s,我的颜色是%s'%(self.model,self.color)
        return msg
    def run(self):
        print('用四个轮子跑')
    def music(self):
        print('活动小丑')

QQ = Car('qq','蓝色')
QQ.run()
QQ.music()
print(QQ)
