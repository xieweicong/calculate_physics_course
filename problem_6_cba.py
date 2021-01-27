import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv("decay1.dat", sep = ".", header=None, names=["x1", "x2", "y"], index_col=False)

df2 = pd.read_csv("decay2.dat", sep = ".", header=None, names=["x1", "x2", "y"], index_col=False)

# c課題1
y_err = np.sqrt(df1["y"])
plt.errorbar(df1["x1"]+0.5, df1["y"], yerr = y_err)
plt.show()
y_err2 = np.sqrt(df2["y"])
plt.errorbar(df2["x1"]+0.5, df2["y"], yerr = y_err2)
plt.show()

# c課題2
df1_log = pd.read_csv("decay1.dat", sep = ".", header=None, names=["x1", "x2", "y"], index_col=False)
df2_log = pd.read_csv("decay2.dat", sep = ".", header=None, names=["x1", "x2", "y"], index_col=False)

df1_log["y"] = np.log(df1["y"])
df2_log["y"] = np.log(df2["y"])

y_err3 = np.sqrt(df1["y"])/df1["y"]
y_err4 = np.sqrt(df2["y"])/df2["y"]

plt.errorbar(df1_log["x1"], df1_log["y"], yerr=y_err3)
plt.show()
plt.errorbar(df2_log["x1"], df2_log["y"], yerr=y_err4)
plt.show()


# b課題
k1 = np.sum(df1_log["x1"]**2/y_err3**2)
k2 = np.sum(df1_log["x1"]/y_err3**2)
k3 = np.sum(df1_log["x1"]*df1_log["y"]/y_err3**2)

k4 = np.sum(df1_log["x1"]/y_err3**2)
k5 = np.sum(1/y_err3**2)
k6 = np.sum(df1_log["y"]/y_err3**2)

A1 = np.array([[k1,k2],[k4,k5]])
b1 = np.array([k3,k6])
r1 = np.linalg.solve(A1,b1)
print(r1)

plt.errorbar(df1_log["x1"], df1_log["y"], yerr=y_err3)
x = np.linspace(1, 18, 18) 
plt.plot(x, r1[0]*x + r1[1])
plt.show()


k1 = np.sum(df2_log["x1"]**2/y_err4**2)
k2 = np.sum(df2_log["x1"]/y_err4**2)
k3 = np.sum(df2_log["x1"]*df2_log["y"]/y_err4**2)

k4 = np.sum(df2_log["x1"]/y_err4**2)
k5 = np.sum(1/y_err4**2)
k6 = np.sum(df2_log["y"]/y_err4**2)

A2 = np.array([[k1,k2],[k4,k5]])
b2 = np.array([k3,k6])
r2 = np.linalg.solve(A2,b2)
print(r2)

plt.errorbar(df2_log["x1"], df2_log["y"], yerr=y_err4)
x = np.linspace(1, 13, 13) 
plt.plot(x, r2[0]*x + r2[1])
plt.show()

delta = np.sum(1/y_err3**2)*np.sum(df1_log["x1"]**2/y_err3**2)-np.sum(
df1_log["x1"]/y_err3**2)**2
gosaa = np.sum(1/y_err3**2)/delta
gosab = np.sum(df1_log["x1"]**2/y_err3**2)/delta
print(gosaa,gosab)

delta = np.sum(1/y_err4**2)*np.sum(df2_log["x1"]**2/y_err4**2)-np.sum(
df2_log["x1"]/y_err4**2)**2
gosaa = np.sum(1/y_err4**2)/delta
gosab = np.sum(df2_log["x1"]**2/y_err4**2)/delta
print(gosaa,gosab)

X1 = np.sum((df1_log["y"]-r1[0]*df1_log["x1"]-r1[1])**2/y_err3)
X2 = np.sum((df2_log["y"]-r2[0]*df2_log["x1"]-r2[1])**2/y_err4)
print(X1, X2)