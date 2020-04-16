import control
import matplotlib.pyplot as plt

num = [-1,1]
den = [2,4]

#Creating a transfer function G = num/den
G = control.tf(num,den) 

control.nyquist(G)
#plotting the nyquist plot
plt.grid(True)
plt.title('Nyquist Diagram of G(s)')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.show()
