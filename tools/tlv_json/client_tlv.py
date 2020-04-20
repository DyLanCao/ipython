import socket
import threading
import pickle
import json
from pytlv.TLV import *

# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('localhost', 2333))
tlv = TLV(['89ABCDEF', '9F04'])

def read_from_server(s):
    try:
        data = s.recv(2048)
        # test
        text = tlv.parse(data.decode('utf-8'))
        print(text)
        #print(data)

        #text = json.loads(avp["value"])
        #print(text["username"])
        #print(text["age"])
        return text
        #return data
    # 如果捕获到异常，则表明该socket对应的客户端已经关闭
    except:
        print(Exception.with_traceback())

def read_server(s):
    try:
        while True:
                contend = read_from_server(s)
                if contend is None:
                        break

    except:
        print(Exception.with_traceback())

# 客户端启动线程不断地读取来自服务器的数据
threading.Thread(target=read_server, args=(s, )).start()   # ①
