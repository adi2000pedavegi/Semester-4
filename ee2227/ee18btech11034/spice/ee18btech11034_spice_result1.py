#Code by P.ADITYA
#Date 12th May,2020

import numpy as np  
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11034_1.dat')  
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("Closed loop system magnitude response for $PM=51$")
plt.title('Spice simulation')


#if using termux
plt.savefig('./figs/ee18btech11034/ee18btech11034_spice_result1.pdf')
plt.savefig('./figs/ee18btech11034/ee18btech11034_spice_result1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11034/ee18btech11034_spice_result1.pdf"))
#else
#plt.show()
