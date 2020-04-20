import socket
import threading
import pickle
import time
from pytlv.TLV import *
import json
# 定义保存所有socket的列表
socket_list = []
# 创建socket对象
ss = socket.socket()
# 将socket绑定到本机IP和端口
ss.bind(('localhost', 2333))
# 服务端开始监听来自客户端的连接
ss.listen()

data = {"username":"dylan","age":16}
jsondata = json.dumps(data)

def server_target(s):
    try:
        # 采用循环不断地从socket中读取客户端发送过来的数据
        while True:
            #line = input()
            data = {"username":"测试","age":16}
            jsondata = json.dumps(data)
            if jsondata is None or jsondata == 'exit':
                break
            tlv = TLV(['89ABCDEF', '9F04'])
            test = '1234567890'
            print(len(test))
            data = tlv.build({'89ABCDEF': test})
            print(data)
            time.sleep(2)
            #s.send('hello world'.encode('utf-8'))
            s.send(data.encode('utf-8'))
    except Exception:
        print(Exception.with_traceback())
while True:
    # 此行代码会阻塞，将一直等待别人的连接
    s, addr = ss.accept()
    #socket_list.append(s)
    # 每当客户端连接后启动一个线程为该客户端服务
    threading.Thread(target=server_target, args=(s, )).start()
