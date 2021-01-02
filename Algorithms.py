import numpy as np
from matplotlib import pyplot as plt 
import cv2

class Algorithms():
    def __init__(self):
        print("PREPROCESSING STARTED")
    def showImage(self,img,title):            
        plt.figure(figsize=(5,5))
        plt.imshow(img,cmap='Greys_r')
        #plt.imshow(img)
        plt.title(title)
        plt.show()
    def apply_otsu(self,img):
        ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_OTSU)
        return th2
    def apply_dilation(self,img,kernel_size,iterat):
        # Apply dilation : 
        kernel = np.ones((kernel_size,kernel_size),np.uint8)
        dilation = cv2.dilate(img,kernel,iterations = iterat)
        return dilation
    def region_growing_gray(self,img):
        # get rows and columns
        self.img = img
        self.visit = list()
        self.row_num = self.img.shape[0]
        self.col_num = self.img.shape[1]
        self.label_image = np.zeros((self.row_num,self.col_num),dtype=int)
        self.label = 1
        self.label_image[1,1] = self.label
        self.pix_max = int(self.img.max())
        self.pix_min = int(self.img.min())
        self.visit = list()
        # create emtpy image
        self.stack = list()
        self.stack_empty = True
        for  i in range(1,self.row_num-1):
            print("CURRENT",i)
            for j in range(1,self.col_num-1): 
                self.label_check_gray(i,j,self.label)               
                while not self.stack_empty:
                    if self.stack:
                        cr_i = self.stack[0][0]
                        cr_j = self.stack[0][1]
                        #print(len(self.stack))
                        self.stack.pop(0)
                        self.label_check_gray(cr_i,cr_j,self.label)
                    else:
                        self.stack_empty = True
                        self.label = self.label + 10
                        print("LABEL LABEL")
        return self.label_image
    def label_check_gray(self,i,j,label):
        self.label_image[i,j] = label
        if self.stack_empty:
            for r in range(i-1,i+2,1):
                for e in range(j-1,j+2,1):
                    if self.limit(r,e): 
                        if abs(int(self.img[i,j]) - int(self.img[r,e])) <= 3:
                            self.stack.append([r,e])      
        else:                
            if not [i,j] in self.visit:
                for r in range(i-1,i+2,1):
                    for e in range(j-1,j+2,1):
                        if self.limit(r,e): 
                            if abs(int(self.img[i,j]) - int(self.img[r,e])) <= 3:
                            #int(0.1*(self.pix_max-self.pix_min)):  
                                if not [r,e] in self.stack:
                                    if self.label_image[r,e] == 0:
                                        self.label_image[r,e] = label
                                        self.stack.append([r,e])
        #print(len(self.stack))
        self.stack_empty = False
        self.visit.append([i,j])

    def check_neig(self,i,j):
        for r in range(i-1,i+2,1):
            for e in range(j-1,j+2,1):
                if abs(int(self.img[i,j]) - int(self.img[r,e])) <= int(0.1*(self.pix_max-self.pix_min)):
                    if self.img[r,e] == 0:
                        pass
                    else:
                        self.img[i,j] = self.label_image[r,e] 
                        return 0
                
        self.label = self.label + 20
        self.img[i,j] = self.label

    def region_growing_binary(self,thrs_image):
        """
        This algorithm has problem with the labeling unconnected pixels.

        """
        """
        thrs_image is the thresholded image whose value is 0 or 255.

        """
        # get rows and columns
        self.thrs_image = thrs_image
        self.row_num = thrs_image.shape[0]
        self.col_num = thrs_image.shape[1]
        # create emtpy image
        self.label_image = np.zeros((self.row_num,self.col_num),dtype=int)
        label = 254
        self.value = 255
        self.stack = list()
        self.stack_empty = True
        for  i in range(1,self.row_num-1):
            for j in range(1,self.col_num-1):                
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
                        label = label -5
                        print("LABEL LABEL")
        return self.thrs_image
    def label_check_comp(self,i,j,label):
        self.label_image[i,j] = label 
        gray_sum_avg = 0
        # Take the kernel average
        for r in range(i-1,i+2,1):
            for e in range(j-1,j+2,1):
                gray_sum_avg += self.thrs_image[r,e]
        gray_sum_avg = gray_sum_avg/9
        #print("(",i,j,")")
        #print(gray_sum_avg,"::",int(255/2))
        for r in range(i-1,i+2,1):
            for e in range(j-1,j+2,1):
                if self.thrs_image[r,e] == self.value:
                    if r == i and e == j:
                        continue
                    else:                            
                        if not [r,e] in self.stack:
                            self.stack.append([r,e])  
                if int(gray_sum_avg) >= int(255/2):
                    self.label_image[r,e] = 255    
        self.stack_empty = False         
    def label_check(self,i,j,label):
        self.thrs_image[i,j] = label
        for r in range(i-1,i+2,1):
            for e in range(j-1,j+2,1):
                if self.thrs_image[r,e] == self.value:
                    if not [r,e] in self.stack:
                        self.stack.append([r,e])
        self.stack_empty = False
    def limit(self, x,y):
        return  0<=x<self.row_num and 0<=y<self.col_num