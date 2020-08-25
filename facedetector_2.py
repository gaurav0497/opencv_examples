import cv2
img = cv2.imread("resource/gaurav.jpg")
# face_1 = img[65:190, 110:210]
# face_1 = cv2.resize(face_1, (300, 350))
# img_2 = cv2.imread("resource/photo7.jpg", 0)
# face_2 = img_2[150:500, 300:600]
#
# well = cv2.bitwise_and(face_2, face_1)
# a = cv2.findContours(img, cv2.RETR_CCOMP, cv2. )
# img = cv2.Canny(img, 155, 300, 1)
# contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# print(img.shape)
# cv2.imshow("image_2", img)
# # print(contours)
# img=cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
def faceDetector(img):
    faceModel = cv2.CascadeClassifier("opencv_tut/resources/face.xml")
    faces = faceModel.detectMultiScale(img, 1.2, 7)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x+10, y+10), (x + w-10, y + h), (0, 255, 0), 1)
faceDetector(img)
cv2.imshow("image_1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()