from socket import *

#创建一个udp的套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',8080))
#对方ip端口
s.sendto('哈哈哈'.encode('gb2312'),('192.168.43.59',8080))
while True:
    msg = s.recvfrom(1024)
    print(msg[0].decode('gb2312'),msg[1][0])
s.close()
