# Simulation time plotter
# Created by Alex O'Hare, 29/05/2024

# Import the required libraries
import matplotlib.pyplot as plt
import numpy as np

# Load the data
HH = np.load("hh_spike_times.npy")
IF = np.load("if_spike_times.npy")
IZ = np.load("iz_spike_times.npy")

time_list = range(1, 5000, 200)

#plt.plot(time_list, HH, color = "black", linewidth = 0.9, label = "HH")
#plt.plot(time_list, IF, color = "black", linewidth = 0.9, linestyle = "dashed",
#		label = "IF")
#plt.plot(time_list, IZ, color = "black", linewidth = 0.9, linestyle = "dotted",
#		label = "IZ")
#plt.xlabel("Spikes [a.u.]")
#plt.ylabel("Time [s]")
#plt.legend()
#plt.show()

HH_vel = []
IF_vel = []
IZ_vel = []
for i in range(len(time_list)):
	HH_vel.append(time_list[i] / HH[i])
	IF_vel.append(time_list[i] / IF[i])
	IZ_vel.append(time_list[i] / IZ[i])
	

print("HH: " + str(np.mean(HH_vel)) + ", IF: " + str(np.mean(IF_vel)) +
		", IZ: " + str(np.mean(IZ_vel)))
		
