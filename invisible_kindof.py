import cv2
import numpy as np

# # adding effect
# newimage = cv2.imread("resource/gaurav.jpg")
# background = newimage.copy()
# cv2.GaussianBlur(newimage, (7, 7), 0.8)
# cv2.cvtColor(newimage, cv2.COLOR_BGR2HSV)
# lower, upper = np.array([10, 105, 149]), np.array([157, 255, 231])
# masked = cv2.inRange(newimage, lower, upper)
# masked1 = 255 - masked
# no = cv2.cvtColor(masked, cv2.COLOR_GRAY2BGR)
# op = cv2.bitwise_not(background, no)
# cv2.imshow("mask ", op)
# cv2.imshow("win", masked1)
background = cv2.imread("resource/extra.jpg")
add_img = cv2.imread("resource/gaurav.jpg")
# print(add_img[0:100, 0:100])
add_img[330:490, 100:258] = 241
cv2.GaussianBlur(add_img, (5, 5), 1.8)
add_img = cv2.resize(add_img, (330, 600))

background[200:800, 0:330] = background[200:800, 0:330] + add_img
cv2.imshow("window", background)

cv2.waitKey(0)
cv2.destroyAllWindows()