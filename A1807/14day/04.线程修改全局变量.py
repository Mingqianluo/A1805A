from threading import Thread
import time

num = 0

def test():
    global num
    m.acquire(True)
    for i in range(10000):
        num+=1
    m.release()
    print(num)
    print('thread-1')

def test1():
    global num
    for i in range(10000):
        num +=1
    m.release()
    print(num)

t = Thread(target = test)
t.start()

t1 = Thread(target = test1)
t1.start()

print('num = %d'%num)
    
