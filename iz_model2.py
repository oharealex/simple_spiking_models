# Izhikevich 2003 Spiking Neuron Model
# Created by Alex O'Hare (from source material), 27/05/2024

# Import the required libraries
import matplotlib.pyplot as plt
import numpy as np
import random
import timeit
import time

# Define constant and variabs
C = 100
vr = -65
vt = -60
v = vr
u = 0	
I = 0	
k = 0.7
a = 0.11
b = -2
c = -75
d = 100
vpeak = 40

# Define the differential equations

def dvdt(v, u, I):
	return (1/C) * ((k * (v - vr) * (v - vt)) - u + I)

def dudt(v, u):
	return a * ((b * (v - vr)) - u)

spi = 1000000
spike_ran = range(0, spi, 5000)
spike_his = np.zeros(len(spike_ran))
for idx, spike in enumerate(spike_ran):
	print(spike)
	#num_spikes = 10000
	T = spike * 50
	dt = 1
	t = 0
	v_his = []
	u_his = []
	t_his = []

	start_time = time.perf_counter()
	while t < T:
		if t <= 100:
			I = 0
		else:
			I = 70
		v += dvdt(v, u, I) * dt
		u += dudt(v, u) * dt
		if v >= vpeak:
			v = vpeak
			v_his.append(v)
			u_his.append(u)
			t_his.append(t)
			v = c
			u += d
			
		else:
			v_his.append(v)
			u_his.append(u)
			t_his.append(t)
		
		t += dt
		#print(t)
	end_time = time.perf_counter()
	elapsed_time = end_time - start_time
	spike_his[idx] = elapsed_time
np.save("iz_spikes", spike_his)
plt.plot(spike_ran, spike_his)
plt.show()
#print("simulation time: " + str(elapsed_time))
#plt.figure(figsize = (12, 4))
#plt.plot(t_his, v_his, color = "black", linewidth = 0.9)
#plt.xlabel("t [ms]")
#plt.ylabel("V(t) [mV]")
##plt.plot(t_his, u_his, color = "red")
#plt.show()
