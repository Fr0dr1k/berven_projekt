import numpy as np

import roadster as r
import matplotlib.pyplot as plt

anna = r.load_route("speed_anna.npz")
elsa = r.load_route("speed_elsa.npz")

x_a = np.linspace(0,anna[0][-1],20000)
y_a = r.velocity(x_a,"speed_anna.npz")

x_e = np.linspace(0,elsa[0][-1],20000)
y_e = r.velocity(x_e,"speed_elsa.npz")

#plt.plot(x_a,y_a)

plt.plot(x_a, y_a, label="Anna", color="blue")
plt.plot(anna[0],anna[1], ".", markersize=2.0, color="r")

plt.xlabel("Distance (km)")
plt.ylabel("Speed (km/h)")
plt.title("Anna")

plt.show()
plt.plot(x_e, y_e, label="Elsa", color="b")
plt.plot(elsa[0], elsa[1], ".", markersize=2.0, color="r")

plt.xlabel("Distance (km)")
plt.ylabel("Speed (km/h)")
plt.title("Elsa")

plt.show()