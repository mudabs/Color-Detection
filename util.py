import numpy as np
import cv2

#in this example, we will detect a specific color in an image using OpenCV.
#color detection is useful in various applications such as object tracking, image segmentation, and computer vision tasks.
#we will use the HSV color space for better color segmentation because it separates color information (hue) from intensity (value).
def get_limits(color):

    c = np.uint8([[color]])  # create a 1x1 pixel image with the given color
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) # convert bgr to hsv and assign to hsvC

    loweLimit = hsvC[0][0][0] - 10, 100, 100 # define lower limit for color detection in this case that is red 
    upperLimit = hsvC[0][0][0] + 10, 255, 255 # define upper limit for color detection in this case that is red

    lowerLimit = np.array(loweLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit