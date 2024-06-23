# Region-Growing-Image-Segmentation

## Region Growing

### Introduction and Goals
In this project, a region of interest, which is a finger, is aimed to be obtained by using some image processing algorithms. First, the OTSU thresholding algorithm is applied to get the foreground and background images. After this, the region growing algorithm is applied and the largest possible rectangle is calculated and plotted to get and show the region of interest on the image.

### Method 1: Image Enhancement
This method is used to process images in early stages of the pipeline to get suitable images for the region growing algorithm.

\[ g(x) = a f(x) + B \]

This linear transformation is used to get a brighter image. Here \( a \) and \( B \) are constants and \( f(x) \) is our image.

### Method 2: Otsu Thresholding
OTSU algorithm considers two different classes and tries to minimize the weighted within-class variance:

\[ q_w(t) = q_1(t) \cdot \sigma_1^2(t) + q_2(t) \cdot \sigma_2^2(t) \]

where \( q_{1,2}(t) \) denotes the class probabilities. To calculate the probability for one class, the number of pixels whose gray value is bigger than the threshold should be divided by the total number of pixels. The same thing can be done for pixels whose gray value is less than the threshold. Therefore, the algorithm finds a value of \( t \) with which the two classes' variance becomes minimum.

### Method 3: Region Growing
Region growing is one of the image segmentation methods in which one seed or multiple seeds are chosen as starting points for a unique region. According to the neighbors of the seed, the region is expanded by adding the neighboring pixels if they satisfy some rule-based criteria. Adding a new pixel to a region can depend on many different features of the image. Some of them are given below:
- Average intensity
- Variance
- Color
- Texture
- Size

In this case, intensity values were used as a reference for growing the region.

### Method 4: Dilation and Erosion
After region growing, in order to find the possible rectangle inside and outside of the image, morphological operations are applied to get bigger and smaller regions. After obtaining these areas, possible rectangles are tried to be found.

After region growing, the largest possible rectangle is plotted on the original image that is obtained from the labeled image to show the region of interest.

### Results
The results show the effectiveness of the region growing method combined with other image processing techniques.

### Discussion
* Image contrast affects the OTSU results. Without contrast manipulation, the OTSU algorithm is not that efficient in distinguishing the foreground and background.
* Unconnected neighbors created problems during the region growing algorithm, and this can be solved with morphological methods.
* Erosion might delete more data than needed; that's why the inner rectangle does not fit well in some images because of the different contrast levels.
* Applying thresholding and then applying the region growing method gives good results, but results can be improved with different algorithms such as the region growing algorithm based on the surface fitting method that is explained in this [article](https://www.semanticscholar.org/paper/Segmentation-through-Variable-Order-Surface-Fitting-Besl-Jain/9cb0b37ade76ffb299f6d103203e246d058a6d8c).
