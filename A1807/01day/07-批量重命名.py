import os
name = input('请输入要重命名的文件夹')
files = os.listdir(name)
for i in files:
    p = i.rfind('.')
    n = i[:p] +'-腾讯'+i[p:]
    old_name = name +'/' + i#1/1.txt
    new_name = name + '/' +n
    os.rename(old_name,new_name)
