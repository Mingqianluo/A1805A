class try1(Exception):
    def __init__(self,name):
        self.name = name

        
        
        
class try2():
    def my_input(self):
        name = input('请输入名字')
        try:
            if name == '老王':
                raise try1(name)
        except try1 as ret:
            print('输入%s就报错'%ret.name)

im = try2()
im.my_input()
