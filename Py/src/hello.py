import cv2 as cv
import numpy as np

img = cv.imread('J.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
 
cv.imshow('j',erosion)
 
cv.waitKey(0)
cv.destroyAllWindows()

