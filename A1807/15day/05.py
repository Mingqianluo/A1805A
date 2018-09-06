from socket import *
s = socket (AF_INET,SOCK_DGRAM)#创建一个udp的套接字

s.bind(('',8080))#绑定端口

while True:
    content = input('请输入内容')
    s.sendto(content.encode('gb2312'),('192.168.43.59',8080))
    msg = s.recvfrom(1024)
    print('消息是%s来自IP%s'%(msg[0].decode('gb2312'),msg[1][0]))
s.close()
