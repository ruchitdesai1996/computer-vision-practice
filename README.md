# computer-vision-practice

Grab and Cut - A Computer Vision Algorithm which is used along with OpenCv and in Python to cut out the background extra spaces from the spcific image.

Using the import "matplotlib" we import the matplotlib package in our python code.

Reading the image as our input image:

We need to make sure to give an image as an input so that the interpreter can read our image using cv2.imread() funtion.

After that we need to create rectangle which will help us to cut the image specified through the dimensions. So we will use 

// cv2.rectangle(img, frame1, frame2, thickness, border) 

After creating the rectangle we will apply the Grab and Cut algorithm which will enforce the cut on the image and crop the background according to our need.

// cv2.grabCut(img, mask, rect, bgModel, fgModel, iterations, cv2.GC_INIT_WITH_RECT)


Finally we need to plot the image with the function plt.image() and then show the image using plt.imshow()

//


