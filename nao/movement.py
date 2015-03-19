import sys
import os
import time
from gi.repository import Gtk
from naoqi import ALProxy


IP = "10.51.5.167"
PORT = 9559


try:
	tts         = ALProxy("ALTextToSpeech", IP, PORT)
	motion  = ALProxy("ALMotion", IP, PORT)
	posture = ALProxy("ALRobotPosture", IP, PORT)
	photo    = ALProxy("ALPhotoCapture", IP, PORT)
except Exception, e:
	print "Error"
	print str(e)
	exit(1)


class NaoController:

	def __init__(self):
            pass

#### Nao Posture Functions
	def naoStandInit(self, widget):
	    posture.goToPosture("StandInit", 1.0)
            print "Stand Init"

	def naoRelax(self, widget):
	    posture.goToPosture("SitRelax", 1.0)
            print "Sit Relax"

	def naoZero(self, widget):
	    posture.goToPosture("StandZero", 1.0)
            print "Stand Zero"

	def naoBelly(self, widget):
	    posture.goToPosture("LyingBelly", 1.0)
            print "Lying Belly"
	
	def naoBack(self, widget):
	    posture.goToPosture("LyingBack", 1.0)
            print "Lying Back"

	def naoStand(self, widget):
	    posture.goToPosture("Stand", 1.0)
            print "Stand"

	def naoCrouch(self, widget):
	    posture.goToPosture("Crouch", 1.0)
            print "Crouch"

	def naoSit(self, widget):
	    posture.goToPosture("Sit", 1.0)
            print "Sit"




#### Nao Motion Functions
	def naoEnough(self, widget):
	    motion.moveInit()
            motion.post.wakeUp()
	    tts.say("Enough")	
            print "WakeUp"

	def naoCharge(self, widget):
	    motion.moveInit()
            motion.post.rest() 
	    tts.say("Charge me")
	    print "Rest"
    
        def naoForward(self, widget):
	    motion.moveInit()
            motion.walkTo(10, 0, 0)
	    print "Forward"

	def naoBackward(self, widget):
	    motion.moveInit()
            motion.moveTo(-10, 0, 0)
            print "Backward"

	def naoLeft(self, widget):
	    motion.moveInit()
            motion.moveTo(0, 10, 0)
            print "Left"

	def naoRight(self, widget):
	    motion.moveInit()
            motion.moveTo(0, -10, 0)
            print "Right"

	def naoPhoto(self, widget):
	    photo.setResolution(1)
	    photo.setPictureFormat("jpg")
            photo.takePictures(3,"/tmp/nao", "image")
            print "Taking Photo"

        def naoSay(self, widget):
            tts.say(entry.get_text())
            print entry.get_text()

        def destroy(self, widget):
            print "destroyed"
            Gtk.main_quit()



