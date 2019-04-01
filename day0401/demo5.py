import types
class Good():
    """
    这是一个商品类
    """
    # 通过slots 限制动态添加内容
    __slots__ = ("name",'addr','price',"geti")
    def __init__(self, _addr):
        self.addr = _addr

g1 = Good("fujian")
g2 = Good("guangdong")


#
# 通过类名添加类属性  通过实例名添加实例属性
# 动态添加 实例方法 类方法 静态方法

def getinfo(self):
    print(self.addr)

# 动态的添加实例方法
g2.geti = types.MethodType(getinfo, g2)

g2.geti()

@classmethod
def getdoc(cls):
    print(cls.__doc__)
# 动态的添加类方法
Good.getd = getdoc

Good.getd()
g1.getd()
# g1.geti()

@staticmethod
def get():
    print("static method")

Good.get = get

Good.get()

delattr(Good,"get")
# del Good.get
if hasattr(Good, "get"):
    print("存在get")
else:
    print("不存在get")


if hasattr(g1, "geti"):
    print("存在geti")
else:
    print("不存在geti")



