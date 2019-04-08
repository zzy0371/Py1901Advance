# print()
import os

# 1 导入模块
import logging
# 2 创建日志模块
loginLogger = logging.getLogger("loginregist")
# 2.1 设置等级
loginLogger.setLevel(logging.WARNING)

# 3 创建日志输出类型
fileHandler = logging.FileHandler('loginregist.txt',encoding='utf-8')
# 3.1 文件日志等级
fileHandler.setLevel(logging.DEBUG)
# 4 指定日志格式
fileformater = logging.Formatter('%(name)s-%(levelno)s-%(lineno)d-%(asctime)s-%(message)s')
# 5 将文件绑定日志格式
fileHandler.setFormatter(fileformater)

streamHanlder = logging.StreamHandler()
streamHanlder.setLevel(logging.DEBUG)
streamHanlder.setFormatter(fileformater)



# 6 将日志处理方法添加到日志工具
loginLogger.addHandler(fileHandler)
loginLogger.addHandler(streamHanlder)




loginLogger.debug("debug000")
loginLogger.info("info000")
loginLogger.warning("warning000")
loginLogger.error("error000")


def fun(x):
    x += 1
    return x

l1 = [1,2,3,4,5,6]
l2 = ['a','b','c']

result = map(fun, l1)
# print(type(result))
for r in result:
    print(r)

#     map  对象将列表进行映射形成map对象

def f1(x):
    if x%2 ==0:
        return True
    else:
        return False
result = filter(f1, l1)
for r in result:
    print(r)

# filter 过滤 第二个参数 ，使用第一个函数

from functools import reduce
from _functools import reduce
def sum1(x,y):
    return x-y

result = reduce(sum1,l1)
print(result)
# reduce  将序列中元素 相邻两个使用fun操作 结果和后续元素操作

import sys
import os
print(os.cpu_count())
# print(len(os.sched_getaffinity(0)))


# 1
# logging模块使用（只将error日志信息输出到文件，info以上信息输出到控制台）

# 2
# json 模块使用 （创建Good类：包含name，price类属性 ）
# 序列化：程序运行后输入 商品名，价格 生成实例，然后将实例存储在good.txt文件中
# 反序列化：程序运行后解析上述good.txt文件，生成Good实例  得到该实例的name 和price

# 3
# map  reduce
# filter函数使用：使用filter将列表中所有基数打印
import json

class Good():
    def __init__(self, _name, _price):
        self.name = _name
        self.price = _price

# with open("data.txt",'r') as f:
#     content = f.read()
#     print(content)
#     g = json.loads(content)
#     print(g,g["name"],g["price"])
import pickle
with open('data.txt', 'w') as f:
    name = input("输入名字")
    price = input("输入价格")
    g = Good(name,price)
    print(g.name,g.price)
    result = json.dumps(g.__dict__)
    # result = pickle.dumps(g)
    # f.write(str(result))


