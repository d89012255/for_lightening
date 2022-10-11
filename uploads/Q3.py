import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk
import math
import matplotlib.pyplot as plt

window = tk.Tk()
window.title('Q3 -- Edge Detection')

def pending(img_data):
    pending_img = np.zeros((351, 600),np.uint8)
    for i in range(1,350):
        for j in range(1,599):
            pending_img[i,j] = img_data[i-1,j-1]

    return pending_img

#gray level image
img = cv2.imread('House.jpg') #img.shape = 349, 598, 3
gray_original_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#pending
gray_img = np.zeros((351, 600),np.uint8)
gray_img = pending(gray_original_img)         
#create Gussian_Filter
gau_kernel = np.zeros((3, 3))
sigma = 0.707    
for a in range(3):
    for b in range(3):
        c = a - 1
        d = b - 1
        value = np.exp(-(c*c+d*d)/(2*sigma*sigma))
        value = value/(2*np.pi*sigma*sigma)
        gau_kernel[a,b] = value           
#gaussian_filter normalize -> (every gaussian_filter value /= sum of gaussian_filter value)
gau_kernel /= gau_kernel.sum()
#do Gaussian Smoothing
gau_img = np.zeros((349, 598),np.uint8)
for m1 in range(349):
    for n1 in range(598):
        gau_data = np.sum(np.multiply(gau_kernel, gray_img[m1:m1 + 3, n1:n1 + 3]))
        gau_img[m1,n1] = np.uint8(gau_data)

#Sobel_X, Sobel_Y, Magnitude
sobelx_filter = np.array([[-1.0,0.0,1.0],[-2.0,0.0,2.0],[-1.0,0.0,1.0]])
sobely_filter = np.array([[1.0,2.0,1.0],[0.0,0.0,0.0],[-1.0,-2.0,-1.0]])
gaux = np.zeros((349, 598),np.uint8)
gaux = gau_img
solx_img = np.zeros((347, 596),np.uint8)
soly_img = np.zeros((347, 596),np.uint8)
man_img = np.zeros((347, 596),np.uint8)
for m2 in range(347):
    for n2 in range(596):
        gx = np.sum(np.multiply(sobelx_filter, gaux[m2:m2 + 3, n2:n2 + 3]))
        gy = np.sum(np.multiply(sobely_filter, gaux[m2:m2 + 3, n2:n2 + 3]))
        gm = np.sqrt(np.square(gx) + np.square(gy))
        gx = np.abs(gx)
        gy = np.abs(gy)
        gm = np.abs(gm)
        solx_img[m2,n2] = np.uint8(gx)
        soly_img[m2,n2] = np.uint8(gy)
        man_img[m2,n2] = np.uint8(gm)

def show_image(que_num):
    if que_num == '1':
        cv2.imshow('GrayScale',gray_original_img)
        cv2.imshow('Gaussian Blur',gau_img)
    elif que_num == '2':
        cv2.imshow('Sobel X',solx_img)
    elif que_num == '3':
        cv2.imshow('Sobel Y',soly_img)
    elif que_num == '4':
        cv2.imshow('Magnitude',man_img)
    
#button1 set up
bt1 = tk.Button(window, text='3.1 Guassian Blur', font=('Arial', 12))
bt1['width'] = 50
bt1['height'] = 4
bt1.grid(column = 0, row = 0)

bt1.config(command = lambda:show_image('1'))

#button2 set up
bt2 = tk.Button(window, text='3.2 Sobel X', font=('Arial', 12))
bt2['width'] = 50
bt2['height'] = 4
bt2.grid(column = 0, row = 1)

bt2.config(command = lambda:show_image('2'))

#button3 set up
bt3 = tk.Button(window, text='3.3 Sobel Y', font=('Arial', 12))
bt3['width'] = 50
bt3['height'] = 4
bt3.grid(column = 0, row = 2)

bt3.config(command = lambda:show_image('3'))

#button4 set up
bt4 = tk.Button(window, text='3.4 Magnitude', font=('Arial', 12))
bt4['width'] = 50
bt4['height'] = 4
bt4.grid(column = 0, row = 3)

bt4.config(command = lambda:show_image('4'))

window.mainloop()
