import numpy as np
import matplotlib.pyplot as plt

# Number of T's
n = 3
# dimensional parameter, controls general flashbang strength
alpha = 0.1

# exponential parameter, controls fall off of the flashbang very close to the T
a = 0.4
# Define T's positions

t_pos = [(0.5,0.4), (0.5,0.4+0.2828427125)]

x = np.linspace(0, 1, 10000)
y = x

X, Y = np.meshgrid(x, y)


def u(r):
    return a*(np.e)**2 * np.exp(-a/r)/(4*r*r) * np.sin(2*np.pi*4*r)


def h(x, y):
    res = 0
    for x_k, y_k in t_pos:
        r = np.sqrt((x - x_k)**2 + (y - y_k)**2)
        res += u(r)
    return alpha*res


Z = h(X, Y)


fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')
#for x_k, y_k in t_pos:
#    ax.plot(x_k, y_k, 'rx')
pcm = ax.pcolormesh(X, Y, Z, cmap='inferno')
#fig.colorbar(pcm)
fig.savefig("flashbangexample.png", dpi=1000, bbox_inches='tight', pad_inches=0)
