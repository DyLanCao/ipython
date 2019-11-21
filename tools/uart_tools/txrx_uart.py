import serial
from time import sleep

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

    while True:
        data="hello world"
        print("write:"+ data)
        sleep(2)
        serial.write(data.encode("gbk")) #数据写回
        rx_data = recv(serial)
        if rx_data != b'':
            print(rx_data)

