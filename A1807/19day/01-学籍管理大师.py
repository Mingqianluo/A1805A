class StuManger():
    def __init__(self):
        self.list = []
        self.read()
        print(self.list[0].name)
    def save(self):
        name = input('请输入名字')

