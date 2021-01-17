import numpy as np
import cv2
from skimage.measure import label
from matplotlib import pyplot as plt 
import os
class BinaryRG():
    def __init__(self):
        self.window_size = 15
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
        self.value = 255
        self.stack = list()
        self.visit = list()
        self.stack_empty = True
        self.break_loops = False
        for  i in range(1,self.row_num-1):
            for j in range(1,self.col_num-1):                
                self.label_check(i,j)                
        return self.label_image
    def label_check(self,i,j):
        for r in range(i-1,i+2,1):
            for e in range(j-1,j+2,1):
                if self.limit(r,e): 
                    if self.thrs_image[r,e] == self.value:                            
                        self.label_image[r,e] = self.value
    def neigh_check(self,i,j,m,img):
        count = 0
        for r in range(i-m,i+m+1,1):
            for e in range(j,j+m+1,1):
                if self.limit(r,e): 
                    if img[r,e] == 255:                            
                        count = count + 1
        if count == (2*m+1)*(m+1): 
            return True
        else:
            count = 0
            for r in range(i,i+m+1,1):
                for e in range(j-m,j+m+1,1):
                    if self.limit(r,e): 
                        if img[r,e] == 255:                            
                            count = count + 1
            if count == (2*m+1)*(m+1): 
                return True
            else: 
                return False

    
    def limit(self, x,y):
        return  1<=x<self.row_num and 1<=y<self.col_num
    def apply_dilation(self,img,kernel_size,iterat):
        # Apply dilation : 
        kernel = np.ones((kernel_size,kernel_size),np.uint8)
        dilation = cv2.dilate(img,kernel,iterations = iterat)
        return dilation
    def out_rectangle(self,img):
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
    def in_rectangle(self,img):
        min_corner = [5000,5000]
        max_corner = [0,0]
        for  i in range(1,self.row_num-1):
            for j in range(1,self.col_num-1): 
                if img[i,j] == self.value:
                    flag_minmax = self.neigh_check(i,j,self.window_size,img)
                    if flag_minmax: 
                        if min_corner[0] >= i :
                            min_corner[0] = i
                            
                        if min_corner[1] >= j :
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
for filename in os.listdir("./FV-USM"):
    if "jpg" in filename:
        # READ IMAGE
        #img = cv2.imread('./UTFVP/0003_6_4_120524-161445.png',cv2.CV_8U)
        img = cv2.imread('./FV-USM/'+filename,cv2.CV_8U)
        # APPLY THRESHOLD
        alpha = 5
        beta = 20
        # Change the contrast of the image
        img_en = cv2.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0,beta)
        binary_rg.showImage(img_en,"title")
        # apply threshold
        ret2,th2= cv2.threshold(img_en,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)
        #cv2.imwrite("new_method/thres_"+filename, th2)
        # apply region growing
        binary_rg.showImage(th2,"title")
        region_growing = binary_rg.region_growing_binary(th2)
        region_growing = region_growing.astype(np.uint8)
        color_map = cv2.applyColorMap(region_growing, cv2.COLORMAP_JET)
        #cv2.imwrite("new_method/colormap_"+filename, color_map)
        #cv2.imwrite("new_method/reggrow_"+filename, region_growing)
        # apply dilation
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
        dil_region = cv2.dilate(region_growing,kernel,iterations = 1)
        
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
        # appply erosion
        er_region = cv2.erode(region_growing,kernel,iterations = 7)
        binary_rg.showImage(er_region,"title")
        #cv2.imwrite("new_method/dil_"+filename, dil_region)
        #cv2.imwrite("new_method/er_"+filename, er_region)
        print(filename)
        # find proper rectangeles
        min_out,max_out = binary_rg.out_rectangle(dil_region) 
        min_in,max_in = binary_rg.in_rectangle(er_region)
        # Place and on the original image
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        image = cv2.rectangle(img,(max_out[1],max_out[0]),(min_out[1],min_out[0]),(0,0,255),1)
        image = cv2.rectangle(img,(max_in[1],max_in[0]),(min_in[1],min_in[0]),(0,0,255),1)
        binary_rg.showImage(image,"title")
        #cv2.imwrite("new_method/ench_"+filename, img_en)
        #cv2.imwrite("new_method/rec_"+filename, image)