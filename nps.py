# Spike frequency vs neurons per second

import matplotlib.pyplot as plt
import numpy as np

spike_frequency = np.arange(0.1, 400, 0.1)
hh_nps_28 = np.zeros(len(spike_frequency))
if_nps_28 = np.zeros(len(spike_frequency))
iz_nps_28 = np.zeros(len(spike_frequency))

hh_nps_1 = np.zeros(len(spike_frequency))
if_nps_1 = np.zeros(len(spike_frequency))
iz_nps_1 = np.zeros(len(spike_frequency))

hh_28 = 89
if_28 = 1926766
iz_28 = 1226008

hh_1 = hh_28 / 2.8
if_1 = if_28 / 2.8
iz_1 = iz_28 / 2.8

for idx, i in enumerate(spike_frequency):
	hh_nps_28[idx] = hh_28 / i
	if_nps_28[idx] = if_28 / i
	iz_nps_28[idx] = iz_28 / i
	hh_nps_1[idx] = hh_1 / i
	if_nps_1[idx] = if_1 / i
	iz_nps_1[idx] = iz_1 / i

plt.plot(spike_frequency, hh_nps_28, color = "black", linewidth = 0.9, label = "HH")
plt.plot(spike_frequency, if_nps_28, color = "black", linewidth = 0.9,
		linestyle = "dashed", label = "IF")
plt.plot(spike_frequency, iz_nps_28, color = "black", linewidth = 0.9,
		linestyle = "dotted", label = "IZ")
plt.xlabel("Spike frequency [Hz]")
plt.ylabel("Simulation speed [neurons per second]")
plt.legend()
plt.ylim(0, 200000)
plt.show()
#plt.savefig("2.8ghz_all.png")
plt.close()


plt.plot(spike_frequency, hh_nps_1, color = "black", linewidth = 0.9, label = "HH")
plt.plot(spike_frequency, if_nps_1, color = "black", linewidth = 0.9,
		linestyle = "dashed", label = "IF")
plt.plot(spike_frequency, iz_nps_1, color = "black", linewidth = 0.9,
		linestyle = "dotted", label = "IZ")
plt.xlabel("Spike frequency [Hz]")
plt.ylabel("Simulation speed [neurons per second]")
plt.legend()
plt.ylim(0, 200000)
#plt.savefig("1ghz_all.png")
plt.show()

