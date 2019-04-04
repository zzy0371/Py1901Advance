import re

result = re.findall("hi*", "hi china hello chiiiiiina")
print(result)

result = re.findall("hi+", "hi china hello chiina")
print(result)

result = re.findall("hi?", "hhi china hello chiina")
print(result)

result = re.search("hi{2}", "hi china hello chiina")
print(result)

result = re.findall("hi{2,}", "hi china hello chiina")
print(result)

result = re.findall("hi{1,5}", "hi china hello chiiina")
print(result)


# *  >=0
# +  >=1
# ?  0/1
# {2}  =2
# {2,} >=2
# {m,n}   m>=x>=n
# 正则默认贪婪模式（最可能多匹配） ？尽可能少匹配


result = re.findall("he+?", "hhllo hee heeeee zzheee0")
print(result)
#结果为 ['hee', 'heeeee', 'heee']

result = re.findall("h.*? h", "hee heehee   heee zzheee0")
print(result)
#结果为 ['h', 'h', 'h']