import time
from threading import Thread
def work(i):
    num = 0
    time.sleep(i)
    num+=1
    print(num)

t = Thread(target=work,args=(3,))
t1 = Thread(target = work,args = (5,))
t.start()
t1.start()

