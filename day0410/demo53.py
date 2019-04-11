"""
TCP 客户端
"""
from socket import *
client = socket(AF_INET,SOCK_STREAM)
# 连接到服务端
client.connect(("192.168.12.135",8888))
inputstr = input("输入发送信息").encode("utf8")
client.send(inputstr)
print("发送成功")

while True:
    result = client.recv(1024)
    if len(result)>0:
        print(result)
    else:
        break
client.close()


# tread tsend

