# Integrate-and-Fire model
# Alex O'Hare, 27/05/2024

# Import the required libraries
import matplotlib.pyplot as plt
import numpy as np
import random

# Define the variables and constants
v = -65
b = -65
E_threshold = -60
E_K = -75
t = 0
dt = 0.0001

# Define the differential equations
def dvdt(b, v):
	return b - v

# Data storage for plotting
v_his = []
b_his = []
t_his = []

while t < 100:
	if 0 < t < 100:
		v += dvdt(b, v) * dt + random.uniform(0,1)
		if v >= E_threshold:
			v = 40
			v_his.append(v)
			t_his.append(t)
			v = E_K
			t += 2
		else:
			v_his.append(v)
			t_his.append(t)
			t += dt
	else:	
		v = -65
		v_his.append(v)
		t_his.append(t)
		t += dt
	

plt.figure(figsize = (12, 4))
plt.plot(t_his, v_his, color = "black", linewidth = 0.9)
plt.xlabel("t [ms]")
plt.ylabel("V(t) [mV]")
plt.axhline(-60, linestyle = "--", color = "black", linewidth = 0.9)
plt.axhline(-65, linestyle = "--", color = "black", linewidth = 0.9)
plt.axhline(-75, linestyle = "--", color = "black", linewidth = 0.9)
plt.text(107, -60, r"$E_{threshold}$")
plt.text(107, -65, r"$E_{rest}$")
plt.text(107, -75, r"$E_K$")

#plt.ylim(-80, 50)
plt.show()
