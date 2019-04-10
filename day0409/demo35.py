import os
from multiprocessing import Pool
import time


def process(p):
    # time.sleep(2)
    # print('pid', os.getpid(), 'ppid', os.getppid(), '  p ', p)
    while True:
        time.sleep(1)
        print('pid', os.getpid(),'ppid',os.getppid(),'  p ',p)

if __name__ == "__main__":
    print(os.getpid())
    # while True:
    #     time.sleep(1)
    #     print("++",os.getpid(),os.getppid())
    # 1构造进程池，存放4个可用进程
    pool = Pool(4)
    # 2 使用异步方式从池子取出可用进程

    for p in range(20):
        pool.apply_async(process, args=(p,))

    # pool.apply_async(process)
    # pool.apply_async(process)
    # pool.apply_async(process)
    # pool.apply_async(process)
    # pool.apply_async(process)

    # pool.apply(process)
    # pool.apply(process)

    # 3 以后不再使用该进程池
    pool.close()
    # time.sleep(5)
    # print("进程开启5秒")
    # 进程池中所有进程全部执行完毕
    # pool.terminate()
    # 4进程池阻塞主进程
    pool.join()
    print("finish")

# applay_async 异步取进程，不会阻塞主进程
# applay 取进程会阻塞主进程


"""
构造进程池（初始化参数）
异步取：不会则主进程
同步去：阻塞主进程（第一个进程没有执行完毕，第二个进程不可用）
close()进程池不可用（进程正常运行）
join()阻塞主进程
terminate（）终止进程池中的所有进程
传参：类似Process进程类


"""

