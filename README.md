# ImageAnalysis
## Scripts to manipulate and analyze images for cultural heritage science.

This repository is a work in progress, but ultimately seeks to provide cultural heritage scientists with safe, free, and easy-to-use technology to accomplish tasks that could otherwise involve unsecured websites or expensive/inaccessible programs.

VERSION 1.1

**ImageResizerFiles**

The files in the ImageResizerFiles folder accept a folder of images and a destination directory as input and return a resized version of the original files with the prefix "resized_" before the original file name to save in the destination directory. The images are resized based on the dimensions of the lowest pixel resolution of the original dataset (because different cameras for different hyperspectral data result in different resolutions among the images). 

To use these files:
1. Run the main.py file
2. A popup window with buttons will appear to ask for the filetype of the images you would like to resize. This feature supports .jpg and .tif file types, but can support more if desired. This way, only specific image types will be pulled from folders that could have many image types. The user will just have to click on one of these buttons one time.
3. A popup window will appear to ask for the directory of the images you wish to input. Navigate to the folder of images you wish to resize and click submit. Folders with multiple file types will be filtered to only resize the original filetype.
4. Another popup window will appear to ask for the destination directory.
5. The code now has enough information to run. The terminal will print out the dimensions of all of the input images and indicate the smallest dimensions, and then your resized images will be available in the directory above the directory selected for these images. 


**slidertool**

The index script inside this folder takes two images as input and superimposes the images with a slider tool for easy comparison.

To use these files:
1. Copy the file paths of the images you would like to compare inside the quotes on lines 56 and 60.
2. I use a VSCode extension called "Live Server" to display the images locally in real time. I highly recommend this method. I simply right-click "open in live server" and the slider tool is ready to use! 
3. In order to change the images in the slider tool, simply change the file paths.

**imagepoints**
 
checkpoints.py visualizes a set of points indicated in the script. markpoints.py allows a user to click on an image and displays the (x,y) coordinates of the selected point.

To use checkpoints:
1. On line 3, put the filepath of the image you'd like to use between the quotations.
2. The "pts" variable is a numpy array of points, which can be adjusted to display coordinates on an image. I'll develop an interface to select the points more easily later, but for now, just enter each individual set of points in [brackets] and separate each set of coordinates with a comma.
3. Run checkpoints.py. The image will appear with the points you've selected indicated by a red x.

To use markpoints:
1. On line 46, insert the full filepath of the image you'd like to use in between the quotations. I'm planning to make this easier soon, but this is what I have for now.
2. Run markpoints.py. Once the image appears, you can click on various points on the image and the coordinates of that point will be displayed in real time, as well as logged to the console.
