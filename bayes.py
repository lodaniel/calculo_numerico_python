'''
Esta animação exibe as atualizações de estimativas posteriores à medida que são reajustadas quando novos dados chegam. A linha vertical representa o valor teórico para o qual a distribuição plotada deve convergir.
'''

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim

def func(var, p1, p2):
    return (var**(p1-1)*(1-var)**(p2-1)*math.gamma(p1+p2)/(math.gamma(p1)*math.gamma(p2)))

class UpdateDist:
    def __init__(slf, eixo, prob=0.5):
        slf.success = 0
        slf.prob = prob
        slf.line, = eixo.plot([], [], 'k-')
        slf.var = np.linspace(0, 1, 200)
        slf.eixo = eixo
        # parametros de plotagem
        slf.eixo.set_xlim(0, 1)
        slf.eixo.set_ylim(0, 10)
        slf.eixo.grid(True)
        # Linha vertical que representa o valor teorico
        # para o qual a distribuição plotada deve convergir.
        slf.eixo.axvline(prob, linestyle='--', color='black')
    def __call__(slf, i):
        # plotagem pode ser executada continuamente e continua-se 
        # observando novas realizações do processo.
        if i == 0:
            slf.success = 0
            slf.line.set_data([], [])
            return slf.line,
        # Sucesso baseado em exceder um limite (escolha uniforme)
        if np.random.rand(1,) < slf.prob:
            slf.success += 1
        z = func(slf.var,slf.success+1,(i-slf.success)+1)
        slf.line.set_data(slf.var, z)
        return slf.line,

# Corrigindo o estado aleatório para reprodutibilidade
np.random.seed(19680801)
fig, eixo = plt.subplots()
ud = UpdateDist(eixo, prob=0.7)
anim = anim(fig,ud,frames=100,interval=100,blit=True)
plt.show()