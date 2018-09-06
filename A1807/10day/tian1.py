def com_days(year,month,day):
    big_month = [1,3,5,7,8,10,12]
    small_month = [4,6,9,11]
    for i in range(1,month):
        if i in big_month:
            day+=31
        if i in small_month:
            day += 30
        if i == 2:
            if (year%4 == 0 and year % 100 != 0) or year % 400 == 0:
                day += 29
            else:
                day += 28
    day+=day
    print('%d'%day)
date = '20180817'
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])
com_days(year,month,day)
