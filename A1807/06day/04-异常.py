try:
    #open('1.txt','r')
    #print(name)
    11/0
except (FileNotFoundRrror,NameError):
    print('报错了')
except Exception as ret:
    print('报错了','ret')
else:
    print('没有错误的执行')
finally:
    print('不管有错都执行')

