import cv2
import numpy as np
import time



# img = cv2.imread('opencv_tut/resources/car1.jpg')

# img = cv2.resize(img, (1080, 720))
vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read()
    gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gary = cv2.GaussianBlur(gary, (7, 7), 1.8)
    gary = cv2.Canny(gary, 120, 120, 4)

    # for i in gary:
    #     if sum(i) != 0:
    #         print(sum(i))
    # # print(np.where(gary>=0))
    # break
    cv2.imshow("hello", gary)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


if __name__ == '__main__':
    pass