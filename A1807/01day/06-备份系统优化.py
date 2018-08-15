name = input('请输入备份文件的名字(要有后缀名)')
f = open(name,'r')
content = f.read()
a = name.rfind('.')
f1 = open(name[:a]+'备份'+'.txt','w')
while True:
    content = f.read(1024)
    f1.write(content)
    if len(content) == 0:
        break
f.close()
f1.close()

