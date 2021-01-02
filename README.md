# Region-Growing-Image-Segmentation

## region_growing_gray method :
For same label region grows till self.stack become empty which means there is no more same label pixel in image. This method use **label_check_gray** method which calculate the density difference between center pixel and 8-neighboor pixels to catogarize the pixel with labels.

## region_growing_binary : 
This method expect a thresholded image in which background is 0 and foreground is 255. Same prenciple with the region_growing_gray. Seeds are growing for different labels. This method uses **label_check** method which append the neighboor pixel into stack if pixel value is equal to 255. Here, you can remove the background colors if foreground pixels are dominant. 