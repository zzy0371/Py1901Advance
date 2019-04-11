# 1 引入模块
from socket import *
# 2 构造socket对象
server = socket(AF_INET,SOCK_STREAM)
# 3 绑定地址
SERVERADDR = ("192.168.12.135",8888)
server.bind(SERVERADDR)
# 4 开始监听
server.listen()
print('开启监听')
# 5 接受连接
# accept方法为阻塞方法
client,clientaddr = server.accept()
print("连接",clientaddr)
# 6接受消息 指定接受哪个客户端信息
BUFFERSIZE = 1024
info = client.recv(BUFFERSIZE)
print(info.decode("utf8"),client.getpeername())
# 7发送消息 指定发送给那个客户端
inputstr = input("请输入发送信息").encode("utf8")
client.send(inputstr)
# 8关闭socket对象
client.close()
server.close()
