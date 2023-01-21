import cv2
import numpy as np

# image opening operation
image = cv2.imread('img.jpg', 0)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(0)