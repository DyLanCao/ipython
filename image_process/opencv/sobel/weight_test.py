# coding=utf-8

import cv2

# 底板图案
bottom_pic = 'girl1.jpg'
# 上层图案
top_pic = 'girl2.jpg'

bottom = cv2.imread(bottom_pic)
top = cv2.imread(top_pic)

h, w, _ = bottom.shape

img2 = cv2.resize(top, (w,h), interpolation=cv2.INTER_AREA)

#alpha，beta，gamma可调
alpha = 0.7
beta = 1-alpha
gamma = 0

# 权重越大，透明度越低
overlapping = cv2.addWeighted(bottom, alpha, img2, beta, gamma)
#cv2.addWeighted(bottom, 0.5, img2, 0.5, 0)
#overlapping = cv2.addWeighted(bottom,0.8,top,0.2,0)
# 保存叠加后的图片
cv2.imwrite('overlap(8:2).jpg', overlapping)

cv2.namedWindow('newImage')
cv2.imshow('newImage',overlapping)
cv2.waitKey()
cv2.destroyAllWindows()
