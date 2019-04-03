"""
通过sys   getrefcount(obj)

"""
from sys import getrefcount
print(getrefcount("hello"))
a = "hello"
print(getrefcount("hello"))
b = "hello"
print(getrefcount("hello"))
c = b
print(getrefcount("hello"))

def fun(pama):
    # print(getrefcount("hello"))
    print(pama)

fun(c)

c = "world"

del a
del b
print(getrefcount("hello"))

# print(getrefcount("a"))

print("----------------------")
list1 = [1,2,3]
list2 = [4,5,6]

print(getrefcount(list1))
print(getrefcount(list2))

list1.append(list2)
list2.append(list1)
# print(list1, list2)
# print(getrefcount(list1))
# print(getrefcount(list2))
# list1[3]

print(list2)
print(getrefcount(list1), getrefcount(list2))

del list1
# del list2
# print(list2[3])
del list2

"""
原始存储[1,2,3]内存块A      [4,5,6]存储在内存块B     内存引用计数1
list1  = 内存A     内存A +1  =》2
list2  = 内存B     内存B +1  =》2

循环引用导致内存A+1 =》3   内存B +1=》3
del list1    内存A -1 =》2
del list2    内存B -1  =》 2

内存A 和内存B 比原始状态 引用计数+1


第一个缺点：维护所有内存的引用计数 消耗资源
第二个缺点：当循环引用时导致内存泄露
 """



"""
内存A  付给list1  内存A引用 1
内存B  付给list2  内存B引用 1
内存C  付给list3/list4  内存C 引用2
内存D  付给list6    内存D引用1


list1 、list2 循环引用 内存A、内存B引用计数2

list3 、list6 循环引用 内存C引用计数3、内存D引用计数2



del list1  内存A引用 1
del list2  内存B引用 1
del list3  内存C引用 2
del list6  内存D引用 1

此时引用计数出现问题 永远不能被回收 泄露

第一步 ：将删除的对象的引用计数都减1 
内存A 引用 0
内存B 引用 0
内存C 引用 1
内存D 引用 0
将内存引用计数为0 对象加入死亡容器  （A，B，D都在死亡容器）
将内存引用计数不为0 对象加入存活容器  （C在存活容器）
第二步：遍历存活容器 如果引用到了死亡容器对象 将该引用对象移入存活容器 （D移入存活容器）
第三步：删除内存A 内存B  恢复C 恢复D



"""



