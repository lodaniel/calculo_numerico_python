import numpy as np
def elim_gauss(M, N):
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n-1):
        for j in range(i+1, n):
            m = M[j][i]/M[i][i]
            for k in range(i, n):
                M[j][k] = M[j][k] - m*M[i][k]
            N[j] = N[j] - m*N[i]
    for j in range(n-1,-1,-1):
        x[j] = N[j]/M[j][j]
        for i in range(j-1,-1,-1):
            N[i] = N[i] - M[i][j]*x[j]
    return x
def impr(M, N):
    for i in range(M.shape[0]):
        linha = []
        for j in range(M.shape[1]):
            linha.append('{0}*x{1}'.format(M[i, j], j + 1))
        print(" + ".join(linha), "=", N[i])
    print()
MAXITER = 100
M = np.array([[4., -7., 9., 1.],
              [-16., 0., -2., 10.],
              [6., -2., 7., -12.],
              [0., 5., -2., 7.]])
N = np.array([-9., 14., 6., 26.])
impr(M, N)
x = elim_gauss(M, N)
print(x)
input()