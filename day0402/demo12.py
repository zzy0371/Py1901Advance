"""
装饰器：为了扩展函数的功能，
由闭包+语法糖
@

"""

# 在查询逻辑之前需要添加权限验证
def check(fun):
    def ck():
        # print(type(fun), fun.__name__)
        user = input("输入用户名")
        if user == "zzy":
            fun()
        else:
            print('无权限')
        # fun()
    return ck

@check
def selectgoods():
    print('封装查询商品逻辑')
    # 。。。。。。

@check
def insertorder():
    print('插入订单')


