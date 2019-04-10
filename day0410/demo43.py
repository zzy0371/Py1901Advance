"""
加锁
"""
import threading
import time
def thread1():
    lock1.acquire()
    # 使用延确保两个锁都已经加锁过
    time.sleep(1)
    # 一秒之后 锁2在线程2 已经加锁成功  此处需要等待线程2 释放锁资源才能加锁
    lock2.acquire()
    print('t1')
def thread2():
    lock2.acquire()
    time.sleep(2)
    # 一秒之后 锁1在线程1 已经加锁成功 此处需要等待线程1 释放锁资源才能加锁
    lock1.acquire()
    print('t2')

if __name__ == "__main__":
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    t1 = threading.Thread(target=thread1)
    t1.start()
    t2 = threading.Thread(target=thread2)
    t2.start()

    t1.join()
    t2.join()
    print("end")
    # print("init")
    # lock.acquire()
    # print("lock1")
    # lock.release()
    # lock.acquire()
    # print("lock2")