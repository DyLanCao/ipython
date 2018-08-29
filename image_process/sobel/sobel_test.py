# coding=utf-8

import Image
import numpy as np
import matplotlib.pyplot as pyplot
import pylab
im =Image.open('Bikesgray.jpg')
w,h = im.size
res = np.zeros((w, h))
sobel_x =[[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]]
sobel_y =[[-1, -2, 1],[0, 0, 0],[1, 2, -1]]
for x in range(1, (w-1)):#注意初始值问题，是从第二个开始的
    for y in range(1, (h-1)):
        sub =[[im.getpixel((x-1, y-1)), im.getpixel((x-1, y)), im.getpixel((x-1, y+1))],\
        [im.getpixel((x, y-1)), im.getpixel((x, y)), im.getpixel((x, y+1))], \
        [im.getpixel((x+1, y-1)), im.getpixel((x+1, y)), im.getpixel((x+1, y+1))]]
        sub = np.array(sub)
        roberts_x = np.array(sobel_x)
        roberts_y = np.array(sobel_y)
        var_x =sum(sum(sub * sobel_x))
        var_y = sum(sum(sub * sobel_y))

        #var = max(abs(var_x),abs(var_y))备注1
        var = abs(var_x) + abs(var_y)

        res[x][y] = var#把var值放在x行y列位置上



pyplot.imshow(res, cmap=pyplot.cm.gray)#输出图片可能颜色有问题，用cmap=pyplot.cm.gray进行改颜色
pylab.show()
