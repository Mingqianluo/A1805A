date =input('请输入日期')
y = date[:4]
m = date[4:6]
d = date[6:9]
big = [1,3,5,7,8,10,12]
small = [2,4,6,9,11]
if (y % 4 == 0) or (y % 100 != 0) or (y % 400 == 0):
    return 1
else:
    return 0
day = 0
for i in range(1,m+1):
    if i in big:
        day += 31
    elif i in small:
        day += 30
    elif return and i ==2:
        day += 29
    elif i == 2:
        day += 28
