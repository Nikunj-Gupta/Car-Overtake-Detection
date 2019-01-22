import cv2
import numpy

W = 39.37 # KNOWN_WIDTH

def distance(x1, y1, x2, y2, F):
	W = 39.37 # KNOWN_WIDTH
	P = abs(x2 - x1)
	D = ( F * W ) / P
	return D

image_loc = "cars4.jpeg"
img = cv2.imread(image_loc) # read an image

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

x1_cord = 76
y1_cord = 43
x2_cord = 649
y2_cord = 393

D = 39.37 # KNOWN_DISTANCE
P = (x2_cord)-(x1_cord)
F = ( P * D ) / W


#((90, 0), (439, 199))


x3_cord = 90
y3_cord = 0
x4_cord = 439
y4_cord = 199	

#((0, 0), (649, 419))


x3_cord = 0
y3_cord = 0
x4_cord = 649
y4_cord = 419	

dist = ( distance(x3_cord, y3_cord, x4_cord, y4_cord, F) / 12 )
print dist,
print " feet."

if (dist < 16):
	print "Unsafe"
else:
	print "Safe"
