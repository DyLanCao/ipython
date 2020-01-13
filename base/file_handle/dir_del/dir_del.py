import os
import sys
import glob

def del_files(path):
    fileNames = glob.glob(path + r'/*')
    
    for fileName in fileNames:
        try:
            os.remove(fileName)
            print("remove file:%s" % fileNames)
        except:
            try:
                os.mkdir(fileName)
                print("mkdir file:%s " % fileName)
            except:
                print("del file:%s " % fileName)
                del_files(fileName)
                os.rmdir(fileName)


def del_file(path):
    lsdir = os.listdir(path)
    print(lsdir)
    if any(name.endswitch('.py') for name in lsdir):
        print("no txt in this dir")
    else:
        print("have txt and need to remove")

    for file in lsdir:
        try:
            c_path = os.path.join(path,file)
            os.remove(c_path)
            print("rm c path: %s " % c_path)
        except:
            del_file(path)
            os.rmdir(file)
            print("rm failed try again: %s " % c_path)


if __name__ == '__main__':
    BASE_PATH = os.getcwd()
    print("below is base path:\n %s" % BASE_PATH)
    tmp_path = os.path.join(BASE_PATH,'static/')
    print("below is tmp_path:\n %s" % tmp_path)
    #del_files(tmp_path)
    del_file(tmp_path)

