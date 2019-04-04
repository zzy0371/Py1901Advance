import re
from collections.abc import Iterator
# 输入：字符串
# 输出：None， match对象 list
# pattern  匹配模式 匹配规则
# match 从开头匹配
# search 从任意位置开始匹配第一个
# fullmath 需要从开头匹配到结尾

# findall 返回所有匹配结果
# splite 分割字符串 第三个参数为分割次数 返回列表
# sub 替换子字符串  第一个参数匹配模式 第二个参数新内容  第三个参数目标字符串 第四个参数替换次数
# finditer 类似findall 但是返回为迭代器 迭代器中每一个对象为match类型


s1 = "hello worlld ll aaa allaah"
# result = re.match("hello", s1)
# result = re.search("llo", s1)
# result = re.fullmatch("he.*?h", s1)
# result = re.findall("ll", s1)
# result = re.split("h",s1)
# result = re.sub("ll","6666",s1,3)
result = re.finditer("ll",s1)

re.RegexFlag

# print(result, type(result), isinstance(result,str))
if result:
    if isinstance(result, re.Match):
        print("返回Match")
        g1 = result.group()
        print(g1)
    elif isinstance(result, Iterator):
        print("返回Iterator")
        for r in result:
            print(r.group())
    elif isinstance(result,list):
        print("返回list")
        for r in result:
            print(r)
    elif isinstance(result,str):
        print("返回str")
        print(result)
else:
    print("匹配结果为空")

result = re.findall("^abc","abcde\nabcd",re.M)
print(result)