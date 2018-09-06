import re
s1 = '我19岁'
def add(x):
    num = int(x.group())+5
    return str(num)
s2 = re.sub(r'(\d+)',add,s1)
print(s2)
