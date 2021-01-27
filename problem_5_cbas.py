import numpy as np
import matplotlib.pyplot as plt
import random

def ave(R):
    a = 0
    for i in range(len(R)):
        a += R[i]
    return a/len(R)

def variance(R):
    a = 0
    ave_R = ave(R)
    for i in range(len(R)):
        a += (R[i]-ave_R)**2
    return a/len(R)

def one_step_1():
    r = np.random.rand()
    theta = 2*np.pi*r
    
    x_i, y_i = np.cos(theta), np.sin(theta)
    
    return x_i, y_i

def one_step_2(x, y):
    r = np.random.rand()
    if r<0.25:
        return x+1, y
    if r>=0.25 and r<0.5:
        return x-1, y
    if r>=0.5 and r<0.75:
        return x, y+1
    if r>=0.75:
        return x, y-1
        

def one_simulation_1(N):
    x, y = 0, 0
    X, Y = [0], [0]
    
    for i in range(N):
        x_i, y_i = one_step_1()
        x += x_i
        y += y_i
        
        X.append(x)
        Y.append(y)

    R = np.sqrt((X[-1]**2 + Y[-1]**2))
    return X, Y, R
    
def one_simulation_2(N):
    x, y = 0, 0
    X, Y = [0], [0]
    
    for i in range(N):
        x, y = one_step_2(x, y)
        
        X.append(x)
        Y.append(y)

    R = np.sqrt((X[-1]**2 + Y[-1]**2))
    return X, Y, R

## 課題c
x, y, R = one_simulation_1(100)
plt.plot(x,y)
plt.show()

## 課題a
ave_1, ave_2, variance_1, variance_2 = [], [], [], []
N = [10, 30, 300, 1000, 3000, 10000]

for n in N:
    R1 = []
    R2 = []
    for i in range(100):
        R1.append(one_simulation_1(n)[2])
        R2.append(one_simulation_2(n)[2])
    ave_1.append(ave(R1))
    ave_2.append(ave(R2))
    variance_1.append(variance(R1))
    variance_2.append(variance(R2))

plt.plot(variance_1, label='variance_1')
plt.plot(variance_2, label='variance_2')
plt.title("variance")
plt.legend()
plt.xticks([0,1,2,3,4,5], [10, 30, 300, 1000, 3000, 10000])
plt.show()

plt.plot(ave_1, label='ave_1')
plt.plot(ave_2, label='ave_2')
plt.show()
plt.title("Average - theoretical values")
plt.legend()
plt.xticks([0,1,2,3,4,5], [10, 30, 300, 1000, 3000, 10000])
plt.plot(ave_1 - np.sqrt(N), label='ave_1 - theoretical values')
plt.plot(ave_2 - np.sqrt(N), label='ave_2 - theoretical values')
plt.show()

## 課題b
R_1, R_2 = [], []
for i in range(100):
    r_1 = one_simulation_1(100)[2]
    r_2 = one_simulation_2(100)[2]
    R_1.append(r_1)
    R_2.append(r_2)
    
ave_1 = ave(R_1)
ave_2 = ave(R_2)
print(ave_1, ave_2)

variance_1 = variance(R_1)
variance_2 = variance(R_2)
print(variance_1, variance_2)

## 課題s
def one_step_4(x, y, z, h):
    r = np.random.rand()
    if r<1/8:
        return x+1, y, z, h
    
    if r>=1/8 and r<2/8:
        return x-1, y, z, h
    
    if r>=2/8 and r<3/8:
        return x, y+1, z, h
    
    if r>=3/8 and r<4/8:
        return x, y-1, z, h
    
    if r>=4/8 and r<5/8:
        return x, y, z+1, h
    
    if r>=5/8 and r<6/8:
        return x, y, z-1, h
    
    if r>=6/8 and r<7/8:
        return x, y, z, h+1
    
    if r>=7/8:
        return x, y-1, z, h-1
        
    
def one_simulation_4(N):
    x, y, z, h = 0, 0, 0, 0
    X, Y, Z, H = [0], [0], [0], [0]
    
    for i in range(N):
        x, y, z, h = one_step_4(x, y, z, h)
        
        X.append(x)
        Y.append(y)
        Z.append(z)
        H.append(h)

    R = np.sqrt(X[-1]**2 + Y[-1]**2 + Z[-1]**2 + H[-1]**2)
    return R

    
ave_4 = []
N = [10, 30, 300, 1000, 3000, 10000]

for n in N:
    R4 = []
    for i in range(100):
        R4.append(one_simulation_4(n))
    ave_4.append(ave(R4))

plt.plot(ave_4, label='Four-dimensional_ave')
plt.title("Four-dimensional_ave")
plt.legend()
plt.xticks([0,1,2,3,4,5], [10, 30, 300, 1000, 3000, 10000])
plt.show()