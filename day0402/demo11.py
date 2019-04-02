"""
闭包：
函数的内部声明函数
外部函数返回内部函数的引用
内部函数可以访问外部函数局部变量
"""

def fun1(a):
    def fun2(b):
        nonlocal a
        a += 1
        return a+b
    return fun2

f = fun1(10)
print(hasattr(f))
print(type(f))



from day0402 import demo12
demo12.selectgoods()

demo12.insertorder()

"""
1开始调用函数  原始函数名+（）
2解释发现执行函数有装饰函数 将执行函数作为参数传递给装饰函数 并且执行装饰函数（将内部函数函数名返回）
3将装饰器返回的函数引用赋予 原始函数名（）
"""


