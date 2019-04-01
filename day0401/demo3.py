"""
类属性类方法
类属性类方法 属于类 只占一份内存
实例方法，实例属性属于实例 每使用一个实例生成一个内存
声明实例属性，实例方法 浪费内存，适当的选择声明类属性和类方法节省内存

"""

class Util():
    @staticmethod
    def max(x,y):
        if x>y:
            return x
        else:
            return y


