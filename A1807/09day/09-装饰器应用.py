def q1(f):
    def inner():
        print('扫描二维码')
        f()
    return inner

@q1
def pay():
    print('无法识别')

pay()
