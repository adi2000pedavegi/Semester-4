import control
import matplotlib.pyplot as plt
import numpy as np
#if using termux
import subprocess
import shlex
#end if

#coefficents of open loop transfer function
den = [4,5,1,0]
num1 = [1.25]
num2 = [2]
num3 = [1]

#Creating a transfer function G = num/den
G1 = control.tf(num1,den) 
G2 = control.tf(num2,den)
G3 = control.tf(num3,den)

#plotting the nyquist plot for three different transfer functions for a variable K


control.nyquist(G1,label='K=1.25')
control.nyquist(G2,label='K=2')
control.nyquist(G3,label='K=1')
plt.xlim(-4,0)
plt.ylim(-2,2)
plt.legend()
plt.annotate("-1+0j",(-1,0))
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
#if using termux
plt.savefig('./figs/ee18btech11034/ee18btech11034_1.pdf')
plt.savefig('./figs/ee18btech11034/ee18btech11034_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11034/ee18btech11034_1.pdf"))
#else
#plt.show()


