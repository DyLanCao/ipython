# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:58:03 2018

@author: zhupc
"""
import numpy as np
import h5py 

def loadDataSet():
    '''
    加载图片数据集
    '''
    pictureSet=[];pictureClasses=[]
    with h5py.File('bdata/Land.h5') as h5f:
        forest=h5f['forest'][:]
        urban=h5f['urban'][:]
        pictureSet=np.vstack((forest,urban))
        pictureClasses=[0]*50+[1]*50
    return pictureSet,pictureClasses
def createVocabList(pictureSet):
    '''
    创建一个词袋集合
    '''
    vocabSet=set([])
    for picture in pictureSet:
        vocabSet=vocabSet|set(picture)
    return list(vocabSet)


def randomSpillPictureSet(pictureSet):
    '''
    随机划分训练集与测试集
    '''
    trainingSet=[x for x in range(100)];testSet=[];
    for i in range(20):
        randIndex=int(np.random.uniform(0,len(trainingSet)))   
        testSet.append(trainingSet[randIndex])
        trainingSet.remove(trainingSet[randIndex])
    return trainingSet,testSet
def setOfPix2Vec(vocaList,inputSet):
    '''
    把像素转化为向量
    '''
    returnVec=[0]*len(vocaList)
    for pix in  inputSet:
        if pix in vocaList:
            returnVec[vocaList.index(pix)]=1
    return returnVec

def NBFit(trainMatrix,trainCategory):
    numTrainPictures=len(trainMatrix)
    numPix=len(trainMatrix[0])
    pUrban=sum(trainCategory)/float(numTrainPictures)#城市概率 p(城市)
    #拉普拉斯平滑
    pForestNum=np.ones(numPix);pUrbanNum=np.ones(numPix)
    pFDenom=2;pUDenom=2
    for i in range(numTrainPictures):
        if trainCategory[i]==0:
            pForestNum+=trainMatrix[i]
            pFDenom+=sum(trainMatrix[i])
        else:
            pUrbanNum+=trainMatrix[i]
            pUDenom+=sum(trainMatrix[i])
    pFVect=np.log(pForestNum/pFDenom)
    pUVect=np.log(pUrbanNum/pFDenom)
    return pFVect,pUVect,pUrban

def classifyNB(vecPicture,pFVec,pUVec,pUrban):
    '''
    利用朴素贝叶斯进行分类
    '''
    pF=sum(vecPicture*pFVec)+np.log(1-pUrban)
    pU=sum(vecPicture*pUVec)+np.log(pUrban)
    return 1 if pU/pF>1  else 0

def testingNB():
     pictureSet,pictureClasses=loadDataSet()
     vocabList=createVocabList(pictureSet)
     trainMat=[];trainClasses=[]
     trainingSet,testSet=randomSpillPictureSet(pictureSet)
     #for i in trainingSet:
     #    trainMat.append(setOfPix2Vec(vocabList,pictureSet[i]))
     #    trainClasses.append(pictureClasses[i])
     #pFVect,pUVect,pUrban=NBFit(trainMat,trainClasses)
     errorCount=0
     for i in testSet:
        picVector=setOfPix2Vec(vocabList,pictureSet[i])
        if classifyNB(np.array(picVector),pFVect,pUVect,pUrban)!=pictureClasses[i]:
            errorCount+=1
            print('classification error')
        else:print('分类正确')
     print('the error rate is :',float(errorCount)/len(testSet))
testingNB()


