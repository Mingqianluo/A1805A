class Bank():
    def __init__(self,account,pwd,name):
        self.account = account
        self.__pwd = pwd
        self.name = name

    def getPwd(self):
        return self.__pwd

    def setPwd(self,pwd):
        self.__pwd = pwd

    def getMoney(self):
        return 10000000

    def check(self,account,pwd):
        if account == self.account and pwd == self.__pwd:
            return self.__getMoney()
        else:
            print('验证失败')

bank = Bank('123','123','花旗')
print(bank.account)
print(bank.getPwd())
print(bank.name)
bank.setPwd('456')
print(bank,getPwd())

print(bank.check('123','456'))
