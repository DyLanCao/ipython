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
    serial = serial.Serial('/dev/ttyUSB4', 115200, timeout=0.5)  #/dev/ttyUSB0
    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")
    
    number = 0

    while True:
        #data="this is data send from uart to network......................."
        #data=0x555555555555555555555555555555555
        number = number + 1
        #print("write:"+ data)
        #sleep(2)
        #serial.write(data.encode("gbk")) #数据写回
        sleep(0.02)
        rx_data = recv(serial).hex()
        if rx_data != b'':
            print("read:" + rx_data)

