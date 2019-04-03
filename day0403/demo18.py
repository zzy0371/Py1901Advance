# list1 = [1,2,3,[4,5]]
# list2 = list1
# # print(list2 is list1)
# # print(list2[3] is list1[3])
# list1.insert(3, 3.5)
# print(list1,list2)
#
# list2[4].insert(1,4.5)
# print(list1, list2)

"""
= 完全拷贝引用，内外层均拷贝引用
"""


# import copy
# list1 = [1,2,3,[4,5]]
# list2 = copy.copy(list1)
# # print(list1 is lis2)
# # print(list1[3] is lis2[3])
#
# # list1.insert(3,3.5)
# # print(list1, list2)
#
# list2[3].insert(1,4.5)
# print(list1, list2)

"""
浅拷贝 外层拷贝值 内层拷贝引用
"""

# import copy
# list1 = [1,2,3,[4,5]]
# list2 = copy.deepcopy(list1)
# # print(list1 is list2)
# # print(list2[3] is list1[3])
# list1.insert(3, 3.5)
# print(list1, list2)
#
# list2[3].insert(1, 4.5)
# print(list2, list1)

"""
深拷贝： 外层拷贝值，内层拷贝值
"""

