import threading
from socket import *

def send(sc,sendto):
    while True:
        info = input("输入发送内容").encode("utf8")
        sc.sendto(info,sendto)
def recv(sc,buffersize):
    while True:
        info,addr = sc.recvfrom(buffersize)
        print(info.decode("utf8"),addr)

if __name__ == '__main__':
    SEND_ADDR = ('127.0.0.1', 60000)
    BUFFERSIZE = 1024
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    clientSocket.sendto("".encode("utf8"),SEND_ADDR)
    t1 = threading.Thread(target=send,args=(clientSocket,SEND_ADDR))
    t1.start()
    t2 = threading.Thread(target=recv,args=(clientSocket,BUFFERSIZE))
    t2.start()
    t1.join()
    t2.join()
