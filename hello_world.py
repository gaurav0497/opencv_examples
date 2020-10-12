import tkinter as tk
import cv2


root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def hello():
    label1 = tk.Label(root, text='Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    cap = cv2.VideoCapture(0)
    canvas1.create_window(150, 200, window=label1)
    while True:
        _, vid = cap.read()
        canvas1.create_window(150, 150, window="frame")
        cv2.imshow("frame", vid)
        cv2.waitKey(1)





# button1 = tk.Button(text='Click Me', command=hello, bg='brown', fg='white')



root.mainloop()