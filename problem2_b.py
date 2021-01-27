import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def rk42(x0, xf, y, n, w):
    x_solution, y_solution1, y_solution2 = [], [], []
    
    x = x0
    h = (xf-x0)/n
    
    for i in range(n):
        k1 = df1(x, y[0], y[1])
        l1 = df2(x, y[0], y[1], w)
        
        k2 = df1(x+0.5*h, y[0]+h*k1/2, y[1]+h*l1/2)
        l2 = df2(x+0.5*h, y[0]+h*k1/2, y[1]+h*l1/2, w)
        
        k3 = df1(x+0.5*h, y[0]+h*k2/2, y[1]+h*l2/2)
        l3 = df2(x+0.5*h, y[0]+h*k2/2, y[1]+h*l2/2, w)
        
        k4 = df1(x+h, y[0]+h*k3, y[1]+h*l3)
        l4 = df2(x+h, y[0]+h*k3, y[1]+h*l3, w)
        
        y[0] += h*(k1 + 2*k2 + 2*k3 + k4)/6
        y[1] += h*(l1 + 2*l2 + 2*l3 + l4)/6
        
        y_solution1.append(y[0])
        y_solution2.append(y[1])

        x = x0 + (i+1)*h
        x_solution.append(x)
        
    return x_solution, y_solution1
        
def df1(x, y1, y2):
    return y2

def df2(x, y1, y2, w):
    return -GRAV/LENG*np.sin(y1) + 0.1*(w**2/LENG)*np.sin(w0*x)*np.cos(y1)

LENG = 1.0
GRAV = 9.80665
MASS = 1.0
w0 = np.sqrt(GRAV/LENG)
w = 8

x0 = 0
xf = 10
y10 = 0
y20 = 0
n = 500

y = [0, 0]

y[0] = y10
y[1] = y20

x_solution, y_solution1= rk42(x0, xf, y, n, w0)
x_solution, y_solution2= rk42(x0, xf, y, n, w)

def update_points1(num):
    point_ani.set_data(x1[num], y1[num])
    return point_ani,

def update_points2(num):
    point_ani.set_data(x2[num], y2[num])
    return point_ani,
 
x1 = LENG*np.sin(np.array(y_solution1)) + 0.1*np.sin(w0*np.array(x_solution))
y1 = -LENG*np.cos(y_solution1)

fig1 = plt.figure(tight_layout=True, figsize=(8, 5))
# plt.title("w=w0", fontsize=18)
# ax1 = fig1.add_subplot(1,2,1)
# plt.plot(x1,y1)
# point_ani, = plt.plot(x1[0], y1[0], "ro")
# plt.grid(ls="--")

# ani1 = animation.FuncAnimation(fig1, update_points1, np.arange(0, 500), interval=20, blit=True)

# ax2 = fig1.add_subplot(1,2,2)
# plt.plot(x_solution, y_solution1)


# fig2 = plt.figure(tight_layout=True, figsize=(8, 5))
plt.title("w!=w0", fontsize=18)
# x2 = LENG*np.sin(np.array(y_solution2)) + 0.1*np.sin(w0*np.array(x_solution))
# y2 = -LENG*np.cos(y_solution2)
# # ax1 = fig2.add_subplot(1,2,1)
# plt.plot(x2,y2)
# point_ani, = plt.plot(x2[0], y2[0], "ro")
# plt.grid(ls="--")

# ani2 = animation.FuncAnimation(fig2, update_points2, np.arange(0, 500), interval=6, blit=True)

# ax2 = fig2.add_subplot(1,2,2)
plt.plot(x_solution, y_solution2)

plt.show()