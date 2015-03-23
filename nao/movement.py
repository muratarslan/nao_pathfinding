import sys
import os
import time
from gi.repository import Gtk
from naoqi import ALProxy

import config as c

tts        = ALProxy("ALTextToSpeech", c.IP, c.PORT)
motion     = ALProxy("ALMotion", c.IP, c.PORT)
posture    = ALProxy("ALRobotPosture", c.IP, c.PORT)
photo      = ALProxy("ALPhotoCapture", c.IP, c.PORT)
#navigation = ALProxy("ALNavigation", c.IP, c.PORT)

headposition = 0
protection   = 0


class NaoController:
        
        """Represents Nao Controller GUI

        params: glade_file_path - path:string
        """
	def __init__(self, glade_file_path=c.GLADE_FILE_PATH):
            self.glade_file_path = glade_file_path
            
            # Gtk Builder Init
            self.builder = Gtk.Builder()
            self.builder.add_from_file(self.glade_file_path)
            self.builder.connect_signals(self)

            # Add UI Components
            self.window = self.builder.get_object("naoControllerWindow")
            self.speechbox = self.builder.get_object("speechbox")

            # Show UI
            self.window.show_all()
   
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
    
        
        def naoSay(self, widget):
            tts.say(self.speechbox.get_text())
            print "Say: %s" % self.speechbox.get_text()

        def destroy(self, widget):
            print "destroyed"
            Gtk.main_quit()

            ## Key Pressed Event to control Nao remotely
        def keyPressed(self, widget, event):
            global headposition
            global protection

            key_code = event.get_keycode()[1]
            if key_code == 33:  # P Protection On / Off
                    if protection == 0:
                            motion.setExternalCollisionProtectionEnabled( "All", False )
                            protection = 1
                            print "Protection Off"
                    else:
                            motion.setExternalCollisionProtectionEnabled( "All", True )
                            protection = 0
                            print "Protection On"
            if key_code == 111:  # UP Nao Forward
                    print "Moving Forward..."
                    motion.moveInit()
                    motion.walkTo(0.1, 0, 0)
            if key_code == 116: # Down Nao Backward
                    print "Moving Backward..."
                    motion.moveInit()
                    motion.moveTo(-0.1, 0, 0)
            if key_code == 113: # Left Nao Left
                    print "Moving Left..."
                    motion.moveInit()
                    motion.moveTo(0, 0.1, 0)
            if key_code == 114: # Right Nao Right
                    print "Moving Right..."
                    motion.moveInit()
                    motion.moveTo(0, -0.1, 0)
            if key_code == 38: # a Turn Left
                    print "Turning Left..."
                    motion.moveInit()
                    motion.moveTo(0, 0, 1)
            if key_code == 40: # d Turn Right
                    print "Turning Right..."
                    motion.moveInit()
                    motion.moveTo(0, 0, -1)
            if key_code == 25: # w Head Down
                    headposition = headposition + 0.1
                    motion.angleInterpolation("HeadPitch", headposition, 0.5, True)
                    if headposition > 0.5:
                            headposition = 0.5
                    print "Head Position: %s" % headposition
            if key_code == 39: # s Head UP
                    headposition = headposition - 0.1
                    motion.angleInterpolation("HeadPitch", headposition, 0.5, True)
                    if headposition < -0.5:
                            headposition = -0.5
                    print "Head Position: %s" % headposition

            #print "keyPressed: %s" % key_code 

        def keyReleased(self, widget, event):
            key_code = event.get_keycode()[1]
            #print "keyReleased: %s" % key_code
