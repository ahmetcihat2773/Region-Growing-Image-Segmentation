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
        self.thrs_image = thrs_image
        row_num = thrs_image.shape[0]
        col_num = thrs_image.shape[1]
        label = 1
        self.value = 255
        self.stack = list()
        self.stack_empty = True
        for  i in range(1,row_num-1):
            for j in range(1,col_num-1):                
                if self.thrs_image[i,j] == self.value:
                    self.label_check(i,j,label)
                while not self.stack_empty:
                    if self.stack:
                        cr_i = self.stack[0][0]
                        cr_j = self.stack[0][1]
                        self.stack.pop(0)
                        self.label_check(cr_i,cr_j,label)
                    else:
                        self.stack_empty = True
                        label = label +20
                        print("LABEL",label)
        return self.thrs_image
    def label_check(self,i,j,label):
        self.thrs_image[i,j] = label
        for r in range(i-1,i+2,1):
            for e in range(j-1,j+2,1):
                if self.thrs_image[r,e] == self.value:
                    if not [r,e] in self.stack:
                        self.stack.append([r,e])
        self.stack_empty = False
