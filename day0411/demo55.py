"""
TCP 服务端
"""
from socket import *
import time
import threading

def tread(cs):
    while True:
        result = cs.recv(1024)
        if len(result)>0:
            info =result.decode("gbk").split(":")
            to = info[0]
            message = info[1].encode("gbk")
            if to in userdict.keys():
                userdict[to].send(message)
            else:
                cs.send("对方已离线,你不能发送消息".encode("gbk"))

        else:
            userdict.pop(str(cs.getpeername()[1]))
            print("剩余客户端", len(userdict))
            break



def tlisten(s):
    # 接受连接
    while True:
        client, clientaddr = s.accept()
        # 将连接的用户存入用户字典
        userdict[str(clientaddr[1])] = client
        print(clientaddr, "连接上了", "用户列表", len(userdict))
        # 第二个线程用来接受client发来的消息
        tr = threading.Thread(target=tread,args=(client,))
        tr.start()

if __name__ == '__main__':
    try:
        userdict = {}

        # 构造服务端对象
        server = socket(AF_INET, SOCK_STREAM)
        # 绑定地址
        server.bind(("192.168.12.135", 8888))
        # 开启监听
        server.listen(10)
        print('开启监听')

        # 开启线程用于接受客户端连接
        tl = threading.Thread(target=tlisten,args=(server,))
        tl.start()



    except Exception as e:
        print(e)



"""
A 告诉 B 你好
服务端收到 A 发来 你好 给B 
找到B 
然后告诉 B  A发来你好
"""