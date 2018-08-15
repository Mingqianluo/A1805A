import random
class Cq:
    def cq(self):
        userInput = 'begin'
        while userInput=='begin':
                shitou = '石头'
                jiandao = '剪刀'
                bu = '布'
                user = str(input("请用户出小拳拳(q退出)："))
                if user == 'q':
                    break
                pc = random.randint(1,3) # 2; 3)
                if pc == 1:
                    pcStr = shitou
                    print("电脑出了:石头")
                elif pc == 2:
                    pcStr = jiandao
                    print("电脑出了:剪刀")
                else:
                    pcStr = bu
                    print("电脑出了:布")
                if (user==shitou and pcStr==jiandao) or (user==jiandao and pcStr==bu) or (user==bu and pcStr==shitou):
                    print('电脑太弱了')
                elif user == pcStr:
                    print('平局')
                else:
                    print('你输了')

a = Cq()
a.cq()
