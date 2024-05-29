# Integrate-and-Fire model
# Alex O'Hare, 27/05/2024

# Import the required libraries
import matplotlib.pyplot as plt
import numpy as np
import time

# Define the variables and constants
v_rest = -65      # Resting potential
v = v_rest        # Initial membrane potential
v_reset = -75     # Reset potential after spike
E_threshold = -60 # Threshold for firing
R = 100             # Membrane resistance
I = 0           # Input current (constant)
tau = 10          # Membrane time constant
dt = 1     # Time step (50 ms)
t_max = 1000     # Total simulation time in milliseconds
fire_interval = 50 # Firing interval in milliseconds

# Define the differential equation for membrane potential
def dvdt(v, I):
	return (-(v - v_rest) + R * I) / tau

# Data storage for plotting
v_his = []
t_his = []

t = 0

# Simulation loop
while t < t_max:
	if t % 50 <= 0.5:
	    I = 70
	else:
	    I = 0
	v += dvdt(v, I) * dt
	if v >= E_threshold:
		     # Reset potential
	    v = 40
	    v_his.append(v) # Record threshold crossing
	    t_his.append(t)  # Record time
	    v = v_reset 
	else:
	    v_his.append(v)
	    t_his.append(t)
	
	t += dt


# Plotting the results
plt.figure(figsize=(12, 4))
plt.plot(t_his, v_his, color="black", linewidth=0.9)
#plt.axhline(E_threshold, linestyle="--", color="black", linewidth=0.9)
#	plt.axhline(v_rest, linestyle="--", color="black", linewidth=0.9)
#plt.axhline(v_reset, linestyle="--", color="black", linewidth=0.9)
#plt.text(t_max + 1, E_threshold, r"$E_{threshold}$")
#plt.text(t_max + 1, v_rest, r"$E_{rest}$")
#plt.text(t_max + 1, v_reset, r"$E_{reset}$")

plt.ylim(-80, 50)
plt.xlabel('t [ms]')
plt.ylabel('V(t) [mV]')
#plt.title('Integrate-and-Fire Neuron Model')
plt.show()

