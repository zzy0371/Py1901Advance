print(r"hello\nworld")
import re
result = re.findall("^hello", "hello world \nhello zhengzhou",re.M)
print(result)

result = re.findall("zhengzhou$", "hello worzhengzhou\nld hello zhengzhou",re.M)
print(result)

# \b表示回退一定要 使用原始语句 r
result = re.findall(r"\bhello\b", "helloworld hello zhengzhou sayhellook")
print(result)

# ^ 开头 包括字符串的原始开头  多行模式下 \n后面的内容
#  $结尾 包括字符串最后  \n前面内容
#  \b 代表单词边界（单词两遍都为空）  只能用于原始字符串  符号. \n等认为单词边界
# \bxxx\B 代表左边为单词边界 右边为非单词边界