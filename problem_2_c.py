import math
import numpy as np
import matplotlib.pyplot as plt

def rk42(x0, xf, y, n):

    
    x = x0
    h = (xf-x0)/n
    x_solution, y_solution1, y_solution2 = [x], [y[0]], [y[1]]
    
    for i in range(n):
        k1 = df1(x, y[0], y[1])
        l1 = df2(x, y[0], y[1])
        
        k2 = df1(x+0.5*h, y[0]+h*k1/2, y[1]+h*l1/2)
        l2 = df2(x+0.5*h, y[0]+h*k1/2, y[1]+h*l1/2)
        
        k3 = df1(x+0.5*h, y[0]+h*k2/2, y[1]+h*l2/2)
        l3 = df2(x+0.5*h, y[0]+h*k2/2, y[1]+h*l2/2)
        
        k4 = df1(x+h, y[0]+h*k3, y[1]+h*l3)
        l4 = df2(x+h, y[0]+h*k3, y[1]+h*l3)
        
        y[0] += h*(k1 + 2*k2 + 2*k3 + k4)/6
        y[1] += h*(l1 + 2*l2 + 2*l3 + l4)/6
        
        y_solution1.append(y[0])
        y_solution2.append(y[1])

        x = x0 + (i+1)*h
        x_solution.append(x)
        
    return x_solution, y_solution1, y_solution2
        
def df1(x, y1, y2):
    return y2

def df2(x, y1, y2):
    return -GRAV/LENG*math.sin(y1)


LENG = 1.0
GRAV = 9.80665
MASS = 1.0

x0 = 0
xf = 10
y10 = math.pi/4
y20 = 0
n = 500

y = [0, 0]

y[0] = y10
y[1] = y20
T = []

for i in range(1,20):
    x0 = 0
    xf = 10
    y10 = i*0.1
    y20 = 0
    n = 500

    y = [0, 0]

    y[0] = y10
    y[1] = y20
    x_solution, y_solution1, y_solution2 = rk42(x0, xf, y, n)
    c = 0
    for k in range(len(x_solution)):
        if y_solution1[k]<-y10+0.001:
            T.append(x_solution[k])
            break

#     kinetic_energy = (MASS*(np.array(y_solution2)*LENG)**2)/2
#     potential_energy = (LENG-(np.cos(np.array(y_solution1))*LENG))*MASS*GRAV
#     all_energy = kinetic_energy + potential_energy
#     ax = fig.add_subplot(2,1,1)
    fig = plt.figure(num=1, figsize=(12, 8))
#     plt.title("2_c_Angular", fontsize=18)
#     plt.plot(x_solution, y_solution1, label="Angular")
# #     plt.legend(loc='upper right', fontsize=18)
#     plt.xlabel('time', fontsize=15)
#     plt.ylabel('Angular', fontsize=15)
    
# ax = fig.add_subplot(2,1,2)
x=np.linspace(0.1,2,19)
plt.title("period", fontsize=18)
plt.plot(x, T)

# ax2 = fig.add_subplot(3,1,2)
# plt.plot(x_solution, y_solution2, label="Angular_velocity")
# plt.title("2_c_Angular_velocity", fontsize=18)
# plt.legend(loc='upper right', fontsize=18)
# plt.xlabel('time', fontsize=15)
# plt.ylabel('Angular velocity', fontsize=15)

# plt.title("Energy", fontsize=18)
# # ax1 = fig.add_subplot(3,1,3)
# plt.plot(x_solution, kinetic_energy, label="kinetic_energy")
# plt.legend(loc='upper right', fontsize=18)

# plt.plot(x_solution, potential_energy, label="potential_energy")
# plt.legend(loc='upper right', fontsize=18)

# plt.plot(x_solution, all_energy, label="all_energy")
# plt.legend(loc='upper right', fontsize=18)

# plt.xlabel('time', fontsize=15)
# plt.ylabel('energy', fontsize=15)

plt.show()