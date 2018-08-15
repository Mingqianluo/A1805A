class QQ():

    def openvip(self):
        print('开通会员成功')

    def checkqq(self,money):
        if money > 10:
            self.__openvip()
        else:
            print('不能开')

qq = QQ()
qq.openvip(12)
#qq1 = QQ()
