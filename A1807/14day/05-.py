from threading import Thread
import time
num = 0
flag = 1
def work():
    global num,flag
    if flag == 1:
        for i in range(100000):
            num +=1
            print('thread-1')
            print(num)
            flag = 2

def work1():
    global num
    while True:
        if flag == 2:
            for i in range(100000):
    
                num +=1
    print('thread-2')
    print(num)

t1 = Thread(target = work)
t1 = start()

t2 = Thread(target = work1)
t2 = start()
print(num)
