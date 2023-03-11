import numpy as np
import matplotlib.pyplot as plt
def F2(t, A, B, C, D):
    return A*(t**B)+C*np.cos(D*t)+np.random.normal(0, 1, t.shape)

def gene2coef(A, B, C, D):
    D = (D-511)/100
    return A, B, C, D


T = np.random.random((1000, 1))*100
fit = []
b2 = F2(T, 0.6, 1.2, 100, 0.4)
ind = []
for i in range(0, 1024):
    A, B, C, D = gene2coef(0.6, 1.2, 100, i)
    fit.append(np.sum(abs(F2(T, A, B, C, D)-b2)))
    ind.append(D)

plt.plot(ind, fit)
plt.show()
