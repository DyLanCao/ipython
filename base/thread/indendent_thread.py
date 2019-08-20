# python3

import time
from threading import Thread

def thread_state(t, n):
	while n > 0:
			n -= 1
			time.sleep(5)
			if t.is_alive():
				print("thread is alive")
			else:
				print("thread is exited")
def countdown(n):
	while n > 0:
		print('T-minus',n)
		n -= 1
		time.sleep(5)
t = Thread(target=countdown, args=(100,))
t.start()
thread_state(t,13)



