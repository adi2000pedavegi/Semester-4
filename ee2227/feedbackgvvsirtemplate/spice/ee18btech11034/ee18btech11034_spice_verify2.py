#Code by P.Aditya
#19th may,2020
#Released under GNU GPL

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import control

#if using termux
import subprocess
import shlex
#end if

p1 = 2*np.pi*10
p2 = 2*np.pi*1e4
R1 = 10
R2 = 700
H = (R1)/(R1+R2)

num = [1e5]		#describing transfer function
den = [(1/(p1*p2)),((1/p1)+(1/p2)),(1e5*H)+1]
closedlooptf = control.TransferFunction(num,den)

T = np.linspace(0,1e-3,1000)
T,yout = control.step_response(closedlooptf,T)	
plt.plot(T,yout)
plt.grid()
plt.xlabel("time (t)")
plt.ylabel("Closed loop system step response")
plt.title("Step response for $PM=45$ degrees")


#if using termux
plt.savefig('./figs/ee18btech11034/ee18btech11034_spice_verify2.pdf')
plt.savefig('./figs/ee18btech11034/ee18btech11034_spice_verify2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11034/ee18btech11034_spice_verify2.pdf"))
#else
#plt.show()
