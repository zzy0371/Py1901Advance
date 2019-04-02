"""
时间消耗装饰器
"""
import time,datetime
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(time.time(), datetime.datetime.timestamp(datetime.datetime.now()))

def timecount(f):
    def tc():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__,'消耗',end-start)
    return tc


@timecount
def getfromlist():
    # start = time.time()
    list1 = [x for x in range(100000)]
    print(list1.index(99999))
    # end = time.time()
    # print(end-start)
@timecount
def getfromgeberator():
    g1 = (x for x in range(100000))
    index = 0
    while True:
        try:
            result = next(g1)
            if result == 99999:
                print(index)
                break
            index += 1
        except StopIteration as e:
            print('没有找到')



getfromlist()
getfromgeberator()
