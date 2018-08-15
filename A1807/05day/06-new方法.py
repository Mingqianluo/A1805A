class Dog():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'I am dog'

    def __del__(self):
        print('dog die')
        
    def __new__(cls):
       return super().__new__(cls)

dog = Dog('hadou')#执行init
print(dog)
del dog
