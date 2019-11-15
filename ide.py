import serial
import numpy as np
import random
import time
buffers = []
pointer = 0
word = ""
data = np.array([])
ser = serial.Serial('/dev/rfcomm0',9600)
while(1):
	k = len(buffers)
	if len(buffers) == 3:
		word = buffers[0] + buffers[1] + buffers[2]	
		print(word)
		dig = int(word)
		data = np.append(data,dig)
	if len(buffers) > 3 & (len(buffers)%5) == 3:
		word = buffers[k-3] + buffers[k-2] + buffers[k-1]
		print(word)	
		dig = int(word)
		data = np.append(data,dig)
	s = ser.read()
	sd = s.decode("utf-8")
	buffers.append(sd)
	#if len(data) == 20:
	#	print(data)
	#	break
	#print(s)
ser.close()