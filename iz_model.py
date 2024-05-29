# Izhikevich 2003 Spiking Neuron Model
# Created by Alex O'Hare (from source material), 27/05/2024

# Import the required libraries
import matplotlib.pyplot as plt
import numpy as np
import random
import time

time_list = range(1, 10000, 200)
time_hist = np.zeros(len(time_list))
for idx, spikes in enumerate(time_list):
	start_time = time.perf_counter()
	# Define constant and variabs
	C = 100
	vr = -65
	vt = -60
	v = vr
	u = 0	
	I = 0	
	k = 0.7
	a = 0.045
	b = -2
	c = -75
	d = 100
	vpeak = 40

	# Define the differential equations

	def dvdt(v, u, I):
		return (1/C) * ((k * (v - vr) * (v - vt)) - u + I)

	def dudt(v, u):
		return a * ((b * (v - vr)) - u)

	T = spikes
	dt = 1	
	t = 0
	v_his = []
	u_his = []
	t_his = []


	while t < T:
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
	end_time = time.perf_counter()
	time_taken = end_time - start_time
	time_hist[idx] = time_taken

plt.plot(time_list, time_hist)
plt.show()
np.save("iz_spike_times", time_hist)	z
#	plt.figure(figsize = (12, 4))
#	plt.plot(t_his, v_his, color = "black", linewidth = 0.9)
#	plt.xlabel("t [ms]")
#	plt.ylabel("V(t) [mV]")
#	#plt.axhline(-65, color = "black", linestyle = "--", linewidth = 0.9)
#	#plt.plot(t_his, u_his, color = "red")
#	plt.show()
