import re
'''
def checkphone(phone):
    ret = re.match('1[3456789][\d]{9}',phone)
    if ret:
        print('合法')
        return True
    else:
        return False
        print('不合法')



ret = checkphone('17600121183')
#re.match('[\w]{4,20}@163\.com','zhaoweiq@163.com')
'''
ret = re.match(r'<(\w+)><(\w+)>.+</\2></\1>',"<h1><li>老王</li></h1>")
print(ret)
