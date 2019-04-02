"""
通过生成器节省内存
生成器特点：后续元素由前方元素确定
通过异常捕获 捕获生成器元素获取完毕
可以使用for循环或者next遍历生成器



"""
import sys
# list1 =[x for x in range(100000) ]
# print(sys.getsizeof(list1))
# print(list1[10])
# 通过生成器来实现节省内存

list2 = (x for x in range(100))
print(sys.getsizeof(list2))
# print(list2[10])
# print(type(list2))
# print(next(list2))
# print(next(list2))

# print(list2.__next__())

for g in list2:
    print(g)


# while True:
#     try:
#         print(next(list2))
#     except Exception as e:
#         print(e)
#         break
#
# print("end")

# list3 = (x for x in range(100))
# print(sys.getsizeof(list3))