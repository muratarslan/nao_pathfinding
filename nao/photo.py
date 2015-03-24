# Image Library
import Image
import cv
import cv2
import os
from naoqi import ALProxy
import numpy as np
import config as c


image = "image.png"

# def showImage():

# 	# Setting up proxy
# 	cameraProxy = ALProxy("ALVideoDevice", c.IP, c.PORT)
# 	# Camera ID
# 	cameraProxy.kCameraSelectID = c.CAMERAID
# 	# Camera Parameters
# 	cameraProxy.setParam(cameraProxy.kCameraSelectID,c.CAMERAID)
# 	# Subscribe Camera Proxy
# 	videoClient = cameraProxy.subscribe("python_client", c.RESOLUTION, c.COLORSPACE, 5)
	
# 	naoImage = cameraProxy.getImageRemote(videoClient)

# 	imageWidth  = naoImage[0]
# 	imageHeight = naoImage[1]
# 	array       = naoImage[6]

# 	# Create a PIL Image from our pixel array.
# 	im = Image.fromstring("RGB", (imageWidth, imageHeight), array)

# 	# Create a BGR Numpy pixel array from camera image
# 	img = np.array(im)

# 	# # Convert BGR to GRAY
# 	#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 	cv2.imshow('image',img)
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()


def takePhoto():

  # Setting up proxy
  cameraProxy = ALProxy("ALVideoDevice", c.IP, c.PORT)

  # Camera ID
  cameraProxy.kCameraSelectID = c.CAMERAID

  # Camera Parameters
  cameraProxy.setParam(cameraProxy.kCameraSelectID,c.CAMERAID)

  # Subscribe Camera Proxy
  videoClient = cameraProxy.subscribe("python_client", c.RESOLUTION, c.COLORSPACE, 5)

  # image[6] contains ASCII
  naoImage = cameraProxy.getImageRemote(videoClient)

  # Unsubscribe Camera Proxy
  cameraProxy.unsubscribe(videoClient)

  # Image Size and Pixel Array
  imageWidth  = naoImage[0]
  imageHeight = naoImage[1]
  imageArray  = naoImage[6]

  # Create an Image
  im = Image.fromstring("RGB", (imageWidth, imageHeight), imageArray)
  img = np.array(im)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

  # Save image.
  cv2.imwrite('image.png',thresh)

  # Show image
  #cv2.imshow('Image',thresh)
  print "Photo Taken..."

def cropImage():
    img = cv2.imread(image)
    i = 0
    if os.path.isdir('dataset') == False:
        os.mkdir('dataset')  # Create a folder
        os.chdir('dataset')  # Change directory
    else:
        os.chdir('dataset2')  # Change directory
    for v in range(0, 640, 20):
        for c in range (0, 480, 20):
            crop_img = img[c:20+c, v:20+v] # Crop from x, y, w, h 
            #cv2.imshow("cropped", crop_img)
            cv2.imwrite(str(i) + '.png', crop_img)
            i += 1
    print "Image Cropped and dataset created..."


if __name__ == '__main__':
  showImage()
  

