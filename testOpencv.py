import numpy as np
import cv2
np.set_printoptions(threshold=np.nan)

img = cv2.imread('pp.png')
# cv2.cvtColor()

print(img[1,1:])

cv2.imshow('images', img[:,:,1])
cv2.waitKey(1)