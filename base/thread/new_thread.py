import threading
import time
import sys
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        #print("%s:%s" % (threadName, time.ctime(time.time()))

try:
    thread.start_new_thread(print_time)
except:
    print("Error:unable to start thread")
while 1:
	pass
