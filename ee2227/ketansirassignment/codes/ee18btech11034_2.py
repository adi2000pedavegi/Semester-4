import control
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

#coefficents of open loop transfer function
den = [4,1,0,0]
num1 = [1]
num2 = [3]

#Creating a transfer function G = num/den
G1 = control.tf(num1,den) 
G2 = control.tf(num2,den)
#plotting the nyquist plot for three different transfer functions for a variable K
#Each subplot K = 1,3 respectively

plt.subplot(2,1,1)
plt.title('For K=1')
control.nyquist(G1)
plt.grid(True)
plt.xlim(-4,0)
plt.ylim(-2,2)
plt.ylabel('Im(s)')

plt.subplot(2,1,2)
control.nyquist(G2)
plt.grid(True)
plt.xlim(-4,0)
plt.ylim(-2,2)
plt.title('For K=3')
plt.ylabel('Im(s)')
plt.xlabel('Re(s)')
#if using termux
#plt.savefig('./figs/ee18btech11034/ee18btech11034_2.pdf')
plt.savefig('./figs/ee18btech11034_2.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11034/ee18btech11034_2.pdf"))
#else
plt.show()


