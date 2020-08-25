import cv2
import numpy as np


def empty(a):
    pass


image = cv2.imread('resource/lambo.jpg')
image = cv2.resize(image, (500, 300))
image2 = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# image = cv2.Canny(image, 100, 100)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 300)
cv2.createTrackbar('Hue min', "TrackBar", 1, 179, empty)
cv2.createTrackbar('Hue max', "TrackBar", 46, 179, empty)
cv2.createTrackbar('Sat min', "TrackBar", 64, 255, empty)
cv2.createTrackbar('Sat max', "TrackBar", 255, 255, empty)
cv2.createTrackbar('Val min', "TrackBar", 218, 255, empty)
cv2.createTrackbar('Val max', "TrackBar", 255, 255, empty)

cap = cv2.VideoCapture("opencv_tut/resources/video.mp4")
cap.set(cv2.CAP_PROP_FPS, 10)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)

# last = np.zeros((1000, 800, 3), dtype='uint8')
while True:
    # cap.set(cv2.CAP_PROP_FRAME_COUNT, 10)
    _, frame = cap.read()

    # print(cap.get(5))
    # frame = cv2.imread("resource/gaurav.jpg")
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_min, h_max = cv2.getTrackbarPos("Hue min", "TrackBar"), cv2.getTrackbarPos("Hue max", "TrackBar")
    s_min, s_max = cv2.getTrackbarPos("Sat min", "TrackBar"), cv2.getTrackbarPos("Sat max", "TrackBar")
    v_min, v_max = cv2.getTrackbarPos("Val min", "TrackBar"), cv2.getTrackbarPos("Val max", "TrackBar")
    lower, upper = np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max])
    masked = cv2.inRange(frame, lower, upper)
    # masked = cv2.inRange(image, lower, upper)
    # newimage = cv2.bitwise_and(image, image, mask=masked)
    cv2.imshow("window1", frame)
    cv2.imshow("masked", masked)
    # new_image = cv2.bitwise_and(image, masked)
    # print(image.shape, masked.shape)
    # newimage = cv2.bitwise_not(image2, newimage)
    # newimage = cv2.resize(newimage, (200, 100))

    # cv2.imshow("win2", newimage)
    # image2 = cv2.resize(image2, (1000, 800))
    # image2[0:200, 500:800] = newimage
    # cv2.imshow("new", image2)
    # cv2.
    # cv2.imshow("window5", extra)
    cv2.waitKey(50)
