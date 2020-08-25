# ''' finding out different colors from image'''

import cv2
import numpy as np


def empty(a):
    pass


image = cv2.imread('resource/finger_exact.jpeg')
image = cv2.resize(image, (600, 600))
image = image[200:380, 100:500]
# cv2.imshow("framing", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 300)
cv2.createTrackbar('Hue min', "TrackBar", 0, 179, empty)
cv2.createTrackbar('Hue max', "TrackBar", 179, 179, empty)
cv2.createTrackbar('Sat min', "TrackBar", 0, 255, empty)
cv2.createTrackbar('Sat max', "TrackBar", 255, 255, empty)
cv2.createTrackbar('Val min', "TrackBar", 0, 255, empty)
cv2.createTrackbar('Val max', "TrackBar", 255, 255, empty)

vid = cv2.VideoCapture(1)
while True:
    _, frame = vid.read()
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_min, h_max = cv2.getTrackbarPos("Hue min", "TrackBar"), cv2.getTrackbarPos("Hue max", "TrackBar")
    s_min, s_max = cv2.getTrackbarPos("Sat min", "TrackBar"), cv2.getTrackbarPos("Sat max", "TrackBar")
    v_min, v_max = cv2.getTrackbarPos("Val min", "TrackBar"), cv2.getTrackbarPos("Val max", "TrackBar")
    lower, upper = np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max])

    masked = cv2.inRange(frame2, lower, upper)
    # print(masked)
    newimage = cv2.bitwise_and(frame2, frame2, mask=masked)
    cv2.imshow("window1", masked)
    cv2.imshow("window2", frame)
    # cv2.imshow("window2", newimage)
    cv2.waitKey(1)