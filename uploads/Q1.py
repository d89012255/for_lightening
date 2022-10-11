import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Q1 -- Image Processing')

def show_image(pic_name1,pic_name2,que_num):
    if que_num == 'HW1.1':
        img = cv2.imread(pic_name1)
        cv2.imshow(que_num,img)
        print("Height:",img.shape[0],"\nWidth:",img.shape[1])
    elif que_num == 'HW1.2':
        img = cv2.imread(pic_name1)
        #if output without merge(),it would output gray image not blue, green, red colors
        zero = np.zeros(img.shape[:2],dtype = "uint8")
        (B, G, R) = cv2.split(img)
        #merge(B,G,R)->[B,0,0] means stay blue color and remove green,red color
        cv2.imshow('Blue Channel',cv2.merge([B,zero,zero]))
        cv2.imshow('Green Channel',cv2.merge([zero,G,zero]))
        cv2.imshow('Red Channel',cv2.merge([zero,zero,R]))
    elif que_num == 'HW1.3':
        img = cv2.imread(pic_name1)
        img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow('L1',img1)
        col, row, dim = img.shape
        img2 = np.zeros((col, row),np.uint8)
        for i in range(col):
            for j in range(row):
                (b, g, r) = img[i,j] #b, g, r type = uint8
                b = int(b)
                g = int(g)
                r = int(r)
                temp = (b + g + r)/3
                img2[i,j] = np.uint8(temp)
        
        cv2.imshow('L2',img2)
    else:
        def get_data(x):
            img0 = cv2.imread(pic_name1)
            img1 = cv2.imread(pic_name2)
            alpha = cv2.getTrackbarPos('Blending',que_num) #get trackbar value
            
            img2 = cv2.addWeighted(img0,(1-(alpha/255)),img1,alpha/255,0)
            cv2.imshow(que_num,img2)
        
        # create windows
        cv2.namedWindow(que_num)
        cv2.createTrackbar('Blending', que_num, 0, 255,get_data)
        # set parameters
        cv2.setTrackbarPos('Blending', que_num, 128)

#button1 set up
bt1 = tk.Button(window, text='1.1 Load Image', font=('Arial', 12))
bt1['width'] = 50
bt1['height'] = 4
bt1.grid(column = 0, row = 0)

#function without parameter -> bt1.config(command = show_image)
bt1.config(command = lambda:show_image('Sun.jpg','null','HW1.1'))

#button2 set up
bt2 = tk.Button(window, text='1.2 Color Seperation', font=('Arial', 12))
bt2['width'] = 50
bt2['height'] = 4
bt2.grid(column = 0, row = 1)

bt2.config(command = lambda:show_image('Sun.jpg','null','HW1.2'))

#button3 set up
bt3 = tk.Button(window, text='1.3 Color Transformation', font=('Arial', 12))
bt3['width'] = 50
bt3['height'] = 4
bt3.grid(column = 0, row = 2)

bt3.config(command = lambda:show_image('Sun.jpg','null','HW1.3'))

#button4 set up
bt4 = tk.Button(window, text='1.4 Blending', font=('Arial', 12))
bt4['width'] = 50
bt4['height'] = 4
bt4.grid(column = 0, row = 3)

bt4.config(command = lambda:show_image('Dog_Strong.jpg','Dog_Weak.jpg','HW1.4'))


window.mainloop()






