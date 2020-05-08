#Code by P.ADITYA
#May 8th,2020
#Released under GNU GPL
 
import numpy as np
import math
from scipy import signal
import control
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

H = 0.01 #setting the value of H for required phase margin
num = [4e10*((np.pi)**2)*H]
den = [1,6.28*(10+1e4),4e5*((np.pi)**2)]
G = signal.lti(num,den)
w, mag, phase = signal.bode(G,w=np.linspace(1,1e5,100000))
sys = control.tf(num, den)
gm, pm, wpc, wgc = control.margin(sys)

print('Phase Margin in degrees:', pm)
print('Gain cross-over frequency in rad/sec:', wgc)

#Magnitude plot
plt.subplot(2, 1, 1) 
plt.semilogx(w, mag,'g') 
plt.plot(wgc, 0, 'o')
plt.text(49404,0, '({}, {})'.format(49404,0))
plt.ylabel("20$log_{10}(|G(j\omega)|$")
plt.title("Magnitude Plot")
plt.grid()

# Phase plot
plt.subplot(2, 1, 2) 
plt.semilogx(w, phase,'r')  
plt.plot(wgc, pm-180, 'o')
plt.text(49404,-128.1, '({}, {})'.format(49404,-128.1))
plt.xlabel("$\omega$ in rad/s")
plt.ylabel("$\phi(j\omega)$")
plt.title("Phase Plot")
plt.grid()


#if using termux
plt.savefig('./figs/ee18btech11034/ee18btech11034_1.pdf')
plt.savefig('./figs/ee18btech11034/ee18btech11034_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11034/ee18btech11034_1.pdf"))
#else
#plt.show()
