#-*-coding:utf-8-*- 
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.max())
print(a.min())
print(a.max(axis=0))
print(a.max(axis=1))

print(a.argmax(axis=1)) #获取最大元素所在的位置

#获取平均值
print(a.mean())
print(a.mean(axis=0))
print(a.mean(axis=1))

#获取方差
#mean(abs(x - x.mean())**2)
print(a.var())

#获取标准差
#函数std() 相当于sqrt(mean(x - x.mean())**2)
print(a.std())
