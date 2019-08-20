import os,sys

full_path = os.getcwd()

if not os.path.exists(full_path):
	print("path not exist")
else:
	print("full_path:{0}".format(full_path))

