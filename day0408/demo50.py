import threading
def thread1():
    # 子进程 修改主进程变量
    global  num
    num = 2

if __name__ == "__main__":
    num = 1
    t1 = threading.Thread(target=thread1)
    t1.start()
    t1.join()

    print(num)
