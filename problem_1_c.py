import matplotlib.pyplot as plt

def main():
    al1 = 13.8
    pb1 = 74.2
    al03 = 0.552
    pb03 = 12.8

    al_p = 2.7
    pb_p = 11.35

    u = pb1*al_p
    x = 0
    y = 1.0
    xf = 1
    h = 0.005

    x_r, y_r = RungeKutta_method_1(u, x, y, xf, h)
    x_2 = RungeKutta_method_2(u, x, y, h)
    # print(y)
    print(x_2)
    x_e, y_e = eule(u, x, y, xf, h)
    # print(y)
    plt.subplot(1,2,1)
    plt.plot(x_r, y_r)
    plt.subplot(1,2,2)
    plt.plot(x_e, y_e)
    plt.show()

def RungeKutta_method_1(u, x, y, xf, h):
    x_list = []
    y_list = []
    while(x<=xf):
        y_list.append(y)
        x_list.append(x)
        k1 = dy(u, y)
        k2 = dy(u, y + (h/2)*k1)
        k3 = dy(u, y + (h/2)*k2)
        k4 = dy(u, y + h*k3)
        y += (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x += h
    return x_list, y_list

def RungeKutta_method_2(u, x, y, h):
    while(y>0.01):
        k1 = dy(u, y)
        k2 = dy(u, y + (h/2)*k1)
        k3 = dy(u, y + (h/2)*k2)
        k4 = dy(u, y + h*k3)
        y += (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        x += h
    return x

def eule(u, x, y, xf, h):
    x_list = []
    y_list = []
    while(x<=xf):
        y_list.append(y)
        x_list.append(x)
        y += h*dy(u, y)
        x += h
    return x_list, y_list


def dy(u, y):
    return -u*y


if __name__ == "__main__":
    main()