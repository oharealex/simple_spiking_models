# import the required libraries
import matplotlib.pyplot as plt
import numpy as np
import random as r

# define the constants and variables
u = 32.5
v = -65
I = -70
a = 0.02
b = 0.2
c = -65

# define the differential equations
def dvdt(u, v):
	return (0.04 * v * v) + (5 * v) + 140 - u + I

def dudt(u, v, a, b):
	return a * ((b * v) - u)

# main loop
t = 0
T = 10000
dt = 0.01
v_his = []
u_his = []
t_his = []
while t < T:
	v += dvdt(u, v) * dt
	u += dudt(u, v, a, b) * dt
	if v >= 30:
		v = c
		u = u + d
	v_his.append(v)
	u_his.append(v)
	t_his.append(t)
	t += dt

plt.plot(v_his)
plt.plot(u_his)
plt.show()

