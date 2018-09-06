from socket import *

s = socket(AF_INET,SOCK_STREAM)


#这是个链接服务器，做了一件三次握手
s.connect(('192.168.43.59',6666))
while True:
    content = input('请输入内容')
    
    s.send(content.encode('gb2312'))

    msg = s.recv(1024)
    print(msg.decode('gb2312'))
