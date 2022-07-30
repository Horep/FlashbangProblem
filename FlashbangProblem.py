import numpy as np
import matplotlib.pyplot as plt

# strength
alpha = 0.1

# exponential parameter
a = 0.2
# Define t's positions

t_pos = [(0.25, 0.5), (0.75, 0.5)]

x_lin = np.linspace(0, 1, 5000)
y_lin = x_lin

X, Y = np.meshgrid(x_lin, y_lin)


def u(r):  # objective function to be graphed
    res = a*np.e**2 * np.exp(-a/r)/(4*r*r)
    return res


def h(x, y):
    res = 0
    for x_n, y_n in t_pos:
        r = np.sqrt((x - x_n)**2 + (y - y_n)**2)  # calculates the distance from the T
        res += u(r)  # adds the cost from that T
    return alpha*res


Z = h(X, Y)  # calculate the flashbang value at each point in the region


fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel("x")
ax.set_ylabel("y")
for x_k, y_k in t_pos:  # for each T, plot their position as a red x
    ax.plot(x_k, y_k, 'rx')
pcm = ax.pcolormesh(X, Y, Z, cmap='inferno')
fig.colorbar(pcm, label="Flash")
fig.savefig("flashbang_three_ts_1.png", dpi=1000, bbox_inches='tight', pad_inches=0)
plt.show()
