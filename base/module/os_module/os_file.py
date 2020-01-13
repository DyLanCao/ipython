import os
path = '/media/caoyin/work/igithub/ipython/base/module/os_module/test.txt'
for i in os.listdir(path):
        #print(i)
        if os.path.isfile(i):
            print(i)
            print("hello world")
        if os.path.isdir(i):
            print(i)
            print(" world")
