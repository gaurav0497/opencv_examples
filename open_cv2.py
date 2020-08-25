import cv2
import time
import os
import numpy as np
import matplotlib


# img = cv2.resize(img, (600, 600))
# stone = cv2.resize(img[350:450, 225:350], (200, 200))
# img = cv2.imread('opencv_tut/resources/experi.jpg', 1)
# cv2.imshow("preview", img)
# cv2.waitKey(0)
# hey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("preview", hey)
# cv2.waitKey(0)


w, h = 800, 800
image = np.zeros((w, h, 3), 'uint8')
cv2.circle(image, (400, 400), 380, (100, 105, 100), 2)
cv2.circle(image, (400, 400), 300, (0, 255, 0), 2)
cv2.circle(image, (400, 400), 200, (255, 0, 0), 2)
cv2.circle(image, (400, 400), 100, (0, 0, 255), 2)
cv2.circle(image, (400, 400), 50, (120, 255, 230), 2)
cv2.circle(image, (400, 400), 20, (60, 25, 70), 2)
cv2.circle(image, (400, 400), 7, (10, 155, 100), cv2.FILLED)


cv2.imshow("black", image)
cv2.waitKey(1000)



# Drawing pattern

# a = cv2.rectangle(image, (100, 100), (800, 800), (0, 0, 255), 2)
# cv2.imshow("black", a)
# cv2.waitKey(0)
#
#
# a = cv2.rectangle(image, (200, 200), (700, 700), (0, 255, 0), 2)
# cv2.imshow("black", a)
# cv2.waitKey(0)
#
# b = cv2.rectangle(image, (300, 300), (600, 600), (255, 255, 0), 2)
# cv2.imshow("black", b)
# cv2.waitKey(0)
#
# b = cv2.rectangle(image, (400, 400), (500, 500), (255, 255, 200), 2)
# cv2.imshow("black", b)
# cv2.waitKey(0)
#
# b = cv2.rectangle(image, (400, 400), (500, 500), (255, 255, 200), cv2.FILLED)
# cv2.imshow("black", b)
# cv2.waitKey(0)
#
# b = cv2.line(image, (300, 300), (400, 400), (255, 255, 0), 2)
# b = cv2.line(image, (500, 500), (600, 600), (255, 255, 0), 2)
# b = cv2.line(image, (400, 500), (300, 600), (255, 255, 0), 2)
# b = cv2.line(image, (500, 400), (600, 300), (255, 255, 0), 2)
# cv2.imshow("black", b)
# cv2.waitKey(0)
#
#
# b = cv2.line(image, (200, 200), (300, 300), (0, 255, 0), 2)
# b = cv2.line(image, (600, 600), (700, 700), (0, 255, 0), 2)
# b = cv2.line(image, (300, 600), (200, 700), (0, 255, 0), 2)
# b = cv2.line(image, (600, 300), (700, 200), (0, 255, 0), 2)
# cv2.imshow("black", b)
# cv2.waitKey(0)




if __name__ == '__main__':
    pass