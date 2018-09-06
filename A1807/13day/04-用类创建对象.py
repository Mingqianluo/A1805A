from multiprocessing import Process
import time
class MyProcess(Process):
    def __init__(self):
        super().__init__()
    def run(self):
        for i in range(10):
            time.sleep(1)
            print('我爱老王')

p =MyProcess()
p1 =MyProcess()
p.start()
p1.start()
p.join(3)#最多等待3秒
time.sleep(3)
#p.terminate()#不管子进程是否结束，都立刻停止子进程
print('吃喝玩乐')
