from threading import Thread
import time

num = 0
def work1(l):
    time.sleep(5)
    print(num)
    print(l)
def work2(l):
    global num
    time.sleep(3)
    l.append(4)
    num += 1
    print(num)
    print(l)

list = [1,2,3]

t1 = Thread(target = work1,args = (list,))
t2 = Thread(target = work2,args = (list,))
t1.start()
t2.start()
