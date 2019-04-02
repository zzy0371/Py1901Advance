from collections.abc import Iterable,Iterator


class Goods():
    def __init__(self,_addr):
        self.addr = _addr
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # return self.addr[0]
        if self.index<len(self.addr):
            result = self.addr[self.index]
            self.index+=1
            return result
        else:
            # 遍历越界引发异常
            raise StopIteration("越界引发异常")

g = Goods(['anyang','xinxiang','hebi'])

print(g)

try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)

print('end')

print(isinstance(g,Iterator))