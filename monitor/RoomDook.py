from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RoomDook(QDockWidget):
    def __init__(self,mc,room_id):
        QDockWidget.__init__(self)
        self.mc = mc        
        self.room_id = room_id

        self.counter=QLabel()  
        self.counter.setText("0") 
        formLayot=QFormLayout()               
        formLayot.addRow("counter",self.counter)
            
        widget = QWidget(self)
        widget.setLayout(formLayot)
        self.setWidget(widget) 
        self.setWindowTitle(f"Room {room_id}")         
       
        