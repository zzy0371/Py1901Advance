import threading
import time

def thread1(pam1):
    while True:
        time.sleep(1)
        print('+',pam1,threading.currentThread().name,threading.currentThread().isAlive())


def main():
    for i in range(5):
        t1 = threading.Thread(target=thread1, args=(i,), name="MyThread"+str(i))
        t1.start()

if __name__ == "__main__":
    main()
    # while True:
    #     time.sleep(1)
    #     print(threading.enumerate())
    #     print('main',threading.currentThread())

"""
默认线程名字：主线程名字（MainThread）
子线程名字：Thread-n
enumerate()返回当前程序中所有线程（返回列表，只返回alive状态的线程）
threading.currentThread()返回当前线程
name 线程名
ident 线程标识
"""