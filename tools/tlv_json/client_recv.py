import socket
import threading
import pickle
import json
from TLV import *
# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('localhost', 2333))

def read_from_server(s):
    try:
        data = pickle.loads(s.recv(2048))
        # test
        tlvp = TLVParser(data.buffer, t_ext=7, l_ext=7)
        for avp in tlvp.parse():
            print("%d(%d): %s" % (avp["type"], avp["length"], avp["value"]))
        # return s.recv(2048).decode('utf-8')
        text = json.loads(avp["value"])
        #count = count + 1
        #print("test count:")
        #print(count)
        print(text["username"])
        print(text["age"])
        return tlvp
    # 如果捕获到异常，则表明该socket对应的客户端已经关闭
    except:
        # 删除该socket
        socket_list.remove(s)   # ①

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
