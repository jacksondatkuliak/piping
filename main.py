from ast import Or, Str
from operator import or_
from time import sleep
import sys
import datetime
from timeit import Timer
from subprocess import call
import os
from tkinter import Y
import math

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QFont, QPainter, QBrush, QPen
from PyQt5 import QtCore

from ping3 import ping
    
app = QApplication(sys.argv) # Initializing GUI



osType = "dos" # !!SET THIS CORRECT OR EVERYTHING WILL CRASH!! (Types: 'dos' for DOS systems, or 'lin' for everything else.)
targets = ['1.1.1.1', '8.8.8.8'] # IP addresses that will be pung - keep adding more addresses until the app is litteraly locked up...
interval = 500 # Interval that IP will be pung in milliseconds

targetCount = len(targets)

baseWidth = int(220) # Fixed width of a single cell
baseHeight = int(100) # Fixed height of a single cell
maxCellRows = 5 # Maximum rows before creating a new column

#if (targetCount % cellRows == 0):
width = baseWidth * (math.ceil(targetCount / maxCellRows))
#else:
#    width = baseWidth + (baseWidth * )

if (targetCount <= 5):
    height = baseHeight + (baseHeight * (targetCount - 1))
else:
    height = baseHeight + (baseHeight * (maxCellRows - 1))

width = int(width)
height = int(height)

window = QWidget()
window.setWindowTitle('PiPing')
window.setFixedSize(width, height)

pingLabel = [QLabel("", parent=window)] * targetCount
hostLabel = [QLabel("", parent=window)] * targetCount
intervalLabel = [QLabel("", parent=window)] * targetCount
colorLabel = [QLabel("", parent=window)] * targetCount
ms = [int] * targetCount
msStr = [Str] * targetCount



def clear():
    os.system('cls' if osType == 'dos' else 'clear')



def pingUpdate(i = 0, target = ""):
    pingTime = ping(target)
    
    if pingTime == None or False: 
        pingLabel[i].setText("Destination Unreachable")
        print("'"+ target + "': Destination Unreachable")
        pingLabel[i].setFont(QFont('Arial', 12))
    else:
        ms[i] = round(pingTime * 1000)
        msStr[i] = str(ms[i])
        pingLabel[i].setText(msStr[i] + "ms")
        print("'"+ target + "': " + msStr[i] + "ms")
        pingLabel[i].setFont(QFont('Arial', 20))

        if ms[i] < 75:
            colorLabel[i].setStyleSheet("background:lime")
        elif ms[i] < 150:
            colorLabel[i].setStyleSheet("background:yellow")
        else:
            colorLabel[i].setStyleSheet("background:red")

def refresh():
    i = 0
    clear()
    print("---------------------------------------------")
    for target in targets:
        pingUpdate(i, target)
        i = i + 1
    i = 0



i = 0
cellRowCount = 0
for target in targets:

    xOffset = baseWidth * (math.floor((i / maxCellRows)))

    if (cellRowCount <= (maxCellRows - 1)):
        yOffset = baseHeight * cellRowCount

    xOffset = int(xOffset)
    yOffset = int(yOffset)

    print("Making New Tile For Host: '" + target + "' " + "At: " + str(xOffset) + "x" + str(yOffset))

    pingLabel[i] = QLabel("", parent=window)
    hostLabel[i] = QLabel("", parent=window)
    intervalLabel[i] = QLabel("", parent=window)
    colorLabel[i] = QLabel("", parent=window)

    pingLabel[i].setGeometry(10 + xOffset, 5 + yOffset, 125, 35)
    hostLabel[i].setGeometry(10 + xOffset, 45 + yOffset, 220, 20)
    intervalLabel[i].setGeometry(10 + xOffset, 70 + yOffset, 220, 20)
    colorLabel[i].setGeometry(165 + xOffset, 5 + yOffset, 50, 50)

    hostLabel[i].setText("target: " + target)
    intervalLabel[i].setText("interval: " + str(interval) + "ms")
    colorLabel[i].setStyleSheet("background:gray")

    if (cellRowCount == (maxCellRows - 1)): # Reset Row Counter
        cellRowCount = 0
    else:
        cellRowCount = cellRowCount + 1 # Incriment Row Counter

    i = i + 1



window.show()


timer = QtCore.QTimer()
timer.timeout.connect(refresh)
timer.start(interval)

sys.exit(app.exec_())
