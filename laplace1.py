# Solucao da equacao de laplace pelo metodo da diferenca finita
import numpy as np
import matplotlib.pyplot as plt

itera_max = 5000
compr_X = compr_Y = 100 #retangulo
delta = 1
# Condição de contorno
y_alto = []
y_baixo = []
x_dir = []
x_esq = []
for i in range(compr_X):
    y_baixo.append(np.sin(2*np.pi*i/100))
    y_alto.append(np.cos(np.pi*i/200))
    x_dir.append([0])
    x_esq.append([i/100])
chute_ini = 1 #chute inicial no interior
colorinterpolation = 50
colourMap = plt.cm.jet #pode tentar: colourMap = plt.cm.coolwarm
X, Y = np.meshgrid(np.arange(0, compr_X), np.arange(0, compr_Y))
# Tamanho da matriz e valor interior com chute inicial
T = np.empty((compr_X, compr_Y))
T.fill(chute_ini)
# Definindo condicao de contorno
T[(compr_Y-1):, :] = np.copy(y_alto)
T[:1, :] = np.copy(y_baixo)
T[:, (compr_X-1):] = np.copy(x_dir)
T[:, :1] = np.copy(x_esq)
# Iteracoes
cont = 0
for itera in range(0, itera_max):
    for i in range(1, compr_X-1, delta):
        for j in range(1, compr_Y-1, delta):
            pre = T[i, j]
            T[i,j] = 0.25*(T[i+1][j]+T[i-1][j]+T[i][j+1]+T[i][j-1])
            cont+=1
            #if abs(pre-T[i, j])/pre <= 0.000001:
                #break
print(str(cont))
# Contorno
plt.title("Solucao por relaxamento")
plt.contourf(X,Y,T,colorinterpolation,cmap=colourMap)
plt.colorbar()
plt.show()
