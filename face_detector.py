!pip install opencv-python
import cv2
def faceDetector(img):
    faceModel = cv2.CascadeClassifier("opencv_tut/resources/face.xml")
    faces = faceModel.detectMultiScale(img, 1.2, 7)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x+10, y+10), (x + w, y + h), (0, 255, 0), 4)


vid = cv2.VideoCapture(0)
while True:
    _, frame = vid.read()
    frame = cv2.resize(frame, (1000, 800))
    faceDetector(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
if __name__ == '__main__':
    pass
