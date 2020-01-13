#python3 example
from threading import Timer
import time

def print_val(cnt):
	print("cnt:%d new time: %s" % (cnt,time.ctime()))
	cnt += 1

	if cnt < 10:
		t = Timer(1, print_val,(cnt,))
		t.start()
	else:
		return

t = Timer(2.0, print_val,(1,))
t.start()
