import cv2
import numpy as np

# def drawCircle(event, x, y,flag, params):
#     if event == cv2.EVENT_MOUSEMOVE:
#         # print(x, y)
#         cv2.circle(image, (x+2, y+2), 10, (0, 255, 0), 1)
#
# image = np.zeros((600, 600, 3))
# cv2.namedWindow("image")
# cv2.imshow("image", image)
# (cv2.EVENT_MOUSEMOVE)
# cv2.setMouseCallback("image", drawCircle)
# while True:
#     cv2.imshow("image", image)
#
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
# cv2.destroyAllWindows()
#
# print([i for i in dir(cv2) if "EVENT" in i])

def draw_rect(x, y):
    image = np.zeros((1200, 1200, 3))
    cv2.rectangle(image, (x, y), (x+50, y+50), (255, 0, 0), cv2.FILLED)
    cv2.imshow("image", image)


#
x, y = 0, 0
# while y < 600:
#     while x < 600:
#         draw_rect(x, y)
#         x += 50
#     y += 50
#     x = 0
while True:
    draw_rect(x, y)
    key = cv2.waitKey(1) & 0xff
    if (key == ord('d') and x < 550) or (key == 54 and x < 550):
        x += 50
        draw_rect(x+50, y)
    if (key == ord('s') and y < 550) or (key == 50 and y < 550):
        y += 50
        draw_rect(x, y)
    if (key == ord('a') and x > 0) or (key == 52 and x > 0):
        x -= 50
        draw_rect(x + 50, y)
    if (key == ord('w') and y > 0) or (key == 56 and y > 0):
        y -= 50
        draw_rect(x + 50, y)

# cv2.destroyAllWindows()
