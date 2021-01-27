import math

def main():
    H0 = (2.33*10**(-16))*6*6*24*365
    t = 0
    a = 1
    h = 0.001
    t1, a1 = eule(t,a,9999999,h)
    # print(a-H0)
    print(a1,t1)

def eule(t, a, tf, h):
    t_list = []
    a_list = []
    while(a>=0):
        a_list.append(a)
        t_list.append(t)
        a -= h*dadt(a)
        t += h
    return t_list, a_list

def RungeKutta_method_1(t, a, tf, h):
    t_list = []
    a_list = []
    while(t<=tf):
        a_list.append(a)
        t_list.append(t)
        k1 = dadt(a)
        k2 = dadt(a + (h/2)*k1)
        k3 = dadt(a + (h/2)*k2)
        k4 = dadt(a + h*k3)
        a += (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t += h
    return t_list, a_list

def dadt(a):
    omga0 = 1
    H0 = 2.33*10
    return H0*math.sqrt((omga0/a)-(omga0-1))

if __name__ == "__main__":
    main()