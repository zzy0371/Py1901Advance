"""
类 与对象（实例）
类：模板定义属性和方法的封装
实例：具体的类对象 ，类的表现

1实例属性会根据实例不同而不同，类属性由类决定
2实例属性通常在构造赋值
3类属性（类变量）属于类 ， 实例属性属于实例
实例确定，实例属性确定
实例可以调用类属性  ，类不可以调用实例属性
"""

class Good():
    name = 'tea'

    def __init__(self, _addr):
        self.addr = _addr

g1 = Good("fujian")
g2 = Good("guangdong")

print(g1.addr,g2.addr,g1.name,g2.name)
Good.name = 'coffee'
print(Good.name, g1.name)

# print(id(g1), id(g2))
# print(id(g1.name), id(g2.name), id(Good.name))

# 给g1对象添加name 属性
g1.name = 'cookle'

print(id(g1.name), id(g2.name), id(Good.name))



