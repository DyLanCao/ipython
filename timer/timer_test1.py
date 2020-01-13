#python3 example
from threading import Timer
import time
import datetime


def hello_test():
	print("hello world")

now = datetime.datetime.now()
print(now)
t = Timer(2.0,hello_test) 
t.start()
