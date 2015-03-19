# Image Library
import Image
import cv
from naoqi import ALProxy


def showImage(IP, PORT,cameraId):
  cameraProxy = ALProxy("ALVideoDevice", IP, PORT)
  cameraProxy.kCameraSelectID=18
  cameraProxy.setParam(cameraProxy.kCameraSelectID,cameraId)

  
  resolution =  2   # Image Size
  colorSpace = 11   # Select RGB

  videoClient = cameraProxy.subscribe("python_client", resolution, colorSpace, 5)

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
  IP = "10.51.5.167"  # Nao IP Address
  PORT = 9559
  showImage(IP, PORT,18)


