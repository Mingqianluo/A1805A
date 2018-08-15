class BMI:
    def bmi(self):
        h = float(input('身高'))
        w = float(input('体重'))
        c = w/ h**2
        print(c)
        if c < 18.5:
            print('过轻')
        elif c > 18.5 and c < 25:
            print('正常')
        elif c > 25 and c > 28:
            print('过重')
        elif c > 28 and c < 32:
            print('肥胖')
        elif c > 32:
            print('严重肥胖')
            
b = BMI()
b.bmi()
