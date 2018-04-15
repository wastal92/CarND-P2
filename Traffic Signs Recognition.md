# Traffic Signs Recognition
---
**Build a Traffic Sign Recognition Project**
The goals / steps of this project are the following:
- Load the data set (see below for links to the project data set)
- Explore, summarize and visualize the data set
- Design, train and test a model architecture
- Use the model to make predictions on new images
- Analyze the softmax probabilities of the new images
- Summarize the results with a written report

Here is the link to my project code

-------

### Data Set Summary & Exploration
1. Data Set Summary
First, I downloaded the data set from [here](https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/traffic-signs-data.zip) and then extracted it. The data set includes three sets: **train.p** for training, **valid.p** for validation and **test.p** for test.The train, validation and test set contain 34799, 4410 and 12630 examples respectively. The size of each example is 32*32 in width and height. There are 43 unique classes for the entire sets.

2. Exploratory visualization of the dataset
Here is an exploratory visualization of the train data set. Each number in the horizontal axis represents a class and the vertical axis stand for the number of examples in corresponding class.
![pics](https://github.com/wastal92/CarND-P2/blob/master/file_pics/p1.png)

### Design and Test a Model Architecture
1. Preprocess the data
At first, I augmented the train data set because, as can be seen from the above visualization picture, the train set is very unbalanced. Some classes such as the first class contain about only 200 examples while others may include around 2000 examples like the second class. If I train the model with this data set, the classifier may not unable to recognize some classes with small amount examples. So, I applied random translation, random rotation, random scaling and random brightness on the train set with OpenCV to make each class contain the same number of examples. Here are the examples of the traffic sign before and after each random processing.

**Random translation**

![trans](https://github.com/wastal92/CarND-P2/blob/master/file_pics/translate.png)

**Random rotation**

![rotation](https://github.com/wastal92/CarND-P2/blob/master/file_pics/rotate.png)

**Random scaling**

![scale](https://github.com/wastal92/CarND-P2/blob/master/file_pics/scale.png)

**Random brightness**

![bright](https://github.com/wastal92/CarND-P2/blob/master/file_pics/brightness.png)

After augmentation, the distribution of each class in the data set is shown below.

![after_aug](https://github.com/wastal92/CarND-P2/blob/master/file_pics/after_augment.png)

Then I processed the training set to make it suitable for training. The process includes grayscaling the images, enhancing the contrast and normalization. Shape is the essential for recognition instead of color. As a result, I applied the grayscaling to make the training process more efficient. Then, the quality of some examples are not satisfied, so I enhanced the contrast of the images by adaptive histogram equalization in OpenCV. Finally, I normalized the data set to make the optimization converge faster.
The image after grayscaling and enhancing contrast is shown below.
![after_process](https://github.com/wastal92/CarND-P2/blob/master/file_pics/process.png)

2. Model stucture
My final model consisted of the following layers:

Layer  |   Description
--------|-----------
Input    |   32×32×1 gray image
Convolution 5×5  |  $1\times1$stride, same padding, outputs $32\times32\times32$

