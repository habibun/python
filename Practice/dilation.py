import cv2
import numpy as np

# image dilation operation
image = cv2.imread('img.jpg', 0)
kernel = np.ones((5,5), np.uint8)
image_dilation = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Dilation', image_dilation)
cv2.waitKey(0)
