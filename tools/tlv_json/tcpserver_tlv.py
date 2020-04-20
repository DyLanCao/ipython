# This example code is in the Public Domain (or CC0 licensed, at your option.)

# Unless required by applicable law or agreed to in writing, this
# software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.

# -*- coding: utf-8 -*-

import socket
import sys
from pytlv.TLV import *
import json
import time
# -----------  Config  ---------- 
IP_VERSION = 'IPv4'
PORT = 3333;
count = 1
# -------------------------------

if IP_VERSION == 'IPv4':
    family_addr = socket.AF_INET
elif IP_VERSION == 'IPv6':
    family_addr = socket.AF_INET6
else:
    print('IP_VERSION must be IPv4 or IPv6')
    sys.exit(1)


try:
    sock = socket.socket(family_addr, socket.SOCK_STREAM)
    print('Socket created')
except socket.error as msg:
    print('Error: ' + str(msg[0]) + ': ' + msg[1])
    sys.exit(1)

    
try:
    sock.bind(('', PORT))
    print('Socket binded')
    sock.listen(1)
    print('Socket listening')
    conn, addr = sock.accept()
    print('Connected by', addr)
except socket.error as msg:
    print('Error: ' + str(msg[0]) + ': ' + msg[1])
    sock.close()
    sys.exit(1)

while True:

    #data1 = {"ssid":"vision","password":"1234567890","server_addr":"rd.yymedic.com","server_port":3333,"dynamic_ip":1,"dns":""}
    #data1 = {"ssid":"vision","password":"1234567890","server_addr":"rd.yymedic.com","server_port":3333}
    data1 = {"ssid":"vision", "password":"1234567890"}
    jsondata = json.dumps(data1)
    if jsondata is None or jsondata == 'exit':
        break
    header = 'BIRD'
    #tlv = TLV([header, '9F04'])
       
    cmd = '09'
    reser = '00'
    #print(len(jsondata))
    frame_len = hex(len(jsondata) + len(cmd) + len(reser))
    str_len = str(frame_len[2:])
    print(frame_len)
    test = header + str_len + cmd + reser + jsondata
    #print(test)
    #print(len(test))
    #data = tlv.build({header: test})
    count +=1
    print("data send success num:",count)
    time.sleep(1)
    conn.send(test.encode('utf-8'))


    data = conn.recv(1024)
    if not data:
            print("recv is None")
            break
    data = data.decode("utf8","ignore")
    print('Received data: ' + data)
conn.close()
