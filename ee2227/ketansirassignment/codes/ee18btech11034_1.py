import control
import matplotlib.pyplot as plt

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
#Each subplot K = 1.25,2,1 respectively

plt.subplot(3,1,1)
plt.title('For K=1.25')
control.nyquist(G1)
plt.grid(True)
plt.xlim(-4,0)
plt.ylim(-2,2)
plt.ylabel('Im(s)')

plt.subplot(3,1,2)
control.nyquist(G2)
plt.grid(True)
plt.xlim(-4,0)
plt.ylim(-2,2)
plt.title('For K=2')
plt.ylabel('Im(s)')

plt.subplot(3,1,3)
control.nyquist(G3)
plt.grid(True)
plt.title('For K=1')
plt.xlim(-4,0)
plt.ylim(-2,2)
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
#if using termux
#plt.savefig('./figs/ee18btech11034/ee18btech11034_1.pdf')
plt.savefig('./figs/ee18btech11034_1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11034/ee18btech11034_1.pdf"))
#else
plt.show()


