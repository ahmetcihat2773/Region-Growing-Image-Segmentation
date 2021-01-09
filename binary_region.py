import numpy as np
import cv2
from skimage.measure import label
from matplotlib import pyplot as plt 
import os
class BinaryRG():
    def __init__(self):
        print(" ")
    def region_growing_binary(self,thrs_image):
        """
        This algorithm has problem with the labeling unconnected pixels.
        """
        # get rows and columns
        self.thrs_image = thrs_image
        self.row_num = thrs_image.shape[0]
        self.col_num = thrs_image.shape[1]
        # create emtpy image
        self.label_image = np.zeros((self.row_num,self.col_num),dtype=int)
        label = 125
        self.value = 255
        self.stack = list()
        self.visit = list()
        self.stack_empty = True
        self.break_loops = False
        for  i in range(1,self.row_num-1):
            for j in range(1,self.col_num-1):                
                self.label_check(i,j,label)                
        return self.label_image
    def label_check(self,i,j,label):
        for r in range(i-1,i+2,1):
            for e in range(j-1,j+2,1):
                if self.limit(r,e): 
                    if self.thrs_image[r,e] == self.value:                            
                        self.label_image[r,e] = self.value
    def limit(self, x,y):
        return  1<=x<self.row_num and 1<=y<self.col_num
    def apply_dilation(self,img,kernel_size,iterat):
        # Apply dilation : 
        kernel = np.ones((kernel_size,kernel_size),np.uint8)
        dilation = cv2.dilate(img,kernel,iterations = iterat)
        return dilation
    def plot_rectangle(self,img):
        min_corner = [5000,5000]
        max_corner = [0,0]
        for  i in range(1,self.row_num-1):
            for j in range(1,self.col_num-1): 
                if img[i,j] == self.value:
                    if min_corner[0] >= i :
                        min_corner[0] = i
                    if min_corner[1] >= j:
                        min_corner[1] = j
                    if max_corner[0] <= i :
                        max_corner[0] = i
                    if max_corner[1] <= j:
                        max_corner[1] = j
        print(min_corner,"ARADA",max_corner)
        return min_corner,max_corner
    def showImage(self,img,title):            
        plt.figure(figsize=(5,5))
        plt.imshow(img,cmap='Greys_r')
        #plt.imshow(img)
        plt.title(title)
        plt.show()
binary_rg = BinaryRG()
for filename in os.listdir("./UTFVP"):
    if "png" in filename:
        # READ IMAGE
        #img = cv2.imread('./UTFVP/0003_6_4_120524-161445.png',cv2.CV_8U)
        img = cv2.imread('./UTFVP/'+filename,cv2.CV_8U)
        # APPLY THRESHOLD
        img = cv2.GaussianBlur(img,(5,5),0)
        plt.figure()
        plt.hist(img)
        plt.show()
        ret2,th2= cv2.threshold(img,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)
        cv2.imwrite("otsu_"+filename, th2)
        plt.figure()
        plt.hist(th2)
        plt.show()
        #ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_TRIANGLE)
        #binary_rg.showImage(th2,"After Threshold")
        region_growing = binary_rg.region_growing_binary(th2)
        #binary_rg.showImage(region_growing,"Binary")
        print(filename)
        min_points,max_points = binary_rg.plot_rectangle(region_growing)
        image = cv2.rectangle(img,(max_points[1],max_points[0]),(min_points[1],min_points[0]),(255,0,0),2)
        #binary_rg.showImage(image,"Rectangle")
        #binary_rg.showImage(region_growing,"After Region Growing")
        region_growing = region_growing.astype(np.uint8)
        imC = cv2.applyColorMap(region_growing, cv2.COLORMAP_JET)
        cv2.imwrite("output_"+filename, image) 
        #binary_rg.showImage(imC,"Color Map")
