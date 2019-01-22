import cv2

image = cv2.imread("cars1.jpg") 

print type(image)
cv2.imshow("image", image) 
