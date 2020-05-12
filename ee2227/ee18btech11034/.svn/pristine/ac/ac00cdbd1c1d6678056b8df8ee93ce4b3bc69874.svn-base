#Code by P.ADITYA
#Date 11th May,2020

import numpy as np  
import matplotlib.pyplot as plt


#if using termux
import subprocess
import shlex
#end if

data=np.loadtxt('ee18btech11034.dat')  
plt.plot(data[:,0],data[:,1])  
plt.grid()
plt.xlabel("time")
plt.ylabel("Closed loop system magnitude response")
plt.title('Spice simulation')

#if using termux
plt.savefig('./figs/ee18btech11034/ee18btech11034_spice_result.pdf')
plt.savefig('./figs/ee18btech11034/ee18btech11034_spice_result.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11034/ee18btech11034_spice_result.pdf"))
#else
#plt.show()
