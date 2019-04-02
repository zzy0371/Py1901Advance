

def newfunc(fun):
    def func():
        if input('输入用户名') == 'zzy':
            fun()
        else:
            print('没权限')
    return func

def showlist():
    print('显示列表')

# result = newfunc(showlist)
# result()

# showlist = newfunc(showlist)
# showlist()

showlist()



"""
解释器解释到有装饰器的函数：会改变函数结构
把函数作为参数传给装饰器，并且执行装饰器的返回值（装饰器返回的为内部函数）
把装饰器内部函数付给被装饰函数
"""


