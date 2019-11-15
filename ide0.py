import serial
import numpy as np
import random
import time

buffers = []
numstr = []
pointer = 0
datalog = np.array([])
ser = serial.Serial('/dev/rfcomm0',9600)
while(1):
	pointer += 1
	s = ser.readline()
	sd = s.decode("utf-8")
	buffers.append(sd)
	y = len(sd)
	numstr = int(sd[0:y-2])
	print(numstr) 
	datalog = np.append(datalog,numstr)
ser.close()