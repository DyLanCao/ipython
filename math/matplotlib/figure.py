#coding=utf-8
import matplotlib.pyplot as plt

#创建新的figure
fig = plt.figure()

#必须通过add_subplot()创建一个或多个绘图
ax = fig.add_subplot(221)

#绘制2x2两行两列共四个图，编号从1开始
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

#图片的显示
plt.show()
