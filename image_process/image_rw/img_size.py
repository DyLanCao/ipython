#-*- encoding: utf-8 -*-

from PIL import Image
im = Image.open('test3.pgm')#返回一个Image对象
print('宽：%d,高：%d'%(im.size[0],im.size[1]))
print('width：%d height:%d'%(im.width,im.height))
