import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from playsound import playsound


def readserial(i):
    global index
    global serialList
    global xAxis
    serialList.append(int(s.read()))
    xAxis.append(index)
    plt.cla()
    plt.plot(xAxis, serialList)
    index += 1


dataFile = open("learning_data.txt", 'a')

while True:
    run = int(input("1 : Continue\n2 : End Code\nAction: "))
    if run == 2:
        break
    time.sleep(5)
    playsound(
        "C:/Ayush/Personal/Coding/Github/Burgalary-Vibration-Alarm/Ding_Sound_Effect.mp3")

    serialList = []
    xAxis = []
    index = 0
    s = serial.Serial("COM3", 9600)

    anim = FuncAnimation(plt.gcf(), readserial, interval=1, frames=150, repeat=False)
    plt.show()
    s.close()
    playsound(
        "C:/Ayush/Personal/Coding/Github/Burgalary-Vibration-Alarm/Ding_Sound_Effect.mp3")

    print("Type of graph: ")
    print("1 : Walking towards")
    print("2 : Walking away")
    print("3 : Not walking")
    print("4 : Delete Entry")
    print("5 : End Code")
    dataType = int(input("\nEnter type: "))

    if dataType == 1:
        dataStoreType = "T"
    elif dataType == 2:
        dataStoreType = "A"
    elif dataType == 3:
        dataStoreType = "N"
    elif dataType == 4:
        continue
    elif dataType == 5:
        break
    else:
        print("Invalid statement, entry deleted")
        continue

    for i in serialList:
        dataFile.write(str(i) + ", ")
    dataFile.write(dataStoreType + "\n")

dataFile.close()
