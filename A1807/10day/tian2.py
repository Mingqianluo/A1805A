date = input('请输入日期')
year= int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])
big = [1,3,5,7,8,10,12]
small = [4,6,9,11]
if (year % 4 == 0) or (year % 100 != 0) or (year % 400 == 0):
    a = 1
else:
    a = 2
day1 = 0
for i in range(1,month+1):
    if i in big:
        day1 += 31
    elif i in small:
        day1 += 30
    elif a == 1 and i == 2:
        day1 += 28
    elif i == 2 :
        day1 += 29
if month in big:
    day2 = 31
else:
    day2 = 30
day1 -= (day2-day)
print(day1)
