#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

points = np.arange(-5,5,0.01)

xs,ys = np.meshgrid(points,points)

z = np.sqrt(xs**2 + ys**2)

#创建新的figure
fig = plt.figure()

#绘制2x2两行两列共四个图，编号从1开始
ax = fig.add_subplot(221)
ax.imshow(z)

ax = fig.add_subplot(222)
#使用自定义的colormap(灰度图)
ax.imshow(z,cmap=plt.cm.gray)

ax = fig.add_subplot(223)
#使用自定义的colormap
ax.imshow(z,cmap=plt.cm.cool)

ax = fig.add_subplot(224)
#使用自定义的colormap
ax.imshow(z,cmap=plt.cm.hot)

#图片的显示
plt.show()
