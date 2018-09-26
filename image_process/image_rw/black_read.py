#-*- encoding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#img = np.zeros((320,240,3),dtype=np.uint8)
img = plt.imread('test3.pgm')
#img[0,0] = [255,0,0]      
#img[0,1] = [0,255,0]      
#img[1,0] = [0,0,255]      
#img[0,0] = [255,255,255]      
#img[0,1] = [255,255,255]      
#img[1,0] = [255,255,255]      
#img[1,1] = [255,255,255]      
for x in range(240):
	for y in range(320):
		img[x,y] = x


for x in range(240):
	for y in range(320):
		print('x:%d y:%d img:%d' % (x,y,img[x,y]))

plt.imshow(img)
plt.savefig("test3a.png")
plt.show()
