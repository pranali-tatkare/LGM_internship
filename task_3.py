# -*- coding: utf-8 -*-
"""task 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kl3M6EFrk9s3ywj293gPoXYooJApkPFk

Data science internship

Batch=August 2023

Task- image to pencil sketch with python (level-Beginner)

Pranali Dattaram Tatkare
"""

import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize']=[15,6]

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/content/picture.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.axis('off')
#plt.grid(False)
plt.title('original image',size=12)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img,cmap='gray')
plt.axis('off')
#plt.grid(False)
plt.title('grayscale image',size=12)

inv_img=cv2.bitwise_not(gray_img)
plt.imshow(inv_img,cmap='gray')
plt.axis('off')
#plt.grid(False)
plt.title('inverted image',size=12)

blur_img=cv2.GaussianBlur(inv_img,(21,21),sigmaX=0,sigmaY=0)
plt.imshow(blur_img,cmap='gray')
plt.axis('off')
plt.title('blur image',size=12)

pencil_sketch=cv2.divide(gray_img,255-blur_img,scale=255)
plt.imshow(pencil_sketch,cmap='gray')
plt.axis('off')
plt.grid(False)
plt.title('pencil sketch',size=12);

