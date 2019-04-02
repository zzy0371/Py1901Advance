# def fun():
#     yield 1
#     yield 2

# print(next(fun()))
# print(next(fun()))
# print(next(fun()))
# print(next(fun()))

# result = fun()
#
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


# 裴波拉契  裴波那契
# 从第三项开始每一项都为前两项的和
# 0  1  1   2   3  5  8   13 。。。。

def fun(num):
    a, b =0, 1
    yield a
    yield b

    count = 0
    while count<num:
        a, b = b, a+b
        yield b
        count+=1
result = fun(10)
for r in result:
    print(r)





