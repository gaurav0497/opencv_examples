import cv2
import numpy as np

points = []
def getContor(img):
    contours, heirachy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
    pot = []
    x, w, y =0, 0, 0
    h=0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            print(area)
            cv2.drawContours(frame, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.8*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(frame, (x,y), (x+20,y+20), (0,255,0), 2)
            # cv2.rectangle(frame,)
            # pot.append(x)
            # pot.append(y)
    # return pot


def drawonCanvass(points):
    cv2.circle(frame, (points[0], points[1]), 20, (0, 255, 0), cv2.FILLED)

# image = cv2.imread("resource/finger_exact.jpeg")
# image = cv2.resize(image, (600, 600))
# image = image[200:380, 100:500]
# cannyImg = cv2.bitwise_and(image, image, mask=cannyImg)
# imagecont = image.copy()
# getContor(cannyImg)
# cv2.imshow("hello", imagecont)
# cv2.waitKey(0)
vid = cv2.VideoCapture(1)
while True:
    _, frame = vid.read()
    frame = cv2.resize(frame, (1000, 800))
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    image = cv2.GaussianBlur(image, (3, 3), 0)
    # image = cv2.dilate(image,(7,7),1, iterations=1)
    # low, upp = np.array([90, 48, 0]), np.array([118, 255, 255])
    low, upp = np.array([73, 22, 16]), np.array([82, 237, 237])
    cannyImg = cv2.inRange(image, lowerb=low, upperb=upp)

    getContor(cannyImg)
    cannyImg = cv2.bitwise_and(frame, frame, mask=cannyImg)
    # cv2.circle(frame, (x, y-5), 20, (0, 255, 0), cv2.FILLED)
    # for pt in points:
    #     if len(pt)!=0:
    #         drawonCanvass(pt)
    cv2.imshow("fram2", cannyImg)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break