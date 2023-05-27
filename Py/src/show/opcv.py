import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../../img/advance.jpeg')
# print('img_shape',img.shape)     #读取数据的形状
# print('img_size',img.size)       #读取数据的大小
# print('img_dtype',img.dtype)     #读取数据的编码格式
# print('img',img)                 #打印img数据
# print('img_type',type(img))      #读取img的数据类型

b, g, r = cv2.split(img)    #通道分离
print(img.shape[0])
print(img.shape[1])
print(img.shape[2])
print(img.shape[:2])
zeros = np.zeros(img.shape[:2],dtype='uint8')
merge_r = cv2.merge([r,zeros,zeros])
merge_g = cv2.merge([zeros,g,zeros])
merge_b = cv2.merge([zeros,zeros,b])

plt.subplot(231);plt.imshow(b)
# plt.subplot(232);plt.imshow(g)
# plt.subplot(233);plt.imshow(r)
# plt.subplot(234);plt.imshow(merge_r)
# plt.subplot(235);plt.imshow(merge_g)
# plt.subplot(236);plt.imshow(merge_b)
# plt.show()
#
# cv2.imshow('img',img)   #显示图片
# cv2.waitKey(0)
# cv2.destroyAllWindows()