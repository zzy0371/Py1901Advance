"""
由re.compile得到匹配模式（对象）
匹配模式对象拥有上述几个方法（findall， search等）
re.I 忽略大小写
re.M 多行模式  ^可以配到\n后内容     $可以匹配\n内容
re.S 单行：  . 可以匹配 \n

"""
import re
# 得到匹配模式
s1 = "helloworld\nhid\nHello world"
print(s1)
pat = re.compile(".d$",re.M)
# print(pat,type(pat))
# print(dir(pat))
# result = pat.findall(s1,0,7)
# print(result)
result = pat.findall(s1)
print(result)