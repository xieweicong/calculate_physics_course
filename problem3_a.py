import math
import numpy as np
import matplotlib.pyplot as plt

N1 = 50
N2 = 50
N = N1 + N2

C1 = 0.217
K1 = 0.49
p1 = 2.7
deltaX1 = 5/N1
deltaT1 = 0.1*(deltaX1)**2*C1*p1/K1

C2 = 0.113
K2 = 0.12
p2 = 7.8
b = K2*deltaT1/(C2*p2*deltaX1**2)

tempp = [0.0]
temp = []
for i in range(1, N):
    tempp.append(100.0)
tempp.append(0.0)
plt.ion()

for i in range(0, N):
        temp.append(tempp[i])

j = 0
while tempp[50]>5:
    j = j + 1
    for i in range(1, N1):
        temp[i] = tempp[i] + 0.1*(tempp[i+1]+tempp[i-1]-2*tempp[i])
    for i in range(N1, N):
        temp[i] = tempp[i] + b*(tempp[i+1]+tempp[i-1]-2*tempp[i])
        
    for i in range(1, N):
        tempp[i] = temp[i]
    if j%100==0:
        plt.cla()
        plt.ylim(0, 100)
        plt.plot(temp)
        plt.pause(0.01)
    
plt.ioff()

plt.show()