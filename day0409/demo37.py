from multiprocessing import Process,Queue
import time

#获取任务进程，获取任务写入队列
def pwrite(taskqueue):
    # print(taskqueue.qsize())
    for r in range(10):
        time.sleep(2)
        taskqueue.put(r)
        # print(taskqueue.qsize())

def pdo(task):
    """
    真正执行任务的进程
    :param task:
    :return:
    """

# 读取任务进程 ，从队列读取任务
def pread(taskqueue):
    while True:
        # get取不到任务会阻塞读进程
        task = taskqueue.get()
        print("读取到任务",task)
        "取出来任务"
        "来一个任务开一个进程 "
        pdo = Process(target=pdo,args=(task,))
        pdo.start()


if __name__ == "__main__":
    # 1 定义任务队列
    taskQueue = Queue(10)
    pw = Process(target=pwrite,args=(taskQueue,))
    pw.start()
    print('写进程开启 pid',pw.pid)
    pr = Process(target=pread,args=(taskQueue,))
    pr.start()
    print('读进程开启 pid', pr.pid)
    pw.join()
    # pw.join()会阻塞后代码执行， 不会影响pr进程执行
    pr.join()
    print("finish")


"""
使用队列在进程间共享数据
"""