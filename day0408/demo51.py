import threading
import time

def thread():
    for r in range(1000000):
        global num
        lock.acquire()
        num += 1
        lock.release()

if __name__ == "__main__":
    # 用来加锁num
    lock = threading.Lock()

    num = 0
    t1 = threading.Thread(target=thread)
    t1.start()


    t2 = threading.Thread(target=thread)
    t2.start()

    t1.join()
    t2.join()
    print(num)

"""
num = 0
线程1 获取num =0 
线程2 获取num =0

线程1 num+=1   num = 1
线程1 num+=1   num = 2
线程1 num+=1   num = 3
线程2 num+=1   num = 1


"""

"""
针对指定的资源加锁
如果成功 ，可以修改
如果不成功 ， 陷入等待 直到加锁成功（上一个锁释放）
lock = thread.Lock() 构造锁
lock.acquire()
a= 1
b= 2

lock.release()

线程1 acquire成功 num +=1 release 
线程1 acquire成功 num +=1 release 
线程1 acquire成功 num +=1 release 
线程1 acquire成功 num +=1 release 
线程2 wait
线程2 wait
线程2 wait
线程2 wait
线程2 acquire成功 num +=1 release 






"""