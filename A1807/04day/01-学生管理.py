import time
import os
class people():
    def add(self,name):
        self.name = name
        self.xh = input("输入学号")
        f = open(name+".txt","w")        
        f.write("名字:%s\t学号%s\t"%(self.name,self.xh))
        f.close
    def dele(self,name):
        os.remove(name+".txt")
    def change(self):
        name = input("请输入名字")
        os.remove(name+".txt")
        a = input("输入修改后的名字")
        b = input("输入修改后的学号")
        f = open(a+'.txt','w')
        f.write("名字:%s\t学号%s\t"%(a,b))
        f.close
    def cat(self,name):
        f = open(name+'.txt','r')
        b = f.read()
        print(b)
        f.close

class fun():
    def choose(self):
        while True:
            os.chdir("学生资料")
            print("1.添加  2.删除  3.修改  4.查看  5.打印  0.退出")
            a = input("请选择功能序号")
            if a == '1':
                name = input("输入名字")
                laowang = people()
                laowang.add(name)
                os.chdir('../')
            
            elif a == '2':
                name = input("输入姓名")
                laowang = people()
                laowang.dele(name)
                os.chdir('../')
            elif a == '3':
                laowang = people()
                laowang.change()
                os.chdir('../')
            elif a == '4':
                name = input("输入名字")
                laowang = people()
                laowang.cat(name)
                os.chdir('../')
            elif a == '5':
                os.chdir('../')
                files = os.listdir('学生资料')
                for i in files:
                    print(i)
            elif a == '0':
                break
cc = fun()
cc.choose()
print("程序将于3秒后关闭...")
for i in range(3,0,-1):
    time.sleep(1)
    print(i)

