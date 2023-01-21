import cv2
import numpy as np

# image closing operation
image = cv2.imread('img.jpg', 0)
kernel = np.ones((5,5), np.uint8)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)