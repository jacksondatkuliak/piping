import sys
import datetime

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont
from PyQt5 import QtCore

from ping3 import ping
    
app = QApplication(sys.argv) # Initializing GUI

target = '10.2.144.139' # IP address that will be pung

window = QWidget()
window.setWindowTitle('PiPing')
window.setGeometry(0, 0, 220, 80)
pingLabel = QLabel("", parent=window)
hostLabel = QLabel("", parent=window)

pingLabel.setGeometry(10, 5, 220, 35)
hostLabel.setGeometry(10, 45, 220, 35)

hostLabel.setText("target: " + target)

window.show()

def pingUpdate():
    ms = str(round(ping(target) * 1000))
    if ms == "None": 
        pingLabel.setText("Destination Unreachable")
        print("Destination Unreachable")
        pingLabel.setFont(QFont('Arial', 12))
    else:
        pingLabel.setText(ms + "ms")
        print(ms)
        pingLabel.setFont(QFont('Arial', 20))

timer = QtCore.QTimer()
timer.timeout.connect(pingUpdate)
timer.start(1000)

sys.exit(app.exec_())
