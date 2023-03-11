import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def F2(t, A, B, C, D):
    return A*(t**B)+C*np.cos(D*t)+np.random.normal(0, 1, t.shape)


def gene2coef(A, B, C, D):
    A = (A-511)/100
    C = (C-511)
    return A, B, C, D


T = np.random.random((1000, 1))*100
fit = []
b2 = F2(T, 0.6, 1.2, 100, 0.4)
ind_i = []
ind_j = []
for i in range(0, 1024):
    print(i)
    fit.append([])
    for j in range(0, 1024):
        A, B, C, D = gene2coef(i, 1.2, j, 0.4)
        fit[i].append(np.sum(abs(F2(T, A, B, C, D)-b2)))
ind_i = (np.arange(1024) - 511)/100
ind_j = (np.arange(1024) - 511)
fig = plt.figure()
ax = plt.axes(projection='3d')
#ind_i = np.array(ind_i)
#ind_j = np.array(ind_j)
fit = np.array(fit)
ind_i, ind_j = np.meshgrid(ind_i, ind_j)
ax.plot_surface(ind_i, ind_j,fit)
plt.show()