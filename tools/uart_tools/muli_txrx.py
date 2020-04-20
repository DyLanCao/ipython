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
    
    number = 0

    while True:
        number = number + 1
        print("number is:" + str(number))
        if number == 1:
            data="ssid:vision"
        elif number == 2:
            data="passwd:12345678"
        elif number == 3:
            data="port:3333"
        elif number == 4:
            data="tcpip:1"
        elif number == 5:
            data = "ipv4:127.0.0.1"
        elif number == 6:
            data = "server_addr:www.baidu.com"
        elif number == 7:
            data = "state_get"
        else:
            data="mac_addr:11:22:33:44:55:66"

        print("write:"+ data)
        sleep(2)
        serial.write(data.encode("gbk")) #数据写回
        sleep(1)
        rx_data = recv(serial)
        if rx_data != b'':
            print("read:" + str(rx_data))

