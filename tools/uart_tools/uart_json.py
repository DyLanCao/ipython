import serial
from time import sleep
import json

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.2)
    return data

if __name__ == '__main__':
    serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)  #/dev/ttyUSB0
    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")
    
    number = 0

    while True:
        number = number + 1
        print("number is:" + str(number))
        j = {
                "ssid":"visoin","password":"12345678","server_addr":"www.baidu.com","server_port":"3333"    
            }

        data = json.dumps(j)

        print("write:"+ data)
        sleep(2)
        serial.write(data.encode("gbk")) #数据写回
        #sleep(1)
        #rx_data = recv(serial)
        #if rx_data != b'':
        #    print("read:" + str(rx_data))

