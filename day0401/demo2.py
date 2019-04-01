"""
实例方法：需要第一个参数为self
类方法：需要第一个参数为cls,并且使用@classmethod声明
静态方法:需要使用@staticmethod声明

类可以调用，类方法， 静态方法
实例可以调用, 类方法，静态方法，实例方法

"""
class Good():
    """
    这是一个商品类
    """
    def __init__(self,_name):
        self.name = _name

    def getname(self):
        return self.name

    @classmethod
    def getinfo(cls):
        print(cls.__doc__)


    @staticmethod
    def pprint():
        print("hellogood")

g1 = Good("tea")
print(g1.getname())
g1.getinfo()
g1.pprint()

# Good.getname()
Good.getinfo()
Good.pprint()