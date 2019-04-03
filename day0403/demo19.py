# class Good():
#     pass
#
# g = Good()

# print(isinstance(g, Good))
# print(type(g))
# print(type(Good))
# print(type(type))

Gd = type("Good",(),{"id":0})
g = Gd()
# print(type(Good), type(g))
Tea = type("Tea",(Gd,),{"name":'chinatea'})

print(Gd.__bases__)
print(Gd.__class__)
print(g.__class__)

print('-------')
print(Tea.__bases__)
print(Tea.__class__)

t = Tea()
# print(t, type(t))

print( hasattr(Gd,"name")  )
print(hasattr(Tea,"name"))
print(hasattr(t,"name"))

t.name = 20

print(hasattr(Tea,"price"))

print(hasattr(t, "id"))


def get():
    pass

def getn(self):
    return self.name

@classmethod
def getd(cls):
    print(cls.__dict__)

@staticmethod
def log(strinfo):
    print(strinfo)

Tie = type("TieTea",(Tea,),{"addr":'henan',"getname":getn, "getdoc":getd, "log": log })

# print(TieTea.getname())
tt = Tie()
print(tt.getname())

Tie.getdoc()

Tie.log("hello world")


"""
如何使用type创建类
第一个参数为 类名（字符串）
第二个参数为 父类列表
第三个参数为 属性方法列表
hasattr(对象,属性字符串)
delattr()
setattr()
__base__
__class__

"""
