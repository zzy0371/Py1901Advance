"""
线程基本
"""
import os
from threading import Thread
import time
def prt():
    print('++')
    time.sleep(1)


def timecount(f):
    def fun():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__,"消耗", end-start)
    return fun

@timecount
def main():
    for i in range(5):
        prt()

@timecount
def multithreadmain():
    # 主线程只负责创建5个子线程 之后马上结束
    listthread = []
    for r in range(5):
        t1 = Thread(target=prt)
        t1.start()
        listthread.append(t1)

    for t in listthread:
        t.join()



if __name__ == "__main__":
    # main()
    multithreadmain()
    # while True:
    #     time.sleep(3)
    #     print('++')

"""
使用Thread构造线程实例 
通过target传入线程的入口函数
通过start方法开启线程
t.join()可以阻塞线程
主线程结束，子线程结束（可以使用join等待子线程执行结束在结束主线程）
"""
