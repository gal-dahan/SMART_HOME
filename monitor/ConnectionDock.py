from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ConnectionDock(QDockWidget):
    def __init__(self,mc):
        QDockWidget.__init__(self)
        self.mc = mc
        self.mc.on_connected_action = self.on_connected
        self.eConnectbtn=QPushButton("Connect", self)
        self.eConnectbtn.setToolTip("click me to connect")
        self.eConnectbtn.clicked.connect(self.on_button_connect_click)
        self.eConnectbtn.setStyleSheet("background-color: red")
        
        formLayot=QFormLayout()
     
        formLayot.addRow("",self.eConnectbtn)

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
