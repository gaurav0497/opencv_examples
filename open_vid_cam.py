
import cv2
import os
import numpy as np
import matplotlib

# kernel = np.ones((3,1), 'uint8')
#
# img = cv2.imread('opencv_tut/resources/experi.jpg', 1)
# img = cv2.resize(img, (720, 600))
#
# canny = cv2.Canny(img, 400, 200)
# imagedilate = cv2.dilate(canny, kernel, iterations=1)
# errode = cv2.erode(imagedilate, kernel, iterations=1)
#
# cv2.imshow("preview1", imagedilate)
# cv2.imshow("preview2", errode)

#
# img = cv2.imread('resource/phot4.jpg')
# img = img[100:500, 300:700]
# cv2.imshow("preview", img)
# # newimg = cv2.imread('resource/phot.jpg')
# # cv2.imshow("new circle", newimg[100:570, 290:720])
# # cv2.waitKey(0)
#
# full = np.zeros((1000, 1400, 3), 'uint8')
# full[0:400, 0:400] += img
# full[0:400, 400:800] += img
# cv2.imshow("preview", full[0:400, 0:800])
# cv2.waitKey(0)
# # Capturing video and taking photos
#
# vid = cv2.VideoCapture(0)
# i = 0
# while True:
#
#     _, frame = vid.read()
#     frame = cv2.resize(frame, (1000, 720))
#     cv2.imshow("frame", frame)
#     cv2.imwrite('resource\photo{}.jpg'.format(i), frame)
#     i = i + 1
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# taking 20 images


# photo_album = []
# for i in range(20):
#     ab = cv2.imread(f'resource/photo{i}.jpg')
#     ab = cv2.resize(ab, (200, 200))
#     photo_album.append(ab)

# JOINING IMAGES

#
# def image_joiner(height, width):
#     blank = np.zeros((height, width, 3), 'uint8')
#     size1 = 0
#     size2 = 0
#     while size2 < height:
#         for photo in photo_album:
#             if size1 < width:
#                 blank[size2:size2+200, size1:size1+200] += photo
#                 size1 += 200
#         size2 += 200
#         size1 = 0
#     return blank
#
# get_img = image_joiner(1000,1000)
# imagine = cv2.cvtColor(get_img, cv2.COLOR_BGR2BGRA)
# cv2.imshow("congrats", imagine)
# cv2.waitKey(0)

image = cv2.imread('resource/exp2.jpg')
# width = 400
# height = 260
#
# image = np.zeros((512, 512, 3), 'uint8')

# pt1 = np.float32([[530, 164], [809, 169], [567, 420], [830, 345]])
# pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
#
# matrix = cv2.getPerspectiveTransform(pt1, pt2)
# image2 = cv2.warpPerspective(image, matrix, (width, height))
# HEL = cv2.putText(image, "hello world", (823, 132), cv2.FONT_ITALIC, 2, (120, 255, 120), 1)

cv2.imshow("window", image)
# cv2.imshow("window2", image2)
cv2.waitKey(0)


if __name__ == '__main__':
    pass
