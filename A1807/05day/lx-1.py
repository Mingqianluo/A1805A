#count = 0
class Phone():
    def __init__(self,color):
        self.color = color
        Phone.count+=1

    def call(self):
        print('打电话')

xiaomi = Phone('白色')
#count+=1
xiaomi1 = Phone('黑色')
#count+=1
#print(count)
print(Phone.count)
