"""
类装饰器：用类装饰器
"""

# class Good():
#     def __init__(self, _name):
#         print('构造调用')
#         self.name = _name
#     def __call__(self, *args, **kwargs):
#         print('实例调用')

# print("hello")
# print(Good("456"))

# g1 = Good("tea")
# print('--------------')
# g1()

"""
可调用对象 ：类，函数，实例
"""


class Decor():
    def __init__(self, _f):
        if input('用户名') == 'zzy':
            self.f = _f
            self.f()
        else:
            print('无权限')




@Decor
def fun():
    print("执行原始函数")









# fun = Decor(fun).f
# fun()
