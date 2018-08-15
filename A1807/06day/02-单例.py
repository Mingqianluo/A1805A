class Dog():
    instance = None
    def __new__(cls):
        if cls.instance == None:
            cls.instance = super.__new__(cls)
            return cls.instance
        else:
            return cls.__instance

    def __init__(self,name):
        

dog1 = Dog()
print(id(dog1))
