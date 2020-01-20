
#通过queue
import time
import threading
from queue import Queue
def get_detail_html(queue):
    while True:
            queue.put("hello")
            print("get detail html started")
            time.sleep(3)
            print("get detail html end")
 
def get_detail_url(queue):
    while True:
        print("get detail url started")
        test = queue.get()
        time.sleep(1)
        print("get detail url end")
 
if __name__ == "__main__":
    url_queue = Queue(maxsize=1000)
    thread2 = threading.Thread(target=get_detail_url,args=(url_queue,))
    thread2.start()
    for i in range(2):
        thread1 = threading.Thread(target=get_detail_html,args=(url_queue,))
        thread1.start()
        #thread1.join()
    #thread1.setDaemon(True)
    #thread2.setDaemon(True)
    start_time = time.time()
 
 
 
    #thread2.join()

    print(time.time() - start_time)
