#python3 example
from threading import Timer
import time

count = 0
def print_timer():
	global t, count
	print("count:%d new time: %s" % (count,time.ctime()))
	count += 1

	if count < 10:
		t = Timer(1, print_timer)
		t.start()

t = Timer(1.0, print_timer)
t.start()
