"""
没有明确服务端客户端
只要指定接受者IP，PORT就可以发送消息
"""
# 引入模块
from socket import *
import threading

def tread(sc):
    while True:
        info,addr = sc.recvfrom(1024)
        print("收到",addr[1],"发来",info.decode("utf8"))

def twrite(sc):
    while True:
        port = int(input("请输入接受信息的用户"))
        info = input("请输入发送信息").encode("utf8")
        sc.sendto(info,("192.168.12.135",port))


if __name__ == '__main__':
    # 得到服务端socket
    serversocket = socket(AF_INET, SOCK_DGRAM)
    SERVERADDR = ("192.168.12.135", 50000)
    # 绑定地址 供客户端连接
    serversocket.bind(SERVERADDR)
    tr = threading.Thread(target=tread,args=(serversocket,))
    tr.start()
    tw = threading.Thread(target=twrite, args=(serversocket,))
    tw.start()
    tr.join()
    tw.join()


