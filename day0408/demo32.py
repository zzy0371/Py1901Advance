import os
from multiprocessing import Process
import time
# p1 进程入口函数
def p1process():
    time.sleep(4)
    print("进程p1执行了", os.getpid())
def p2process():
    while True:
        print("进程p2执行了", os.getpid())
        time.sleep(1)
def main():
    # 1创建进程， 创建Process类的实例
    # 2通过target指定进程入口函数
    p1 = Process(target=p1process,name="pp1")
    # 3开启进程
    p1.start()
    # p1.join()
    p2 = Process(target=p2process)
    p2.start()
    # print('p1 pid',p1.pid)

    print("p1进程名字",p1.name)
    # print("finish")

    time.sleep(2)
    # p1.terminate()
    # p2.terminate()

    while True:
        time.sleep(1)
        print(p1.is_alive(),p2.is_alive())
if __name__ == "__main__":
    data = 1
    print('main pid ',os.getpid()," pycharm pid", os.getppid())
    main()

"""
Process()生成进程实例
target指明进程入口函数
p1.pid 得到进程的pid
进程函数执行完毕进程执行完毕释放资源
主进程结束会结束开启的子进程
join()方法会阻塞进程（join方法在哪个进程写 就阻塞哪个进程）
terminate()会终止进程
isalive() 判断进程是否结束

"""