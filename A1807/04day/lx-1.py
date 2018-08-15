class Dog():
    def __init__(self):
        self.name = '二哈'
        print('init')
    def __str__(self):
        return 'str'
    def __del__(self):
        print('我del')


dog = Dog()
print(dog)
dog1 = dog
del dog
del dog1
print('哈哈')

