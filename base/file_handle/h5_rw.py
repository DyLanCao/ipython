# -*- coding: utf-8 -*-

import h5py
import numpy as np

#HDF5的写入：
imgData = np.zeros((2,10))
f = h5py.File('Land.h5','w')   #创建一个h5文件，文件指针是f
f['forest'] = imgData                 #将数据写入文件的主键data下面
f['labels'] = np.array([1,2,3,4,5,6,7,8,9,10])            #将数据写入文件的主键labels下面
f['urban'] = imgData                 #将数据写入文件的主键data下面
f['labels'] = np.array([1,2,3,4,5,6,7,8,9,10])            #将数据写入文件的主键labels下面
f.close()                           #关闭文件

def loadDataSet():
    '''
    加载图片数据集
    '''
    pictureSet=[];pictureClasses=[]
    with h5py.File('Land.h5') as h5f:
        forest=h5f['forest'][:]
        #urban=h5f['urban'][:]
        #pictureSet=np.vstack((forest,urban))
        pictureClasses=[0]*50+[1]*50
    return pictureSet,pictureClasses

loadDataSet()


"""
imgData = np.zeros((2,4))
f = h5py.File('Land.h5','w')   #创建一个h5文件，文件指针是f
f['urban'] = imgData                 #将数据写入文件的主键data下面
f['labels'] = np.array([10,12,13,14,15,16,17,18,19,20])            #将数据写入文件的主键labels下面
f.close()

#HDF5的读取：
f = h5py.File('HDF5_FILE.h5','r')   #打开h5文件
# 可以查看所有的主键
for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
    print(f[key].value)

"""
