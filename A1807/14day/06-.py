import time
from threading import Thread
#多线程对于全局变量共享
#多线程不共享局部变量
def work(i):
    num = 0
    time.sleep(i)
    num+=1
    print(num)

def work1(i):
    num = 0
    time.sleep(i)
    num+=2
    print(num)

t = Thread(target=work,args=(3,))
t1 = Thread(target=work1,args=(5,))
t.start()
t1.start()
