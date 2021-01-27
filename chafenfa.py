import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#line domain
xmin = 0.0
xmax = np.pi
nx = 64
dx = (xmax-xmin)/nx

#time interval
tmin = 0.0
tmax = 1.0
nt = 1024
dt = (tmax-tmin)/nt

c = 1.0 #spreading coefficient

M = 51 #maximam fourier number

#initialize
F = np.zeros(nx)

T = np.linspace(tmin, tmax, nt, endpoint = False)
X = np.linspace(0, np.pi, nx, endpoint = False)+dx/2
F = np.cos(4*X)
for i in range(nx//2):
    F[i] = 1

## 前进差分法
rsq = c*dt/(dx**2) #constant

#solution
v = np.zeros((nt,nx))

#initial data
v[0] = F
print(len(F))

#simulation
for t in range(nt-1):
    for x in range(1,nx-1):
        v[t+1,x] = (1-2*rsq)*v[t,x]+rsq*(v[t,x-1]+v[t,x+1])
    #Neumann condition
    v[t+1,0] = v[t+1,1]
    v[t+1,nx-1] = v[t+1,nx-2]

## 动画
fig1 = plt.figure()
fig1.set_dpi(100)
ax = fig1.add_subplot(1,1,1)
def animate(t):
    ax.clear()
    plt.ylim([-1.2,1.5])
    
    p, = plt.plot(X,v[t])
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    time_text.set_text('t = %.2f/%.2f,' 
                       % ((t+1)/nt,tmax))
    
anim = animation.FuncAnimation(fig1,animate,frames=nt,interval=60,repeat=False)
plt.show()