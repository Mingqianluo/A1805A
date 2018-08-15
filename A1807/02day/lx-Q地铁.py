import random
class Dt:
    def ditie(self):
        m = 0
        for i in range(1,31):
            for i in range(1,3):
                km = random.randint(1,34)
                #km=64
                if km <=6:
                    price = 3
                elif km > 6 and km <= 12:
                    price = 4
                elif km > 12 and km <= 22:
                    price = 5
                elif km > 22 and km <= 32:
                    price = 6
                elif km > 32:
                    if (km-32)%20 == 0:
                        price=6+(km-32)/20
                    else:
                        price=6+int((km-32)/20)+1

                if m >100 and m <= 150:
                    price = price *0.8
                elif m > 150 and m <= 400:
                    price = price *0.5
                elif m >400:
                    price = price*1
                m = m + price
        print(m)
        if m > 214:
            print('花Q')

a = Dt()
a.ditie()
