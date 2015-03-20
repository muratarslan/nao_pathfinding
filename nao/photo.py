# Image Library
import Image
import cv
from naoqi import ALProxy
import config as c


def showImage():
  cameraProxy = ALProxy("ALVideoDevice", c.IP, c.PORT)
  cameraProxy.kCameraSelectID = c.CAMERAID
  cameraProxy.setParam(cameraProxy.kCameraSelectID,c.CAMERAID)

  videoClient = cameraProxy.subscribe("python_client", c.RESOLUTION, c.COLORSPACE, 5)

  # image[6] contains ASCII
  naoImage = cameraProxy.getImageRemote(videoClient)


  cameraProxy.unsubscribe(videoClient)



  # Image Size and Pixel Array
  imageWidth = naoImage[0]
  imageHeight = naoImage[1]
  imageArray = naoImage[6]

  # Create an Image
  im = Image.fromstring("RGB", (imageWidth, imageHeight), imageArray)


  # Save  image.
  im.save("Image.png", "PNG")

  im.show()



if __name__ == '__main__':
  showImage()


