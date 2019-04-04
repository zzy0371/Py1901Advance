import re
result = re.findall("...", "hello")
# "." 不可以匹配换行符
print(result)

result = re.findall("[^0-3].ello", "0hello 1hello 2 ello 88ello 888ello")
print(result)

result = re.findall("\d\dhello", "55hello 1hello 5hello 0hello")
print(result)

result = re.findall("\Dhello", "xhello 1hello 5hello  hello")
print(result)

result = re.findall("\s\shello", "hello hello     hello")
print(result)

result = re.findall("\S\shello", "1hello s hello    1\thello")
print(result)

result = re.findall("\Wello", "hello aello5ello_ello .ello ^ello")
print(result)


#  . 可以匹配任意字符（\n 需要有re.S 支持）
# [] 可以匹配[]出现的任意字符  可以使用范围0-9   a-z  A-Z
#  [^0-5] == [6789]
# \d  一个数字
# \D  一个非数字
# \w  一个字符（字母 数字 _）
# \W 一个非字符
# \s 匹配 空格 tab
# \S 匹配 非空格 非tab



# print("hello world\nhi\tworld")
