import numpy as np
from matplotlib import pyplot as plt 
import cv2

class Algorithms():
    def __init__(self):
        print("PREPROCESSING STARTED")
    def showImage(self,img,title):            
        plt.figure(figsize=(5,5))
        plt.imshow(img,cmap='Greys_r')
        plt.title(title)
        plt.show()
    def apply_otsu(self,img):
        ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return th2
    def apply_dilation(self,img,iterat):
        # Apply dilation : 
        kernel = np.ones((3,3),np.uint8)
        dilation = cv2.dilate(img,kernel,iterations = iterat)
        return dilation
    def region_growing(self,thrs_image):
        """
        thrs_image is the thresholded image whose value is 0 or 255.

        """
        # get rows and columns
        row_num = thrs_image.shape[0]
        col_num = thrs_image.shape[1]
        label = 150
        self.value = 255
        for  i in range(row_num):
            for j in range(col_num):
                self.stack_empty = True
                if thrs_image[i,j] == self.value:
                    stack = self.label_check(thrs_image,i,j,label)

    def label_check(self,thrs_image,i,j,label):
        thrs_image[i,j] = label
        temp_stac = list()
        for r in range(i-1,i+1):
            for e in range(j-1,j+1):
                if thrs_image[r,e] == self.value:
                    temp_stac.append((r,e))
                    self.stack_empty = False


        

"""
plt.figure(figsize=(5,5))
plt.hist(img.ravel(),256,[0,256])
plt.title("Histogram Before Threshold")

# Adaptive Threshold
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)
plt.figure(figsize=(5,5))
plt.imshow(th3)
plt.show()

plt.figure(figsize=(5,5))
plt.hist(img.ravel(),256,[0,256])
plt.title("Histogram After Adaptive Threshold")
plt.show()

# Gaus Filter
blur = cv2.GaussianBlur(th3,(5,5),0)
plt.figure(figsize=(5,5))
plt.imshow(blur)
plt.show()
"""