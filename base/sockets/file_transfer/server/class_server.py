#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
建立TCP的基本流程
ss = socket() # 创建服务器套接字
ss.bind() # 套接字与地址绑定
ss.listen() # 监听连接
inf_loop: # 服务器无限循环
    cs = ss.accept() # 接受客户端连接
    comm_loop: # 通信循环
        cs.recv()/cs.send() # 对话（接收/发送）
    cs.close() # 关闭客户端套接字
ss.close() # 关闭服务器套接字#（可选）
"""
#!/usr/bin/env python

import os
from socket import *
from time import ctime
import time

HOST = ''  #对bind（）方法的标识，表示可以使用任何可用的地址
PORT = 21567  #设置端口
BUFSIZ = 1024  #设置缓存区的大小
ADDR = (HOST, PORT)

class SocketServer():
    def __init__(self):
        self.tcpSerSock = socket(AF_INET, SOCK_STREAM)  #定义了一个套接字
        self.tcpSerSock.bind(ADDR)  #绑定地址
        self.tcpSerSock.listen(5)     #规定传入连接请求的最大数，异步的时候适用
        self.state = False
        self.cnt = 0
    def file_recv(self,name):
        print("file recv:%s" % name)
        self.message = input(name)
        self.state = True

    def data_rect(self):
        while True:
            print('waiting for connection...')
            tcpCliSock, addr = self.tcpSerSock.accept()
            print ('...connected from:', addr)
            while True:
                if self.state == True:
                    message = self.message
                    self.state = False
                    data = bytes(message,'utf-8')
                    print("recv files:",data.decode("utf-8"))
                    if not data:
                        break
                    filename = data.decode("utf-8")
                    print(filename)
                    if os.path.exists(filename):
                        filesize = str(os.path.getsize(filename))
                        print("文件大小为：",filesize)
                        tcpCliSock.send(filesize.encode())
                        data = tcpCliSock.recv(BUFSIZ)   #挂起服务器发送，确保客户端单独收到文件大小数据，避免粘包
                        print("开始发送")
                        f = open(filename, "rb")
                        for line in f:
                            tcpCliSock.send(line)
                    else:
                        tcpCliSock.send("0001".encode())   #如果文件不存在，那么就返回该代码
                else:
                    self.cnt = self.cnt + 1
                    print("count:%d" % self.cnt)
                    time.sleep(1)
                    continue

        tcpSerSock.close()


if __name__ == '__main__':


    sock_server = SocketServer()   
    #sock_server.data_rect()

    while 1:
        time.sleep(2)
        sock_server.file_recv('test.txt')


