"""
TCP多线程
"""
from socket import *
import threading
def tread(cs):
    while True:
        try:
            result = cs.recv(1024)
            if len(result) > 0:
                print(result)
            else:
                cs.close()
                break
        except Exception as e:
            print(e)

def tsend(cs):
    while True:
        try:
            if cs._closed:
                break
            else:
                # 当进入while循环还没断开链接
                # input阻塞之后断开链接
                inputstr = input("请输入发送信息").encode("utf8")
                if cs._closed:
                    break
                else:
                    cs.send(inputstr)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(("192.168.12.135", 8888))
        tr = threading.Thread(target=tread,args=(client,))
        tr.start()
        ts = threading.Thread(target=tsend,args=(client,))
        ts.start()
        tr.join()
        ts.join()
    except Exception as e:
        print(e)

    print("已经断开链接")

"""
开启两个线程分别负责收，发
"""
