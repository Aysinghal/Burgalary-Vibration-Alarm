import serial
from record_data import readingSerial, codeRunning

s = serial.Serial("COM3", 9600)

while codeRunning:
    while not readingSerial:
        s.read()
