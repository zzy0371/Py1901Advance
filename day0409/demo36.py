"""
进程之间使用队列共享数据
"""
from multiprocessing import Queue
# 初始化队列
queue = Queue(5)
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
# 阻塞5秒


try:
    # queue.put(6, block=False)
    queue.put_nowait(6)
except:
    print('error')

first = queue.get()
first = queue.get()
first = queue.get()
first = queue.get()
first = queue.get()
print(first)

try:
    # first = queue.get(block=False)
    first = queue.get_nowait()
    print(first)
except:
    print('get error')
print(queue.empty())
print(queue.full())

"""
Queue(n)初始化队列
get（） 阻塞取，取不出来一直等待
put（）阻塞方法，放不进去等待


"""