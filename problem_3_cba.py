import numpy as np
import matplotlib.pyplot as plt

def Gauss_Seidel_method():
    U = np.zeros((100, 100), dtype=np.float)
    U[0] = 1
    corrmax = 1

    u1010 = []
    u5010 = []
    u5050 = []
    u8080 = []

    while corrmax>0.00001:
        corrmax = 0
        for i in range(1, 99):
            for j in range(1, 99):
                corr=1/4.0*(U[i+1][j]+U[i-1][j]+U[i][j+1]+U[i][j-1])- U[i][j]
                U[i][j] += corr
                corrmax = np.maximum(abs(corr), corrmax)
        u1010.append(U[10][10])
        u5010.append(U[50][10])
        u5050.append(U[50][50])
        u8080.append(U[80][80])
        if len(u1010)%100==0:
            print(len(u1010))
    return u1010, u5010, u5050, u8080, U


def SOR(w):
    U = np.zeros((100, 100), dtype=np.float)
    U[0] = 1
    corrmax = 1

    u1010 = []
    u5050 = []
    u8080 = []

    print("Now w = %f" % w)

    while corrmax>0.00001:
        corrmax = 0
        for i in range(1, 99):
            for j in range(1, 99):
                corr=w/4.0*(U[i+1][j]+U[i-1][j]+U[i][j+1]+U[i][j-1]) - w*U[i][j]
                U[i][j] += corr
                corrmax = np.maximum(abs(corr), corrmax)
        u1010.append(U[10][10])
        u5050.append(U[50][50])
        u8080.append(U[80][80])
        if len(u1010)%100==0:
            print(len(u1010))
    return u1010, u5050, u8080


def main():
    print("c")
    u1010, u5010, u5050, u8080, U = Gauss_Seidel_method()
    fig = plt.figure(figsize=(12, 10))
    ax0 = fig.add_subplot(221, title="U[10][10]")
    plt.plot(u1010)
    ax0 = fig.add_subplot(222, title="U[50][10]")
    plt.plot(u5010)
    ax0 = fig.add_subplot(223, title="U[50][50]")
    plt.plot(u5050)
    ax0 = fig.add_subplot(224, title="U[80][80]")
    plt.plot(u8080)
    plt.show()

    print("b")
    plt.imshow(U, cmap='gray')
    plt.show()

    print("a")
    ua1010, ua5050, ua8080 = SOR(2/(1+np.sin(np.pi/100)))
    ua12_1010, ua12_5050, ua12_8080 = SOR(1.2)
    ua14_1010, ua14_5050, ua14_8080 = SOR(1.4)
    ua16_1010, ua16_5050, ua16_8080 = SOR(1.6)
    ua18_1010, ua18_5050, ua18_8080 = SOR(1.8)

    fig = plt.figure(figsize=(12, 8))

    ax0 = fig.add_subplot(221, title="U[10][10]")
    plt.plot(ua1010, label='w_opt')
    plt.plot(ua12_1010, label='1.2')
    plt.plot(ua14_1010, label='1.4')
    plt.plot(ua16_1010, label='1.6')
    plt.plot(ua18_1010, label='1.8')
    plt.plot(u1010, label='1.0')
    plt.legend(loc='upper right', fontsize=12)

    ax0 = fig.add_subplot(222, title="U[50][50]")
    plt.plot(ua5050, label='w_opt')
    plt.plot(ua12_5050, label='1.2')
    plt.plot(ua14_5050, label='1.4')
    plt.plot(ua16_5050, label='1.6')
    plt.plot(ua18_5050, label='1.8')
    plt.plot(u5050, label='1.0')
    plt.legend(loc='upper right', fontsize=12)

    ax0 = fig.add_subplot(223, title="U[80][80]")
    plt.plot(ua8080, label='w_opt')
    plt.plot(ua12_8080, label='1.2')
    plt.plot(ua14_8080, label='1.4')
    plt.plot(ua16_8080, label='1.6')
    plt.plot(ua18_8080, label='1.8')
    plt.plot(u8080, label='1.0')
    plt.legend(loc='upper right', fontsize=12)

    plt.show()


if __name__ == '__main__':
    main()