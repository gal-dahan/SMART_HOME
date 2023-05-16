from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mqtt_init

class ConnectionDock(QDockWidget):
    """Main """
    def __init__(self,mc):
        QDockWidget.__init__(self)
        
        self.mc = mc
        self.mc.on_connected_action = self.on_connected
        
        self.eConnectbtn=QPushButton("Enable/Connect", self)
        self.eConnectbtn.setToolTip("click me to connect")
        self.eConnectbtn.clicked.connect(self.on_button_connect_click)
        self.eConnectbtn.setStyleSheet("background-color: gray")
        
        self.ePublisherTopic=QLineEdit()
        self.ePublisherTopic.setText(mqtt_init.topic)
        
        self.room_id=QLineEdit()
        self.room_id.setText('')

        formLayot=QFormLayout()       
        formLayot.addRow("Turn On/Off",self.eConnectbtn)
        formLayot.addRow("Pub topic",self.ePublisherTopic)
        formLayot.addRow("Room",self.room_id)

        widget = QWidget(self)
        widget.setLayout(formLayot)
        self.setTitleBarWidget(widget)
        self.setWidget(widget)     
        self.setWindowTitle("Connect") 
        
    def on_connected(self):
        self.eConnectbtn.setStyleSheet("background-color: green")
                    
    def on_button_connect_click(self):     
        self.mc.connect_to()        
        self.mc.start_listening()

    def push_button_click(self):
        self.mc.publish_to(self.ePublisherTopic.text(), '"value":1')
     