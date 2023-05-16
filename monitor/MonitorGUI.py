from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
from .ConnectionDock import ConnectionDock
from .RoomDook import RoomDook
from utils.Mqtt_client import Mqtt_client

rooms = []

def on_message(msg):
    try:
        jsonString=str(msg.payload.decode("utf-8","ignore"))
        jsn = json.loads(jsonString) 
        room = rooms[jsn["room"] - 1]
        newValue = int(room.counter.text()) + jsn["action"]
        if newValue < 0:
            newValue = 0
        room.counter.setText(str(newValue))
    except Exception as e:
        print(e)


class MonitorGUI(QMainWindow):
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
                
        # Init of Mqtt_client class
        self.mc=Mqtt_client(subscribe=True, on_message = lambda client,userdata,msg: on_message(msg))

        # general GUI settings
        self.setUnifiedTitleAndToolBarOnMac(True)

        # set up main window
        self.setGeometry(30, 100, 800, 400)
        self.setWindowTitle('Monitor GUI')        

        # Init QDockWidget objects        
        self.connectionDock = ConnectionDock(self.mc)    
    
        self.addDockWidget(Qt.LeftDockWidgetArea, self.connectionDock)
        for i in range(1,11):
            room = RoomDook(self.mc,i)
            rooms.append(room)
            if i <=5:
                self.addDockWidget(Qt.TopDockWidgetArea, room)
            else:
                self.addDockWidget(Qt.BottomDockWidgetArea, room )

        
