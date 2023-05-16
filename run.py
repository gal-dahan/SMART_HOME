import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from sensor.Door import Door
from monitor.MonitorGUI import MonitorGUI
app = QApplication(sys.argv)
windows = []
for i in range(1,4):
    mainwin = Door(i)
    mainwin.show()
    windows.append(mainwin)

mainwin = MonitorGUI()
mainwin.show()
windows.append(mainwin)
app.exec_()

