import matplotlib.pyplot as plt
import numpy as np
i = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X**2 - Y**2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig("3d_surface_plot.png", dpi=300)
plt.show()