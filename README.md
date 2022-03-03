# aruco_tag_opencv
# First of all Big Thank you to "pyimagesearch founder Adrian Rosebrock" for his excellent knowledge on computer vision and provided the guide.
## Aruco library for Augmented Reality applications based on OpenCV(I am using Python to Write the Code)
## aruco is used in various computer vision and augmented reality application
## 1. camera calibration
## 2. find the object in a given image
## 3. pose estimation
### To Aruco package by default comes under opencv package
In windows use this command to install : pip install opencv-python,
pip install opencv-contrib-python
#### How to Run the Code
#### simplily run the file in command prompt or terminal : python generate_aruco_tag.py ,
#### to see the output go to the output folder and check the result
#### if you want to create your own aruco tag then simple edit the generate_aruco_tag.py file and updated the following 
 ex1:<b> arucoType="DICT_4X4_50", id=20, size=300</b>, 
ex2:<b> arucoType="DICT_5X5_50", id=21, size=300 </b>,
<b> arco.path_to_save = r"output/image_name.png" </b>
