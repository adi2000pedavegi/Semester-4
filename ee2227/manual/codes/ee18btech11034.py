#Code by P.Aditya
#April 18th,2020
#Released under GNU GPL

import control
import matplotlib.pyplot as plt
import subprocess
import shlex


num = [-1,1]  #numerator coefficients of G(s)
den = [2,4]	  #denominator coefficients of G(s)

#Creating a transfer function G = num/den
G = control.tf(num,den) 

control.nyquist(G)
#plotting the nyquist plot
plt.grid(True)
plt.title('Nyquist Diagram of G(s)')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.savefig('./figs/ee18btech11034.eps')
#plt.show()
