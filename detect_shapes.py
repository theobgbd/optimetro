# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2
import numpy
import matplotlib.pyplot as plt


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(args["image"])
image = imutils.resize(image, width=800)
#ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
light_white 		= (0,0,100)
dark_white 	        = (50,50,255)
#water RBG(119, 176, 203)
light_water	= (90 , 90, 100)
dark_water  = (130, 150, 250)

hsv 			= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask_stations 	= cv2.inRange(hsv, light_white, dark_white)
mask_water	 	= cv2.inRange(hsv, light_water, dark_water)
image[mask_stations != 0] = [0,0,255]
image[mask_water    != 0] = [0,255,0]
cv2.imshow("frame", image)
cv2.waitKey(3014656)

#quit()
 
stations	= cv2.bitwise_and(resized, resized, mask=mask_stations)
water		= cv2.bitwise_and(resized, resized, mask=mask_water)
plt.subplot(1, 4, 1)
plt.imshow(mask_stations, cmap="gray")
plt.subplot(1, 4, 2)
plt.imshow(stations, cmap="gray")
#
plt.subplot(1, 4, 3)
plt.imshow(mask_water, cmap="gray")
plt.subplot(1, 4, 4)
plt.imshow(water, cmap="gray")
plt.show()
#gray 		= cv2.cvtColor(stations, cv2.COLOR_HSV2GRAY)
#blurred 	= cv2.GaussianBlur(stations, (5, 5), 0)
#thresh  	= cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]



# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

# loop over the contours
for c in cnts:
	# compute the center of the contour, then detect the name of the
	# shape using only the contour
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	shape = sd.detect(c)

	# multiply the contour (x, y)-coordinates by the resize ratio,
	# then draw the contours and the name of the shape on the image
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (255, 255, 255), 2)

	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)
