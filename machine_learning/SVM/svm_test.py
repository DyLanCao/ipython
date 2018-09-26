#-*- coding:utf-8 -*-
import numpy as np
from numpy import *
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 指定核函数
def KerFunction(X,k,xi,ker):   # 输入：训练集，第 k 个样本，速度参数、核函数类型
    m,n = shape(X)
    K = mat(zeros((m,1)))
    if ker=="Lin":
        K = X*X[k].T
    elif ker=="Rbf":
        for i in range(m):
            deta = abs(X[i] - X[k])
            K[i] = deta*deta.T
        K = exp(K/(-1*2*xi**2))
        return K
    else:
        "没有所指定的和函数，请输入Lin 或者Rbf"
    return K


class SVM:
    def __init__(self,dataX,labelY,C,toler,maxIter,xi,ker):          # 输入：训练样本、标签、惩罚参数、容错率、最大迭代次数、速度参数、选择的核函数类型
        self.X = dataX
        self.Y = labelY
        self.m = shape(dataX)[0]
        self.n = shape(dataX)[1]
        self.b = 0
        self.C = C
        self.toler = toler
        self.maxIter = maxIter
        self.xi = xi
        self.Ker = ker
        self.cError = mat(zeros((self.m,2)))
        self.alpha = mat(zeros((self.m,1)))
        self.K = mat(zeros((self.m, self.m)))
        for i in range(self.m):
            self.K[:,i] = KerFunction(self.X,i,self.xi,self.Ker)


    # 随机选择一个alpha
    def selectRnad(self,i):   
        j = i
        while(j==i):
            j =  int(random.uniform(0,self.m))
        return j

    # 计算预测值与实际值的误差
    def claError(self,i):     # 注意：这里 alpha 与 Y 是对应元素相乘，不是矩阵相乘
        Fxi = float(multiply(self.alpha,self.Y).T*self.K[:,i]) + self.b
        Error = Fxi - float(self.Y[i])
        return Error

    # 输入：i (表示选择的第1个alpha值的下标)； 输出：j,Ej (第二个alpha 值的下表，和预测误差)
    #实现方法：Ej 找出与第i 个预测误差 差值最大的样本
    def selectJ(self,i):
        maxDeta = -1; maxK = 0;maxError = 0             # 3个变量分别用于：存储 abs(Ei - Ek) 的最大值，返回的j, j 的预测误差
        Ei = self.claError(i)
        self.cError[i] = [1, Ei]
        validError = nonzero(self.cError[:0].A)[0]            # 返回第一列所有非零元素的下标
        if len(validError)>1:
            for k in validError:
                if Ei == self.cError[k,1]:
                    continue
                else:
                    Ek = self.claError(k)
                    deta = abs(Ei - Ek)
                    if(deta>maxDeta):
                        maxDeta = deta; maxK = k;maxError = Ek
            return maxK,maxError
        else:                   # 当误差列表中均为0 时，随机选择一个alpha
            j = self.selectRnad(i)
            Ej = self.claError(j)
            return j,Ej

    # 对保存误差的矩阵进行更新
    def updataErrMat(self,i):
        Ei = self.claError(i)
        self.cError[i] = [1,Ei]

    # 数值剪切
    def ClipA(self,i,H,L):
        if self.alpha[i]>H:
            self.alpha[i] = H
        if self.alpha[i] <L:
            self.alpha[i]=L


    # 内循环:  # 输入为选择的第一个 alpha 值，函数功能：对alpha、b  值进行更新
    def innerCir(self,i):
        Ei = self.claError(i)
        if ((self.Y[i]*Ei<-1*self.toler and self.alpha[i]<self.C))or ((self.Y[i]*Ei >self.toler and self.alpha[i]>0)):    #判断是否违反KKT条件
            j,Ej =self.selectJ(i)
            alphaIold = self.alpha[i].copy(); alphaJold = self.alpha[j].copy()
            if (self.Y[i]!=self.Y[j]):
                L = max(0, alphaJold - alphaIold); H = min(self.C, self.C + alphaJold - alphaIold)
            else:
                L = max(0, alphaJold + alphaIold - self.C); H = min(self.C, alphaJold + alphaIold)
            if L==H: return 0
            eta = 2 * self.K[i, j] - self.K[i, i] - self.K[j, j]
            if eta >= 0: return 0
            self.alpha[j] += self.Y[j] * (Ej - Ei) / eta
            self.ClipA(j,H,L)         # 经过剪切，计算出更新后的 alphaJ
            self.claError(j)
            if (abs(self.alpha[j] - alphaJold) < 0.0001): return 0
            self.alpha[i] = alphaIold + self.Y[i]*self.Y[j]*(alphaJold - self.alpha[j])
            self.claError(i)
            b1 = self.b - Ei - self.Y[i]*self.K[i,i]*(self.alpha[i] - alphaIold) - self.Y[j]*self.K[i,j]*(self.alpha[j] - alphaJold)
            b2 = self.b - Ej - self.Y[j]*self.K[j,j]*(self.alpha[j] - alphaJold) - self.Y[i]*self.K[j,i]*(self.alpha[i] - alphaIold)
            if (self.alpha[i] < self.C and self.alpha[i] > 0):
                self.b = b1
            elif(self.alpha[j] < self.C and self.alpha[j] > 0):
                self.b = b2
            else:
                self.b = float(b1+b2)/2.0
            return 1
        else:
            return 0

    # 外层循环
    # 主要难点：退出循环的几个条件
    def OutCir(self):
        alphaChanged = 0
        EntirSet = True
        iter = 0
        while(iter<self.maxIter )and ((alphaChanged>0) or EntirSet):
            alphaChanged = 0
            if EntirSet:                               # 第一次计算时，所有的 alpha 都是0，遍历所有的样本点
                for i in range(self.m):
                    alphaChanged += self.innerCir(i)
                iter += 1
            else:       # 遍历非边界点
                nonBoundIs = nonzero((self.alpha.A > 0) * (self.alpha.A < self.C))[0]     #返回取值范围在 0 和 C 之间的数值的下标签
                for i in nonBoundIs:
                    alphaChanged += self.innerCir(i)
                iter += 1
            if EntirSet:
                EntirSet = False
            elif(alphaChanged==0):           # 当所有的 alpha 不在更新时，保证再遍历一次所有的样本点
                EntirSet = True

    def calcuWB(self):        # 计算 w
        self.OutCir()
        w = mat(zeros((1,self.n)))
        for i in range(self.m):
            w += multiply(self.alpha[i]*self.Y[i],self.X[i])
        return w,self.b

    def Predect(self,inX):   # 预测，输入样本数据集
        self.OutCir()
        w,b = self.calcuWB()
        m,n = shape(inX)
        if(n!=self.n):
            print "input sample is wrong"
            return 0
        label = []
        for i in range(m):
            if w*inX[i].T + b <= 0:
                label.append(-1)
            else:
                label.append(1)
        # print"b=\n",b
        # print"w=\n",w
        return label
