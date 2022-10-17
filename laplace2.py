import numpy as np
import matplotlib.pyplot as plt
itera_max = 5000
compr_X = compr_Y = 20
delta = 1
T_cima = 100
T_baixo = T_esq = 0
T_dir = 30
chute_inicial = 30
cor_interpol = 50
cor_map = plt.cm.jet
X, Y = np.meshgrid(np.arange(0, compr_X), np.arange(0, compr_Y))
T = np.empty((compr_X, compr_Y))
T.fill(chute_inicial)
T[(compr_Y-1):, :] = T_cima
T[:1, :] = T_baixo
T[:, (compr_X-1):] = T_dir
T[:, :1] = T_esq
print("Aguarde...")
for iteration in range(0, itera_max):
    for i in range(1, compr_X-1, delta):
        for j in range(1, compr_Y-1, delta):
            T[i,j] = 0.25*(T[i+1][j]+T[i-1][j]+T[i][j+1]+T[i][j-1])
print("...terminado.")
plt.title("Temperatura")
plt.contourf(X, Y, T, cor_interpol, cmap=cor_map)
plt.colorbar()
plt.show()