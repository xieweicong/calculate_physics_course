import math
import matplotlib.pyplot as plt

LENG = 1.0
GRAV = 9.80665
MASS = 1.0

def rk42(x0, xf, y, n):
    x_solution, kinetic_energy_solution, potential_energy_solution, all_energy_solution = [], [], [], []
    
    x = x0
    h = (xf-x0)/n
    
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
        
        kinetic_energy = (MASS*(y[1]*LENG)**2)/2
        potential_energy = -math.cos(y[0])*LENG*MASS
        all_energy = kinetic_energy + potential_energy
        
        kinetic_energy_solution.append(kinetic_energy)
        potential_energy_solution.append(potential_energy)
        all_energy_solution.append(all_energy)

        x = x0 + (i+1)*h
        x_solution.append(x)
        
    return x_solution, kinetic_energy_solution, potential_energy_solution, all_energy_solution
        
def df1(x, y1, y2):
    return y2

def df2(x, y1, y2):
    return -GRAV/LENG*math.sin(y1)

x0 = 0
xf = 20
y10 = math.pi/4
y20 = 0
n = 200

y = [0, 0]

y[0] = y10
y[1] = y20

x_solution, kinetic_energy, potential_energy, all_energy = rk42(x0, xf, y, n)

# fig = plt.figure(num=1, figsize=(16, 5))
# ax1 = fig.add_subplot(2,2,1)
plt.plot(x_solution, kinetic_energy)
plt.title("2_c_Angular")
# ax2 = fig.add_subplot(2,2,2)
plt.plot(x_solution, potential_energy)
plt.title("2_c_Angular_velocity")
# ax3 = fig.add_subplot(2,2,3)
plt.plot(x_solution, all_energy)
plt.show()