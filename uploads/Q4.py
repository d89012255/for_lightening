import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Q4 -- Transforms')

def func(pic_name,que_num):
    img = cv2.imread(pic_name)
    img1 = cv2.resize(img,(256,256))
    if que_num == 'HW4.1':
        cv2.arrowedLine(img1,(0,0),(256,0),(0,0,255),3,1,0,0.1)
        cv2.arrowedLine(img1,(0,0),(0,256),(0,0,255),3,1,0,0.1)
        cv2.circle(img1,(128,128),0,(0,0,255),3)
        cv2.putText(img1,'C:(128,128)',(130, 128), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('HW4.1 -- resize',img1)
    elif que_num == 'HW4.2':
        H = np.float32([[1,0,0],[0,1,188]])
        img1 = cv2.warpAffine(img1,H,(600,900))
        cv2.arrowedLine(img1,(0,188),(256,188),(0,0,255),3,1,0,0.1)
        cv2.arrowedLine(img1,(0,188),(0,444),(0,0,255),3,1,0,0.1)
        cv2.circle(img1,(128,316),0,(0,0,255),3)
        cv2.putText(img1,'C\':(128,128)',(130, 316), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('HW4.2 -- translation',img1)
    elif que_num == 'HW4.3':
        R = cv2.getRotationMatrix2D((128,128),10,0.5)
        img1 = cv2.warpAffine(img1,R,(400,300))
        cv2.arrowedLine(img1,(80,200),(210,180),(0,255,255),3,1,0,0.1)
        cv2.arrowedLine(img1,(80,200),(210,200),(0,255,255),3,1,0,0.1)
        cv2.putText(img1,'10',(220,200), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('HW4.3 -- rotation and scaling',img1)
    elif que_num == 'HW4.4':
        pts1 = np.float32([[50,50],[200,50],[50,200]])
        pts2 = np.float32([[10,100],[200,50],[100,250]])
        S = cv2.getAffineTransform(pts1,pts2)
        img1 = cv2.warpAffine(img1,S,(700,700))
        cv2.namedWindow('HW4.4 -- shearing',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('HW4.4 -- shearing',700,700)
        cv2.imshow('HW4.4 -- shearing',img1)
    
#button1 set up
bt1 = tk.Button(window, text='4.1 Resize', font=('Arial', 12))
bt1['width'] = 50
bt1['height'] = 4
bt1.grid(column = 0, row = 0)

#function without parameter -> bt1.config(command = show_image)
bt1.config(command = lambda:func('SQUARE-01.png','HW4.1'))

#button2 set up
bt2 = tk.Button(window, text='4.2 Translation', font=('Arial', 12))
bt2['width'] = 50
bt2['height'] = 4
bt2.grid(column = 0, row = 1)

bt2.config(command = lambda:func('SQUARE-01.png','HW4.2'))

#button3 set up
bt3 = tk.Button(window, text='4.3 Rotation , Scaling', font=('Arial', 12))
bt3['width'] = 50
bt3['height'] = 4
bt3.grid(column = 0, row = 2)

bt3.config(command = lambda:func('SQUARE-01.png','HW4.3'))

bt4 = tk.Button(window, text='4.4 Shearing', font=('Arial', 12))
bt4['width'] = 50
bt4['height'] = 4
bt4.grid(column = 0, row = 3)

bt4.config(command = lambda:func('SQUARE-01.png','HW4.4'))

window.mainloop()
