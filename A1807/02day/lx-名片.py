import time
import os
class people():
    def add(self,name):#添加
        self.name = name
        self.age = input('输入年龄')
        f = open(name+'.txt','w')
        f.write('名字:%s\t年龄%s\t'%(self.name,self.age))
        f.close
    def delete(self,name):#删除
        os.remove(name+'.txt')

    def change(self):#修改
        name = input('请输入要修改的名字')
        os.remove(name+'.txt')
        a = input('输入修改后的名字')
        b = input('输入修改后的年龄')
        f = open(a+'.txt','r')
        b = write('名字:%s\t年龄%S\t'%(a,b))
        f.close

    def cat(self,name):
        f = open(name+'.txt','r')
        b = f.read()
        print(b)
        f.close

class fun():
    def choose(self):
        while True:
            os.chdir('名片管理')
            print('1.添加 2.删除 3.修改 4.查看 5.打印 0.退出')
            a = input('请选择功能序号')
            if a == '1':
                name = input('输入名字')
                n = people()
                n.add(name)
                os.chdir('../')

            elif a == '2':
                name = input('输入姓名')
                n = people()
                n.dele(name)
                os.chdir('../')
            elif a == '3':
                n = people()
                n.changr()
                os.chdir('../')

            elif a == '4':
                name = input('输入名字')
                n = people()
                n.cat(name)
                os.chdir('../')
            elif a == '5':
                os.chdir('../')
                files = os.listdir('名片管理')
                for i in files:
                    print(i)
            elif a == '0':
                break

cc = fun()
cc.choose()
print('程序将于3秒后关闭......')
for i in range(3,0,-1):
    time.sleep(1)
    print(i)

