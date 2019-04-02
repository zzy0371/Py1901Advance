from collections.abc import Iterator,Iterable
# Iterator 迭代器： 可以使用next方法
# Iterable可迭代：可以使用for循环遍历
# 生成器既是可迭代，又是迭代器


dict1 = {"num":0, "age":20}
list1 = [1,2,3]
# print( next(list1))
# print(next(dict1))

# 判断 list1是否是迭代器
print(isinstance(list1,Iterator))
print(isinstance(list1,Iterable))


def fun():
    yield 1
    yield 2

print(isinstance( fun(), Iterable ))
print(isinstance( fun(), Iterator ))


# 使用iter 将 Iterable 变成 Iterator

list12itorlist = iter(list1)
print(next(list12itorlist), isinstance(list12itorlist, Iterator))

# iter 可以将 list dict set tuple str 装换为Iterator类型


