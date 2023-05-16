import sys
import random
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .ConnectionDock import ConnectionDock
from utils.Mqtt_client import Mqtt_client
import mqtt_init

# Creating Client name - should be unique 

update_rate = 5000 # in msec

class Door(QMainWindow):
    
    def __init__(self,room_id, parent=None ):
        QMainWindow.__init__(self, parent)
                
        # Init of Mqtt_client class
        self.mc=Mqtt_client()
        r=random.randrange(1,10000000)
        clientname="IOT_client-Id-"+str(r)
        self.clientName = clientname
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(update_rate) # in msec
        self.room_id = room_id

        # general GUI settings
        self.setUnifiedTitleAndToolBarOnMac(True)

        # set up main window
        self.setGeometry(30, 600, 300, 200)
        self.setWindowTitle('Room Sensor')        

        # Init QDockWidget objects        
        self.connectionDock = ConnectionDock(self.mc)        
        self.connectionDock.room_id.setText(str(room_id))

        self.addDockWidget(Qt.TopDockWidgetArea, self.connectionDock)        

    def update_data(self):
        actions = [-1,1]
        Action = actions[random.randrange(0,2)]
        current_data = '{"room": ' + str(self.room_id) + ',"action": ' + str(Action) + "}" # 1 for in 2 for out
        self.mc.publish_to(mqtt_init.topic,current_data)

        


                   