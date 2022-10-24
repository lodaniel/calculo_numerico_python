# Grafico de curvas de nivel no plano

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
x, y = np.meshgrid(x, y)
z = x**2-2*y**2-1
fig, ax = plt.subplots()
contornos = ax.contour(x, y, z, 20)
ax.clabel(contornos, inline=True, fontsize=10)
ax.set_title('Curvas de nível')
plt.contour(x, y, z)
plt.show()
