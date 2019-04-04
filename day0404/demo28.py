import re
result = re.findall(r"\bhello\b|\bhi\b", "hello world hi world")
print(result)

result = re.search("(.*?)o","hello world hi world")
print(result)
print(result.group(),"+++",result.group(1))

result = re.match(r"(hello).*?\1", "hello world hello china")
print(result.group(), result.group(1))

result = re.match(r"(?P<hname>hello).*?(?P=hname)", "hello world hello china")
print(result.group(),result.group(1),result.group("hname"))

"| 代表左右任意一个满足即可"
# result.group()代表取得整个匹配结果
# result.group(n)代表取得第n组
# \n 代表和前方第n个分组相同的模式  只能用于子字符串
# （?P<name> .*？）可以给分组起别名  引用之前的别名使用（?P=name）