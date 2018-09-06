from threading import Thread
from socket import *

s = None
ip = ''
port = 0
def send():
    while True:
        content = input('请输入发送内容')
        s.sendto(content.encode('gb2312'),(ip,port))

def recv():
    while True:
        msg = s.recvfrom(1024)
        


