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
        '''
        j = {
                "ssid":"vision","password":"12345678","server_addr":"www.baidu.com","server_port":3333,"state_get":1,"dns":"8.8.8.8","baud_rate":115200  
            }
            '''

        j = {
                "ssid":"vision","password":"13916953196","server_port":3000,"brate":115200,"dns":"8.8.8.8","server_addr":"192.168.43.205","socket":3, "state_get":1
            }
        data = json.dumps(j)
        
        print("write:"+ data)
        sleep(2)
        serial.write(data.encode("gbk")) #数据写回
        #sleep(1)
        rx_data = recv(serial)
        if rx_data != b'':
            print("read:" + str(rx_data))

