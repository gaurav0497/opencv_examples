import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 300)
cv2.createTrackbar('Hue min', "TrackBar", 11, 179, empty)
cv2.createTrackbar('Hue max', "TrackBar", 100, 179, empty)
cv2.createTrackbar('Sat min', "TrackBar", 68, 255, empty)
cv2.createTrackbar('Sat max', "TrackBar", 242, 255, empty)
cv2.createTrackbar('Val min', "TrackBar", 216, 255, empty)
cv2.createTrackbar('Val max', "TrackBar", 255, 255, empty)
cv2.createTrackbar("Threshold1", "TrackBar", 133, 400, empty)
cv2.createTrackbar("Threshold2", "TrackBar", 146, 400, empty)
cap = cv2.VideoCapture(0)


def findContor(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10000:
           # new = cv2.drawContours(image, cnt, 1, (255, 0, 0), 3)
           peri = cv2.arcLength(cnt, True)
           approx = cv2.approxPolyDP(cnt, 0.2 * peri, True)
           x, y, w, h = cv2.boundingRect(approx)
           # print("hello")
        # return x, y, w, h
           cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame2 = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny_img = cv2.Canny(frame, cv2.getTrackbarPos("Threshold1", "TrackBar"), cv2.getTrackbarPos("Threshold2", "TrackBar"), 2)
    masking = cv2.dilate(canny_img, (3, 3), iterations=2)

    h_min, h_max = cv2.getTrackbarPos("Hue min", "TrackBar"), cv2.getTrackbarPos("Hue max", "TrackBar")
    s_min, s_max = cv2.getTrackbarPos("Sat min", "TrackBar"), cv2.getTrackbarPos("Sat max", "TrackBar")
    v_min, v_max = cv2.getTrackbarPos("Val min", "TrackBar"), cv2.getTrackbarPos("Val max", "TrackBar")
    lower, upper = np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max])
    masked = cv2.inRange(frame, lowerb=lower, upperb=upper)
    newimage = cv2.bitwise_and(frame2, frame2, mask=masked)
    newimage = cv2.bitwise_and(newimage, frame2, mask=masked)
    next_lev = cv2.subtract(frame2, newimage)
    # x, y, w, h = findContor(masked)
    # print(x, y)
    # findContor(masked)
    # new = cv2.rectangle(masked, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # cv2.imshow("window1", frame2)
    cv2.imshow("window2", newimage)
    cv2.imshow("windpow2", next_lev)

    # cv2.imshow("new", findContor(masked))
    cv2.waitKey(1)


if __name__ == '__main__':
    pass