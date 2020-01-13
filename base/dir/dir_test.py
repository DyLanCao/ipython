import sys
import os

path = os.getcwd()
path1 = os.path.join(path,"test.txt")

def dir_check():
    print("the pwd is:%s" % path)
    print("the full path is:%s" % path1)
    with open(path1) as file:
        css = file.readlines()
        print("%s" % css)

def print_dir():
    print("sys.path[0] = ", sys.path[0])
    print("__file__ = ", __file__)
    print("os.path.abspath(__file__) = ", os.path.abspath(__file__))
    print("os.path.realpath(__file__) = ", os.path.realpath(__file__))
if __name__ == '__main__':
    dir_check()
    print_dir()

