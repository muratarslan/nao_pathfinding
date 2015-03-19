#!/usr/bin/env python

import sys
import os
import time
from gi.repository import Gtk
from naoqi import ALProxy
import movement


behavior = movement.NaoController()



builder = Gtk.Builder()
gladefile = "/home/murat/Desktop/nao/nao.glade"  
builder.add_from_file(gladefile)
window = builder.get_object("naoControllerWindow")
entry = builder.get_object('entry1')
		
if __name__ == "__main__":
	hwg = behavior
        window.show_all()
        builder.connect_signals(hwg)
	Gtk.main()

