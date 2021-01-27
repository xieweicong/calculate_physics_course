import numpy as np
import matplotlib.pyplot as plt

def rk42(x0, y, B):
    x_solution, y_solution1, y_solution2 = [x0], [y[0]], [y[1]]
    x = x0
    k = -1
    
    
    while y[0]>1 + 0.00001 and y[0]<101:
        h = 0.1*np.sqrt((y[0]**3-(B**2)*(y[0]-1))/y[0]**3)
        k1 = df1(x, y[0], y[1], k)
        l1 = df2(x, y[0], y[1])
        
        k2 = df1(x+0.5*h, y[0]+h*k1/2, y[1]+h*l1/2, k)
        l2 = df2(x+0.5*h, y[0]+h*k1/2, y[1]+h*l1/2)
        
        k3 = df1(x+0.5*h, y[0]+h*k2/2, y[1]+h*l2/2, k)
        l3 = df2(x+0.5*h, y[0]+h*k2/2, y[1]+h*l2/2)
        
        k4 = df1(x+h, y[0]+h*k3, y[1]+h*l3, k)
        l4 = df2(x+h, y[0]+h*k3, y[1]+h*l3)
        
        y[0] += h*(k1 + 2*k2 + 2*k3 + k4)/6
        y[1] += h*(l1 + 2*l2 + 2*l3 + l4)/6
        
        if y_solution1[-1]-y[0]<0.0000001:
            k = 1
        y_solution1.append(y[0])
        y_solution2.append(y[1])
       
        
#         if i%100==0:
#             print(i, x, y[0])

        x += h
        x_solution.append(x)
    print(y[0], y[1])
        
    return x_solution, y_solution1, y_solution2
        
def df1(x, y1, y2, k):
    return k*(1-1/y1)*np.sqrt(1-B**2/y1**2+B**2/y1**3)

def df2(x, y1, y2):
    return (1-1/y1)*B/(y1**2)


GRAV = 9.80665
MASS = 1.0
rg = 0

fig = plt.figure(figsize=(7, 7))
for b in range(1,50,1):
    B = 0.1*b
    x0 = 0
    y10 = 100
    y20 = np.arcsin(B/y10)

    y = [0, 0]

    y[0] = y10
    y[1] = y20

    x_solution, y_solution1, y_solution2 = rk42(x0, y, B)
    x = y_solution1*np.cos(y_solution2)
    y = y_solution1*np.sin(y_solution2)
    line1 = plt.plot(x, y)


plt.xlim(-5,5)
plt.ylim(-5,5)
plt.title("Trajectory of rays around a black hole", fontsize=12)
plt.show()
print(y[0], y[1])