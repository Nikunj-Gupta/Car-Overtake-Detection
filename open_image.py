import cv2
import numpy as np

img = cv2.imread("cars4.jpeg")
res = cv2.resize(img,(750,500))

cv2.imshow("Image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
