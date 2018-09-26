import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((320,240,3),dtype=np.uint8)

#img[0,0] = [255,0,0]      
#img[0,1] = [0,255,0]      
#img[1,0] = [0,0,255]      
#img[0,0] = [255,255,255]      
#img[0,1] = [255,255,255]      
#img[1,0] = [255,255,255]      
#img[1,1] = [255,255,255]      

for x in range(320):
	for y in range(240):
		img[x,y] = [y,y,y]


for x in range(320):
	for y in range(240):
		print(img[x,y])

plt.imshow(img)
plt.savefig("test1.jpg")
plt.show()