def Correct_Rate(Label,PredectLabel):
    m = shape(Label)[0]
    k = 0
    for i in range(m):
        if(Label[i]==PredectLabel[i]):
            k += 1
    return float(k/m)


if __name__=="__main__":
    print "hello world"
    data = pd.read_csv("testSet.txt",delimiter='\t',header=None)
    m,n = shape(data)
    dataX = mat(data[range(n-1)])
    labelY =mat(data[n-1]).T
    print "m= \n",m
    print "n= \n",n
    print "dataX= \n",dataX
    print "labelY= \n",labelY
    trainX,testX,trainY,textY = train_test_split(dataX,labelY,train_size=0.7,random_state=1)
    C = 0.6;maxIter = 100;toler = 0.001;xi = 0.3;ker = "Lin"  # Lin线性，Rbf径向基核函数 
    svm = SVM(trainX, trainY, C, toler, maxIter, xi, ker)
    # 计算 w 和 b
    w,b = svm.calcuWB()
    print"b= \n",b
    print"w=\n",w

    # 对训练集测试
    trainLabel = svm.Predect(trainX)
    trainRate = Correct_Rate(trainY, trainLabel)
    print"训练集正确率：",trainRate
    # 对测试集测试
    textLabel = svm.Predect(testX)
    textRate= Correct_Rate(textY,textLabel)
    print "测试集正确率是：", textRate
