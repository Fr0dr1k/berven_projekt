#!/usr/bin/env python3
#Wed Mar 16 15:04:11 2022 +0100, 601cd27
import numpy as np
import roadster
import matplotlib.pyplot as plt

speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = roadster.consumption(speed_kmph)

plt.plot(speed_kmph,consumption_Whpkm)
plt.xlabel("Speed (km/h)")
plt.ylabel("Consumption (Wh/km)")
plt.show()