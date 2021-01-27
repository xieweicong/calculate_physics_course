import math
import numpy as np
import matplotlib.pyplot as plt

N = 100

C1 = 0.217
K1 = 0.49
p1 = 2.7
deltaX = 10/N
deltaT = 0.1*(deltaX)**2*C1*p1/K1

def suchikai(x, t, n, T0):
    C = 0.217
    K = 0.49
    p = 2.7
    T = 0

    for i in range(1,n,2):
        h = i*np.pi/10
        T = T + (4*T0/(i*np.pi))*np.sin(h*x)*np.exp(-h**2*K*t/(C*p))
    return T

tempp = [0.0]
for i in range(1, N):
    if i<51:
        tempp.append(i)
    else:
        tempp.append(100-i)
tempp.append(0.0)
plt.ion()

temp = tempp
t0 = temp

j = 0
while temp[50]>10:
    j = j + 1
    for i in range(1, N):
        temp[i] = tempp[i] + 0.1*(tempp[i+1]+tempp[i-1]-2*tempp[i])
        
    tempp = temp
    if j%100==0:
        y = []
        t = j*deltaT
        for i in range(1,N+1):
            y.append(suchikai(i*0.1,t,11,t0[i]))
        plt.cla()
        plt.ylim(0, 100)
        plt.plot(y)
        plt.plot(temp)
        plt.pause(0.1)
    
plt.ioff()
# print(suchikai(5,0,9,100))
plt.show()