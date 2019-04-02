

# 将函数作为参数传递给装饰器  并且执行装饰器 的返回
def checkuser(fun):
    # print('++') //发现装饰器语法 就执行

    def check(*args):
        if input("用户名") == 'zzy':
            fun(*args )
        else:
            print('登录失败')

    return check



@checkuser
def showlist():
    for r in range(10):
        print(r)
@checkuser
def showdetail(num):
    print('当前页',num)
@checkuser
def showmoney():
    print('当前剩余')

showlist()

# showdetail(10)
