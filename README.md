# Region-Growing-Image-Segmentation

# Region Growing
## Introduction and Goals
In this project, a region of interest which is a finger is aimed to be obtained by using some image processing algorithms. First, OTSU thresholding algorithm is applied to get the foreground and background images. After this, the region growing algorithm is applied and the largest possible rectangle is calculated and plotted to get and show the region of interest on the image.
## Method 1
### Image Enchacenment : 
This method is used to process images in eary stages of the pipline to get suitable images for region growing algorithm. 

$g(x) = af(x) + B$

This linear transformation is used to get more bright image. Here a and B is a constant and f(x) is our image. This transformation results the following images.
Original Image |Image After Transformation|
:-----------------:|:---------------:
![harold](images/new_method/rec/Enchancement/01(1).jpg)|![harold_noise](images/new_method/rec/Enchancement/ench_01(1).jpg)

One can see the affect of this operation on OTSU thresholding with the given two images.

OTSU Before |OTSU After|
:-----------------:|:---------------:
![harold](images/new_method/rec/Enchancement/otsu_01(1).jpg)|![harold_noise](images/new_method/rec/Enchancement/thres_01(1).jpg)

## Method 2 


### Otsu Thresholding
 OTSU algorithm considers two different classes and tries to minimize the weighted within-class variance[1]
$q_w(t) = q_1(t)var_1^2(t) + q_2(t)var_2^2(t)$

$q_{1,2}(t)$  donates the class probabilities. To calculate the probability for one class, the number of pixels whose gray value is bigger than the threshold should be divided with the total number of pixels. The same thing can be done but pixels whose gray value is less than the threshold should be considered. Therefore the algorithm finds a value of t with which two classes' variance become minimum. Some of the results of the thresholding is given below.

Image 1 |Image 2|Image 3|
:-----------------:|:---------------:|:-----------------:
![harold](images/new_method/rec/Enchancement/thres_0053_3_1_120511-103050.png)|![harold_noise](images/new_method/rec/Enchancement/thres_01(1).jpg)|![harold_noise](images/new_method/rec/Enchancement/thres_0046_3_4_120523-160627.png)

## Method 3
### Region Growing
Region growing is one of the image segmentation methods in which one seed or multiple seeds are chosen that are starting points for a unique region. According to the neighbors of the seed, the region is expanded by adding the neighbor pixels if they satisfy some rules-based criteria. Adding a new pixel to a region can depend on many different features of the image. Some of them are given below. 
* average intensity
* variance
* color
* texture
* size
In my case, I used the intensity values as a reference for growing the region. Region growing depending on one seed point can be observed with the given figure below. 

![](growing.gif)
<sub>Image Source: [Gyfcat](https://gfycat.com/)</sub>

## Method 4
#### Dilation and Erosion
After region growing, in order to find the possible rectangle inside and outside of the image, morphological operations are applied to get bigger and smaller regions. After optaining these areas, possible rectangles are tried to be found. You can see the original image, dilated and erosioned images below.

OTSU | Dilation| Erosion |
:-----------------:|:---------------:|:-----------------:
![](images/new_method/rec/Enchancement/thres_30_4(6).jpg)|![](images/new_method/rec/Enchancement/dil_30_4(5).jpg)|![](images/new_method/rec/Enchancement/er_30_4(6).jpg)




After region growing, biggest possible rectangle is plotted on the original image that is obtained from the labeled image to show the region of interest. These images are given in the results section.

## Results
<img src="images/new_method/rec/Enchancement/rec_0003_6_4_120524-161445.png" width="400"/>

<img src="images/new_method/rec/Enchancement/rec_0007_6_3_120523-110018.png" width="400"/>

<img src="images/new_method/rec/Enchancement/rec_30_4(2).jpg" width="400"/>
<img src="images/new_method/rec/Enchancement/rec_30_4(1).jpg" width="400"/>

## Discussion 
* Unconnected neighbors created problems during region growing algorithm and this can be solved with morphological methods. For example, opening operation can be used to connect foreground pixels to each other after OTSU thresholding. 
* Applying thresholding and than applying region growing method gives a good result but results can be made better with different algorithms such as region growing algorithm based on surface fitting method that is explained in this <a href="https://www.semanticscholar.org/paper/Segmentation-through-Variable-Order-Surface-Fitting-Besl-Jain/9cb0b37ade76ffb299f6d103203e246d058a6d8c" target="_top">article</a>.