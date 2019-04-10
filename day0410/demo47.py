"""
网络编程：套接字编程，Socket编程
套接字：一套用于网络通信的API（一套类，方法）
"""
import socket
# print(socket)
# print(dir(socket))

# TCP通信
socketObj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 通过调用socketObj 特定方法完成进程通信

# bind方法用于TCP连接中将socket对象和IP PORT绑定
# socketObj.bind( ("127.0.0.1", 8888) )
# listen 开始监听客户端连接
# socketObj.listen()

# 阻塞方法   直到有客户端连接
# clientsoccket = socketObj.accept()

# 构造客户端socket
# socketclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接到tcp服务器
# socketclient.connect(("192.168.12.135",8888))

# recv,send TCP发送消息
# recvfrom sendto UDP收发消息

# clientsocket.close()
# UDP通信
# socketObj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



"""
UDP :发送数据之前只需要指明 发送给谁即可，不需要预先连接， 也不知道发送成功失败
TCP :发送数据之前需要建立连接  
知道发送成功或者发送失败， 发送失败会进行重发
在调用close之前 可以一直收发
"""