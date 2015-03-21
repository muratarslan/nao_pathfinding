import sys
import os
import time
from gi.repository import Gtk
from naoqi import ALProxy

import config as c

tts     = ALProxy("ALTextToSpeech", c.IP, c.PORT)
motion  = ALProxy("ALMotion", c.IP, c.PORT)
posture = ALProxy("ALRobotPosture", c.IP, c.PORT)
photo   = ALProxy("ALPhotoCapture", c.IP, c.PORT)


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

        def naoSay(self, widget):
            tts.say(self.speechbox.get_text())
            print "Say: %s" % self.speechbox.get_text()

        def destroy(self, widget):
            print "destroyed"
            Gtk.main_quit()

        def keyPressed(self, widget, event):
            key_code = event.get_keycode()[1]
            print "keyPressed: %s" % key_code 

        def keyReleased(self, widget, event):
            key_code = event.get_keycode()[1]
            print "keyReleased: %s" % key_code
