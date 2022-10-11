import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Q2 -- Image Smoothing')

def Gaussian_Filter(pic_name):
    img = cv2.imread(pic_name)
    img1 = cv2.GaussianBlur(img, (5, 5), 1)
    
    cv2.imshow('HW2.1',img1)

def Bilateral_Filter(pic_name):
    img = cv2.imread(pic_name)
    img1 = cv2.bilateralFilter(img, 9, 90, 90)
    cv2.imshow('HW2.2',img1)

def Median_Filter(pic_name):
    img = cv2.imread(pic_name)
    img1 = cv2.medianBlur(img, 3)
    cv2.imshow('HW2.3 -- 3x3',img1)
    img2 = cv2.medianBlur(img, 5)
    cv2.imshow('HW2.3 -- 5x5',img2)
    
#button1 set up
bt1 = tk.Button(window, text='2.1 Guassian Blur', font=('Arial', 12))
bt1['width'] = 50
bt1['height'] = 4
bt1.grid(column = 0, row = 0)

#function without parameter -> bt1.config(command = show_image)
bt1.config(command = lambda:Gaussian_Filter('Lenna_whiteNoise.jpg'))

#button2 set up
bt2 = tk.Button(window, text='2.2 Bilateral Filter', font=('Arial', 12))
bt2['width'] = 50
bt2['height'] = 4
bt2.grid(column = 0, row = 1)

bt2.config(command = lambda:Bilateral_Filter('Lenna_whiteNoise.jpg'))

#button3 set up
bt3 = tk.Button(window, text='2.3 Median Filter', font=('Arial', 12))
bt3['width'] = 50
bt3['height'] = 4
bt3.grid(column = 0, row = 2)

bt3.config(command = lambda:Median_Filter('Lenna_pepperSalt.jpg'))

window.mainloop()
