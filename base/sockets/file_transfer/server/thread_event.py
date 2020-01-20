import threading
import datetime,time

class sockets_thread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name='thread' + threadname)
        self.threadname = int(threadname)

    def run(self):
        event.wait()
        print('子线程运行时间：%s'%datetime.datetime.now())

if __name__ == '__main__':
    event = threading.Event()
    t1 = sockets_thread('1')
    #启动子线程
    t1.start()
    print('主线程运行时间：%s'%datetime.datetime.now())
    time.sleep(2)
    # Flag设置成True
    event.set()
    time.sleep(2)
    # Flag设置成True
    event.set()
    t1.join()
