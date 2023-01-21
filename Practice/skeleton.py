import cv2
import numpy as np

# image skeleton operation
image = cv2.imread('img.jpg', 0)
ret, image = cv2.threshold(image, 127, 255, 0)
s = np.size(image)
skeleton = np.zeros(image.shape, np.uint8)
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

while True:
    open = cv2.morphologyEx(image, cv2.MORPH_OPEN, element)
    temp_cal = cv2.subtract(image, open)
    ero = cv2.erode(image, element)
    skeleton = cv2.bitwise_or(skeleton, temp_cal)
    image = ero.copy()
    if(cv2.countNonZero(image)) == 0:
        break
cv2.imshow('image skeleton', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()