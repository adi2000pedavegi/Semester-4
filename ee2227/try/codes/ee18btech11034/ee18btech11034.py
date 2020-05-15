#Code by P.ADITYA
#May 8th,2020
#Released under GNU GPL

import numpy as np
import math

#Solving f for part 1 question
a = np.roots([1/1e10,0,(1/100)+(1/1e8),0,1-(1e6)])   #Solving bi-quadratic equation
a = a.real
for i in range(len(a)):
	if(a[i]>0):
		freq1 = a[i]
		
print('The gain cross-over frequency where |GH|=1 in Hz is',freq1)
#Solving phase for part 1 question
phi1 = -math.atan(freq1/10)-math.atan(freq1/1e4)
print('The phase for f at |GH|=1 in degree is',phi1*180/(np.pi))

#Solving f for part 2 question
b = np.roots([1/1e5,-(0.1+(1/1e4)),-1])   #Solving quadratic equation
b = b.real
for i in range(len(b)):
	if(b[i]>0):
		freq2 = b[i]
print('The frequency where phase margin of GH is 45 degrees in Hz is',freq2) 
#Solving H for part 2 question
H = (np.sqrt(2)/1e5)*(np.sqrt(1+1e6))
print('The feedback gain H for phase margin 45 degrees is',H)
