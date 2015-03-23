# Image Library
import Image
import cv
from naoqi import ALProxy
import config as c


def showImage():
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
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  imageArray = naoImage[6]

  # Create an Image
  im = Image.fromstring("RGB", (imageWidth, imageHeight), imageArray)

  # Save  image.
  im.save("Image.png", "PNG")

  # Show image
  im.show()



if __name__ == '__main__':
  showImage()
  
