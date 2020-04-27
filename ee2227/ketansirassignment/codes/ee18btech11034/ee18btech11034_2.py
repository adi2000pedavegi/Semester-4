import control
import matplotlib.pyplot as plt
import numpy as np
#if using termux
import subprocess
import shlex
#end if

#coefficents of open loop transfer function
den = [4,1,0,0]
num1 = [1]
num2 = [2]


#Creating a transfer function G = num/den
G1 = control.tf(num1,den) 
G2 = control.tf(num2,den)

#plotting the nyquist plot for three different transfer functions for a variable K


control.nyquist(G1,label='K=1')
control.nyquist(G2,label='K=2')
plt.xlim(-4,0)
plt.ylim(-2,2)
plt.legend()
plt.annotate("-1+0j",(-1,0))
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
#if using termux
plt.savefig('./figs/ee18btech11034/ee18btech11034_2.pdf')
plt.savefig('./figs/ee18btech11034/ee18btech11034_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11034/ee18btech11034_2.pdf"))
#else
#plt.show()


