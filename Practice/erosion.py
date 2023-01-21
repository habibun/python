import cv2
import numpy as np

# image erosion operation
image = cv2.imread('img.jpg', 0)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(image,kernel,iterations = 1)
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)