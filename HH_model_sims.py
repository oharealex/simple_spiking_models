# Import the required libraries

import matplotlib.pyplot as plt
import numpy as np
import random as ran
import math
import time

time_list = range(1, 10000, 200)
time_hist = np.zeros(len(time_list))
for idx, spikes in enumerate(time_list):
	start_time = time.perf_counter()
	# Define constants
	Cm = 1.0
	V_Na = 50.0
	V_K = -75.0
	V_L = -54.387
	g_Na = 120.0
	g_K = 36.0
	g_L = 0.3
	alpha_r = 2
	beta_r = 1
	g_syn = 1
	E_syn = 0

	# Define initial conditions
	V = -65.0
	m = 0.053
	h = 0.6
	n = 0.318
	r = 0

	# Define time step 
	dt = 0.001

	# Define Hodgkin-Huxley equations
	def dVdt():
		return (1 / Cm) * (Isyn()- (g_L * (V - V_L)) - g_Na * m**3 * h * (V - V_Na) - g_K * n**4 * (V - V_K)) 

	def dmdt():
		return (alpha_m() * (1 - m)) - (beta_m() * m) 

	def dhdt():
		return (alpha_h() * (1 - h)) - (beta_h() * h)  
		
	def dndt():
		return (alpha_n() * (1 - n)) - (beta_n() * n) 

	def alpha_m():
		return (0.1 * (-V - 40)) / (np.exp((-V - 40) / 10) - 1) 

	def alpha_h():
		return 0.07 * np.exp((-V - 65.) / 18.)

	def alpha_n():
		return (0.01 * (-V - 55)) / (np.exp((-V - 55) / 10) -1)

	def beta_m():
		return 4 * np.exp((-V - 65) / 18)

	def beta_h():
		return 1 / (np.exp((-V - 35) / 10) + 1)

	def beta_n():
		return 0.125 * np.exp((-V - 65) / 80)
		
	def drdt():
	#	if t > 20 and t < 21:
	#		return alpha_r  * (1 - r) - (beta_r * r) 
	#	elif t > 10 and t < 11:
	#		return alpha_r  * (1 - r) - (beta_r * r)
	#	elif t > 20 and t < 21:
	#		return alpha_r  * (1 - r) - (beta_r * r)
	#	else:
		return -beta_r * r 

	def Isyn():
	#	if t > 10 and t < 11:
	#		return g_syn * r * (V - E_syn) + 2
	#	if t > 20 and t < 21:
	#		return g_syn * r * (V - E_syn) + 10
	#	else:
	#	

		return g_syn * r * (V - E_syn)
		
	# Execute functions
	t = 0
	points = [[],[],[],[],[]]
	print(spikes)
	while t < spikes:
		
		#if ran.randint(0, 10000) != 1:
	#	if V <= -65:
	#		V += dt * dVdt() #+ ran.uniform(0, 0.01)	

		if t % 50 <= 0.5:
			if -66	 < V < -64:
				V += dt * dVdt() + 10
			else:
				V += dt * dVdt()
		else:
			V += dt * dVdt()
	#	else:
	#		if -66 < V < -64:
	#			V += dt * dVdt() + 10	
		r += dt * drdt() 
		n += dt * dndt() 
		m += dt * dmdt() 
		h += dt * dhdt() 
		t += dt
		points[0].append(t)
		points[1].append(V)
		points[2].append(n)
		points[3].append(m)
		points[4].append(h)
	end_time = time.perf_counter()
	time_taken = end_time - start_time
	time_hist[idx] = time_taken
plt.plot(time_list, time_hist)
plt.show()
np.save("hh_spike_times", time_hist)	
#ax, volt = plt.subplots(figsize = (12, 4))
##ax, nmh = plt.subplots(figsize = (12, 4))
#volt.plot(points[0], points[1], color = "black", linewidth = 0.9)
#volt.set_xlabel("t [ms]")
#volt.set_ylabel("V(t) [mV]")
##volt.axhline(-65, color = "black", linewidth = 0.9, linestyle = "--")

#volt.scatter(14.8, -65, label = "unstable eq. points", color = "black")
#volt.quiver(16.8, -65, -1.5, 0, width = 0.007, scale = 35)
#volt.quiver(12.8, -65, 1.5, 0, width = 0.007, scale = 35)

#volt.scatter(20, -65, label = "stable eq. points", marker = "o",
#		facecolors = "none", edgecolors = "black")
#volt.quiver(20.5, -65, 1.5, 0, width = 0.007, scale = 35)
#volt.quiver(19.5, -65, -1.5, 0, width = 0.007, scale = 35)

#volt.scatter(24.7125, -65, marker = "o", color = "black")
#volt.quiver(26.7125	, -65, -1.5, 0, width = 0.007, scale = 35)
#volt.quiver(22.7125, -65, 1.5, 0, width = 0.007, scale = 35)

#volt.scatter(38.84, -65, color = "black", facecolors = "none", edgecolors = "black")
#volt.quiver(39.34, -65, 1.5, 0, width = 0.007, scale = 35)
#volt.quiver(38.34, -65, -1.5, 0, width = 0.007, scale = 35)

#volt.text(14, -40, "Upstroke")
#volt.text(10, -42, "(hyperpolarisation)")
#volt.text(26, -40, "Repolarisation")
#volt.text(31, -75, "Post-hyperpolarisation")
#volt.text(25, 0, r"$C\frac{dV}{dt} = I - I_K - I_{Na} - I_L$")
#volt.text(25, 30, "Action potential (spike)")
#volt.text(30, -60, "Refractory period")
#volt.text(2, -60, "Rest")
#volt.text(5, -62, "Small depolarisation")
#volt.text(8, -55, "Large depolarisation")
#volt.set_xlim(12, 46)
#volt.legend()
#volt.set_ylim(-80, -50)
#nmh.plot(points[0], points[2], label = "n(t)", linewidth = 0.9, color = "black")
#nmh.plot(points[0], points[3], label = "m(t)", linewidth = 0.9, color = "black",
#		linestyle = "dashed")
#nmh.plot(points[0], points[4], label = "h(t)", linewidth = 0.9, color = "black",
#		linestyle = "dotted")
#nmh.set_xlabel("t [ms]")
#nmh.set_ylabel(r"$P_i, \ \ P_1 = n(t), P_2 = m(t), P_3 = h(t)$")
#nmh.legend()

##
plt.show()


	
