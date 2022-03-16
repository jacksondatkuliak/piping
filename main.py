import sys
import datetime

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore

from ping3 import ping
    
app = QApplication(sys.argv) # Initializing GUI

window = QWidget()
window.setWindowTitle('PiPing')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel("", parent=window)
helloMsg.move(60, 15)
window.show()

def pingUpdate():
    ms = str(ping('10.2.144.208'))
    helloMsg.setText(ms)
    print(ms)

timer = QtCore.QTimer()
timer.timeout.connect(pingUpdate)    # helloMsg.setText(str(ping('10.2.144.207')))
timer.start(1000)

sys.exit(app.exec_())
