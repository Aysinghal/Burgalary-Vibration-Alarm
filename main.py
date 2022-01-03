import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


serialList = []
xAxis = []
index = 0
startTime = time.time()


def readserial(i):
    global index
    global serialList
    global xAxis
    global startTime
    serialList.append(int(s.read()))
    xAxis.append(index)
    plt.cla()
    plt.plot(xAxis, serialList)
    if index % 100 == 0:
        print(str(index) + ' - ' + str(time.time() - startTime))
        startTime = time.time()
    if index % 1000 == 0:
        serialList = []
        xAxis = []
    index += 1


s = serial.Serial("COM3", 9600)

anim = FuncAnimation(plt.gcf(), readserial, interval=1)

plt.show()
