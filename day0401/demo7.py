"""
函数式生成器
通过函数+yield

yield 可以保存当前函数状态并继续执行
每一次yield向当前生成器插入对象

函数返回值变成生成器
可以使用异常捕获得到函数 return语句返回值
"""

def fun():
    yield 1
    yield 2
    yield 3
    return "hello"

# print(type(fun()))
# print(next(fun()))
# for r in fun():
#     print(r)

g = fun()
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g),'--')
except StopIteration as e:
    print(e,'++')