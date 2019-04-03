import time, datetime
#
#
# class Ly:
#     def __init__(self, fun):
#         self.fun = fun
#         print('this is the first step on ' + str(datetime.datetime.now()))
#         time.sleep(1)
#         self.fun()
#
#     def __call__(self):
#         print('this is the thirty step on ' + str(datetime.datetime.now()))
#         time.sleep(1)
#         return '++'
#
# @Ly
# def show():
#     print('this is the second step on ' + str(datetime.datetime.now()))
#     time.sleep(1)
#
# if __name__ == "__main__":
#     print(type(show))
#     print('this is the fourth step on ' + str(datetime.datetime.now()))

"""
解释器解释@Ly
将show()原始方法传递给构造函数 第一步执行
执行构造函数 将构造函数的返回值 赋予原函数（show函数 ） Ly()
当执行show函数相当于执行 Ly()()



函数式装饰器：将装饰函数内部函数引用赋予原函数 
类装饰器：    将装饰类的构造函数返回（实例）赋予原函数
 当类的内部有__call__方法是 类的实例成为可执行实例
实例（）   执行类内部__call__方法


"""

# class Ly(object):
#
#     def __init__(self, fun):
#         print("this is the first step")
#         time.sleep(1)
#         self.fun = fun
#
#     def __call__(self, *args):
#         print("this is the second step")
#         time.sleep(1)
#         self.fun(*args)
#         print("this is the fourth step")
#         time.sleep(1)
#
# @Ly
# def show(a1, a2, a3, a4):
#     print('this is the thirty step', a1, a2, a3, a4)
#     time.sleep(1)

# 此时show == Ly（）
# show() == ly()() 执行__call__
# 当解释器解释到类装饰器 将被装饰函数传入 类的构造（构造执行一次）  将构造返回值（实例）赋予原函数引用

#
# show("parm", "1", "1", "1")
# print("After first part call")
# time.sleep(1)
# show("parm", "2", "2", "2")
# print("After second part call")

# print(id(show))
# print(id(show))


# try:
#     print('++')
# except Exception as e:
#     print(e)
# else:
#     print('--')
# finally:
#     print('end')


import time

class Ly:
    def __init__(self, one_parm, two_parm, three_parm):
        self.one_parm = one_parm
        self.two_parm = two_parm
        self.three_parm = three_parm

    def __call__(self, fun):
        print('性别为' + self.one_parm + "的" + self.two_parm + "岁的" + self.three_parm)
        time.sleep(1)
        def info(*args):
            fun(*args)
        return info

@Ly("男", "22", "ly")
def show(name, age, sex):
    print('调用show方法传入参数  性别为' + sex + "的" + age + "岁的" + name)

# show == Ly("男", "22", "ly")

# show("蓝月", "20", "男")
# show("蓝月", "20", "男")




# def pulsp(f):
#     def p(*args):
#         print('--')
#         f(*args)
#     return p
#
# class Test():
#     @pulsp
#     def print(self):
#         print('++')
#
#
#     @staticmethod
#     @pulsp
#     def print1():
#         print('**')
#
#     @classmethod
#     @pulsp
#     def print2(cls):
#         print('//')
# t = Test()
# t.print()
#
# Test.print1()
# Test.print2()


