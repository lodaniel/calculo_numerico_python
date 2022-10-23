# https://www.youtube.com/watch?v=k8opTJTkGek
# https://github.com/PyPhy/Python/blob/master/Physics/FS_square.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib.patches import ConnectionPatch

class FS():
    def __init__(self, Circles, Cycles):
        self.Circles = Circles
        self.Cycles  = Cycles
    def Xcenter(self, n, theta):
        Ans = 0
        if n > 0:
            for i in range(1,n+1):
                Ans += (4/((2*i-1)*np.pi))*np.cos((2*i-1)*theta)
        return Ans
    def Ycenter(self,n,theta):
        Ans = 0
        if n > 0:
            for i in range(1,n+1):
                Ans += (4/((2*i-1)*np.pi))*np.sin((2*i-1)*theta)
        return Ans
    def Rds(self, n):
        return 4/((2*n+1)*np.pi)
    def PlotFS(self):
        time = np.linspace(0,self.Cycles,self.Cycles*70)
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(80,60))
        fig.suptitle('Serie de Fourier', fontsize = 45, fontweight = 'bold')
        color = cm.rainbow(np.linspace(0,1,self.Circles))
        for t in time:
            thta = 2*np.pi*t
            axs[0].clear()
            if (t > 0):
                con.remove()
            for i, c in zip(range(0, self.Circles), color):
                xc = self.Xcenter(i, thta)
                yc = self.Ycenter(i, thta)
                R  = self.Rds(i)
                crl = plt.Circle((xc,yc),R,color=c,alpha=0.5,linewidth=2)
                axs[0].add_artist(crl)
                if (i > 0):
                    axs[0].plot([xco,xc],[yco,yc],color='b',linewidth=2)
                xco = xc
                yco = yc
                Ro  = R
            axs[0].axis('square')
            axs[0].set_xlim([-9/np.pi,9/np.pi])
            axs[0].set_ylim([-9/np.pi,9/np.pi])
            if (t > 0):
                axs[1].plot([to,t],[ycirc,yc],color='m',linewidth=1.5)
            to    = t
            ycirc = yc
            axs[1].axis('square')
            axs[1].set_xlim([0,18/np.pi])
            axs[1].set_ylim([-9/np.pi,9/np.pi])
            con = ConnectionPatch(xyA = (t,yc), xyB = (xc,yc), 
                                   coordsA = 'data', coordsB = 'data',
                                   axesA = axs[1], axesB = axs[0], 
                                   color = 'red')
            axs[1].add_artist(con)
            plt.pause(1e-11)

if __name__ == '__main__':
    fs = FS(8, 2)
    fs.PlotFS()