from multiprocessing import Process
import time

def show(name):
    for i in range(10):
        time.sleep(2)
        print(name)

p = Process(target=show,args=('割草',))
p.start()
#p.join(3)#最多等待3秒
time.sleep(3)
p.terminate()#不管子进程是否结束，都立刻停止子进程
print('吃喝玩乐')
