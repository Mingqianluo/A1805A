class people():
    def __init__(self,name):
        self.name = name
        self.gun = None#刚初始化时没有枪

    def zhuangzd(self,dj,zd):
        dj.addzd(zd)

    def zhuangdj(self,dj,gun):#装弹夹
        gun.addDanjia(dj)#枪自己装子弹

    def nq(self,gun):#拿枪
        self.gun = gun

    def kq(self,dr):#老王开枪
        self.gun.kh(diren)



class gun():
    def __init__(self,name):
        self.name = name
        self.dj = None

    def adddj(self,zd):
        self.dj = dj

    def kh(self):
        zd = self.dj.tzd()
class clip():
    def __init__(self,name):
        self.name = name
        self.zds = []#子弹列表

    def addzd(self,zd):
        self.zds.append(zd)#装子弹
    
    def tzd(self):
        self.zds.pop(0)


class bullet():
    def __init__(self,name):
        self.name = name
        self.sh = sh









lw = people('老王')
FAL = gun('FAL')
biaozhun = clip(30)
for i in range(30):
    zd = bullet('7.62',5)
    laowang.zhuangzd(dj,zd)
laowang.zhuangdj(dj,FAL)
laowang.nq(FAL)



