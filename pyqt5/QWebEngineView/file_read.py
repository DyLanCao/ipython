# minimal QWebEngine example.
import os


path = os.getcwd()

basedir = os.path.abspath(os.path.dirname(__file__))

def file_testa():
    with open(path + '/test.txt') as file:
        css = file.readlines()
        print(" %s " % css)

def file_testb():
    with open(basedir + '/test.txt') as file:
        css = file.readlines()
        print(" %s " % css)

def file_test():
	print(basedir)
	print("hello test")

def main():
	print("hello world is ok")

if __name__ == '__main__':
    main()
    file_test()
    #file_testa()
    file_testb()

#if __main__ == '__main__':
#	file_test()

