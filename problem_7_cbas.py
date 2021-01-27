import numpy as np

# b課題
def skip_func(u):
    
    if u<0:
        return 0
    return 1

def Skip_func(u):
    for i in range(len(u)):
        u[i] = skip_func(u[i])
    return u


w = np.array([1,1,-0.5])
x = np.array([0,0,1])
u = np.dot(w,x)
z = skip_func(u)
print(z)


# a課題
w1 = np.array([-2, 3, 1])
w2 = np.array([-2, 1, -0.5])
w3 = np.array([-2,1,1])

x = np.array([[0, 0, 1],
             [0, 1, 1],
             [1, 0, 1],
             [1, 1, 1]])


def xor(x,w3):
    u1 = np.dot(x, w1)
    u2 = np.dot(x, w2)

    z1 = Skip_func(u1)
    z2 = Skip_func(u2)
    

    u3 = np.dot(np.array([z1,z2,1]), w3)

    z3 = Skip_func(u3)
    return z3

a = xor(x,w3)

print(a)


# s課題
w1 = np.array([-2, 3, 1])
w2 = np.array([-2, 1, -0.5])
w3 = np.array([1, 1, 1])

x = np.array([[0, 0, 1],
             [0, 1, 1],
             [1, 0, 1],
             [1, 1, 1]])

y = np.array([0, 1, 1, 0])

u1 = np.dot(x, w1)
u2 = np.dot(x, w2)

z1 = Skip_func(u1)
z2 = Skip_func(u2)

def one_step(e, w3):
    E = y - xor(x,w3)
    w3[0] += np.dot(z1, E*e)
    w3[1] += np.dot(z2, E*e)
    
for i in range(9):
    one_step(0.5, w3)

print(w3)