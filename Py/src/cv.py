import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# 用灰度模式加载图像
# img = cv.imread('./img/advance.jpeg', 0)
# 彩图
img = cv.imread('./img/advance.jpeg')

# 显示图像，opencv
# cv.imshow('image', img,)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 显示图像，matplotlib
plt.imshow(img)