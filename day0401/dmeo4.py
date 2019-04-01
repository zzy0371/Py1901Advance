"""
属性编写
"""
class Good():
    def __init__(self,_name):
        self.name = _name

    @property
    def gname(self):
        return self.name

    @gname.setter
    def gname(self,_name):
        self.name = _name

g1 = Good("tea")
print(g1.name)
g1.gname = "coffee"
print(g1.gname)
"调用形式  没有赋值就是获取  赋值就是设置"

