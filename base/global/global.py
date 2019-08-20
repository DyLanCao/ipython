global val
val = 10

def test1():
	global val
	val = 5
	print('test1 global val:',val)

def test2():
	val = 8
	print('test2 global val:',val)
class Test():
	def __init__(self):
		#global val
		val = 5
		test1()
		test2()
	def connect(self):
		print("class in connect global val:",val)
		if 5 == val:
			print("global val is:",val)

if __name__=="__main__":
	Test().connect()

