from threading import Threed
import time

def work():
    for i in range(10):
        print('.....')


t = Thread(target =work)

