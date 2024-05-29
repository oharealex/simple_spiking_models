# Integrate-and-Fire model
# Alex O'Hare, 27/05/2024

# Import the required libraries
import matplotlib.pyplot as plt
import numpy as np

# Define the variables and constants
v_rest = -65      # Resting potential
v = v_rest        # Initial membrane potential
v_reset = -75     # Reset potential after spike
E_threshold = -60 # Threshold for firing
R = 1             # Membrane resistance
I = 70	         # Input current (constant)
tau = 10          # Membrane time constant
dt = 50       # Time step
t_max = 1000       # Total simulation time

# Define the differential equation for membrane potential
def dvdt(v, I):
    return (-(v - v_rest) + R * I) / tau

# Data storage for plotting
v_his = []
t_his = []

t = 0

# Simulation loop
while t < t_max:
    v += dvdt(v, I) * dt
    if v >= E_threshold:
        v = 40           # Simulate spike
        v_his.append(v)
        t_his.append(t)
        v = v_reset      # Reset potential
    else:
        v_his.append(v)
        t_his.append(t)
    
    t += dt

# Plotting the results
plt.figure(figsize=(12, 4))
plt.plot(t_his, v_his, color="black", linewidth=0.9)
plt.axhline(E_threshold, linestyle="--", color="black", linewidth=0.9)
plt.axhline(v_rest, linestyle="--", color="black", linewidth=0.9)
plt.axhline(v_reset, linestyle="--", color="black", linewidth=0.9)
plt.text(t_max + 1, E_threshold, r"$E_{threshold}$")
plt.text(t_max + 1, v_rest, r"$E_{rest}$")
plt.text(t_max + 1, v_reset, r"$E_{reset}$")

plt.ylim(-80, 50)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Integrate-and-Fire Neuron Model')
plt.show()

