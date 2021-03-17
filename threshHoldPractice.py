# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:12:36 2021

@author: SaLmAn
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 11:03:22 2021

@author: SaLmAn
"""
import imageio as io
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img=cv.imread("original.png",0);
plt.imshow(img,cmap="gray");
plt.show();
plt.close();


# Showing Histogram
plt.hist(img.ravel(),bins=100);
plt.show();
plt.close();


#       Method 1

# th=187;

# r,c=img.shape;
# i=0;
# j=0;


# for i in range(r):
#     for j in range(c):
        
#         if img[i,j]>th:
#             img[i,j]=255;
#         else:
#             img[i,j]=0;
            

# plt.imshow(img,cmap="gray") ;           
# plt.show();
# plt.close();




#       Method 2

# th=0;
# rV,dImg=cv.threshold(img,th,255,cv.THRESH_BINARY +cv.THRESH_OTSU);

# plt.imshow(dImg,cmap="gray");
# plt.show();
# plt.close();




