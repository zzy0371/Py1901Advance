def renameattr(classname, parentclass ,attrs):
    print('通过原方法重新定义类')
    # print(classname, type(classname))
    # print(parentclass)
    # print(attrs)
#     g_id  g_name
    # print(classname.lower()[0]+"_")
    newattr = {}
    for k,v in attrs.items():
        if not k.startswith("__"):
            # print(k,v)
            k = classname.lower()[0]+"_"+k
            # print(k)
            newattr[k] = v
    # print(newattr)
    return type(classname,parentclass,newattr)
class Good(metaclass = renameattr):
    id = None
    name = None
g = Good()
# print(g)
# print(g.__dir__())
print(hasattr(Good,"name"))
print(hasattr(g,"g_name"))




"""
添加限制 所有的属性需要以类名的首字母的小写开头
class Good():
    g_id = None
    g_name = None
    
metaclass = fun(classname, parentclass, atts )

创建类之前修改的定义
"""

