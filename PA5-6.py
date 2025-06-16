import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#cell3
ptsMixA = pd.read_excel(r'C:\Users\danie\Downloads\ptsMixA.xlsx').values
X = ptsMixA[0, :].reshape(-1, 1)
Y = ptsMixA[1, :].reshape(-1, 1)

#Cell 1
def linefit(X, Y):
    D = np.hstack((np.ones_like(X), X))
    beta = np.linalg.inv(D.T @ D) @ D.T @ Y
    return beta, D

#Cell 2
def quadfit(X, Y):
    D = np.hstack((np.ones_like(X), X, X**2))
    beta = np.linalg.inv(D.T @ D) @ D.T @ Y
    return beta, D

def rms_error(Y, Y_est):
    e = Y - Y_est                    # Residual vector (ε)
    N = len(Y)
    return np.sqrt((e.T @ e) / N)[0, 0]  # Matrix version, extract scalar from 1x1 matrix

#cell 4
beta_L, D_L = linefit(X, Y)
Y_Lfit = D_L @ beta_L
rms_L = rms_error(Y, Y_Lfit)


plt.figure()
plt.plot(X, Y_Lfit, 'r-', label='Linear fit')  # red line
plt.plot(X, Y, 'o', markerfacecolor='none', markeredgecolor='b', label='Measured')  # hollow blue circles
plt.title('Linear Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()


print("Linear Fit Beta:\n", beta_L)
print("RMS Error (Linear):", rms_L)

# cell 5
beta_Q, D_Q = quadfit(X, Y)
Y_Qfit = D_Q @ beta_Q
rms_Q = rms_error(Y, Y_Qfit)

plt.figure()
plt.plot(X, Y_Qfit, 'r-', label='Quadratic fit')
plt.plot(X, Y, 'bo', markerfacecolor='none', markeredgecolor='b', label='Measured')
plt.title('Quadratic Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

print("Quadratic Fit Beta:\n", beta_Q)
print("RMS Error (Quadratic):", rms_Q)

# cell 6

# The quadratic fit is better for this problem as it captures the curvature in the data more effectively than the linear fit.
# The RMS error for the quadratic fit is lower than that for the linear fit, indicating a better fit to the data.