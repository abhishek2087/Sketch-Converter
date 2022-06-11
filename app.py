# Importing OpenCV
import cv2

# Reading Image
img = cv2.imread('img.jpeg')

# Image Processing
grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted = cv2.bitwise_not(grayed)
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)

def blend(x, y):
    return cv2.divide(x, 255 - y, scale = 255)

final_result = blend(grayed, blurred)

# Output the Image
# cv2.imshow('Original Image', img)
# cv2.imshow('Grayed Image', grayed)
# cv2.imshow('Inverted Image', inverted)
# cv2.imshow('Blurred Image', blurred)
# cv2.imshow('Final Image', final_result)

cv2.waitKey(0)

#Saving the Image
cv2.imwrite('img_sketch.jpg', final_result)