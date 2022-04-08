import sys
import datetime

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont, QPainter, QBrush, QPen
from PyQt5 import QtCore

from ping3 import ping
    
app = QApplication(sys.argv) # Initializing GUI

target = '10.2.144.139' # IP address that will be pung
interval = 500 # Interval that IP will be pung in milliseconds
width = 220 # Fixed width of the window
height = 100 # Fixed height of the window

window = QWidget()
window.setWindowTitle('PiPing')
window.setFixedSize(width, height)

pingLabel = QLabel("", parent=window)
hostLabel = QLabel("", parent=window)
intervalLabel = QLabel("", parent=window)
colorLabel = QLabel("", parent=window)

pingLabel.setGeometry(10, 5, 125, 35)
hostLabel.setGeometry(10, 45, 220, 20)
intervalLabel.setGeometry(10, 70, 220, 20)
colorLabel.setGeometry(165, 5, 50, 50)

hostLabel.setText("target: " + target)
intervalLabel.setText("interval: " + str(interval) + "ms")
colorLabel.setStyleSheet("background:gray")

window.show()

def pingUpdate():

    ms = round(ping(target) * 1000)
    msStr = str(ms)
    if msStr == "None": 
        pingLabel.setText("Destination Unreachable")
        print("Destination Unreachable")
        pingLabel.setFont(QFont('Arial', 12))
    else:
        pingLabel.setText(msStr + "ms")
        print(msStr)
        pingLabel.setFont(QFont('Arial', 20))

    if ms < 75:
        colorLabel.setStyleSheet("background:lime")
    elif ms < 150:
        colorLabel.setStyleSheet("background:yellow")
    else:
        colorLabel.setStyleSheet("background:red")

timer = QtCore.QTimer()
timer.timeout.connect(pingUpdate)
timer.start(interval)

sys.exit(app.exec_())
