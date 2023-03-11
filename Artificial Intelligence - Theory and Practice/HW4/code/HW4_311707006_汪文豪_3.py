import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
df = pd.read_csv('./作業/NVDA.csv')

real_data = df['Close']
#plt.plot(df['Close'])
#plt.show()


def F2(T, t_c, beta, omega, phi):
    A = np.zeros((t_c, 3))
    b = np.zeros((t_c, 1))
    for t in range(0, t_c):
        A[t, 0] = 1
        A[t, 1] = (t_c - t)**beta
        A[t, 2] = ((t_c - t)**beta) * np.cos(omega*np.log(t_c-t)+phi)
        b[t] = T[t]
    x = np.linalg.lstsq(A, b)[0]
    print(x)    
    A2 = x[0][0]
    B = x[1][0]
    C = x[2][0]
    C = C/B
    t = np.arange(t_c)
    return A2+(B*((t_c-t)**beta)*(1+C*np.cos(omega*np.log(t_c-t)+phi)))
    

def gene2coef(gene):
    t_c = (np.sum(2**np.arange(2)*gene[0:2])) + 731 # 4
    beta = (np.sum(2**np.arange(10)*gene[2:12]))/1024 # 0 - 1
    omega = (np.sum(2**np.arange(18)*gene[12:30]))/262144 * 10 # omega>=0, random
    phi = (np.sum(2**np.arange(10)*gene[30:40]))/(1024*(2*math.pi)) # 0 - 2 pi
    return t_c, beta, omega, phi

T = np.random.random((1000, 1))*100
N = 10000
G = 10
survive_rate = 0.05
mutation_rate = 0.001
survive = round(N*survive_rate)
mutation = round(N*40*mutation_rate)

pop = np.random.randint(0, 2, (N, 40))
fit = np.zeros((N, 1))

for generation in range(G):
    for i in range(N):
        t_c, beta, omega, phi = gene2coef(pop[i, :])
        realPrices = df.iloc[0:t_c]['Close'].to_numpy()
        realPrices = np.log(realPrices)
        prediction = F2(realPrices, t_c, beta, omega, phi)
        fit[i] = np.mean(abs(prediction-realPrices[0:t_c]))
    # selection
    sortf = np.argsort(fit[:, 0])
    pop = pop[sortf, :]
    for i in range(survive, N):
        fid = np.random.randint(0, survive)
        mid = np.random.randint(0, survive)
        while(fid == mid):
            mid = np.random.randint(0, survive)
        mask = np.random.randint(0, 2, [1, 40])
        son = pop[mid, :].copy()
        father = pop[fid, :]
        son[mask[0, :] == 1] = father[mask[0, :] == 1]
        pop[i, :] = son
    for i in range(mutation):
        m = np.random.randint(survive, N)
        n = np.random.randint(0, 40)
        pop[m, n] = 1-pop[m, n]

for i in range(N):
    t_c, beta, omega, phi = gene2coef(pop[i, :])
    realPrices = df.iloc[0:t_c]['Close'].to_numpy()
    realPrices = np.log(realPrices)
    prediction = F2(realPrices, t_c, beta, omega, phi)
    fit[i] = np.mean(abs(prediction-realPrices[0:t_c]))
sortf = np.argsort(fit[:, 0])
pop = pop[sortf, :]

t_c, beta, omega, phi = gene2coef(pop[0, :])
prediction = F2(realPrices, t_c, beta, omega, phi)
print(t_c, beta, omega, phi)
plt.plot(df['Close'].iloc[0:t_c])
plt.plot(np.exp(prediction))
plt.show()